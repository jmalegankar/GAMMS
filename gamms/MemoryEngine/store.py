# from typing.memory_engine import IPathLike, IStoreType, IStore
import os
from abc import ABC, abstractmethod
from typing import Any, List
from enum import Enum

class IPathLike(ABC):
    pass

class IStoreType(Enum):
    FILE = 1
    REMOTE = 2
    DATABASE = 3

class IStore(ABC):
    def __init__(self, name: str, store_type: IStoreType, path: IPathLike):
        self.name = name 
        self.store_type = store_type
        self.path = path
        
    @abstractmethod
    def save(self, obj: Any) -> None:
        pass

    @abstractmethod
    def load(self) -> Any:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

class PathLike(IPathLike):
    def __init__(self, path: str):
        self.path = path
    
    def __post_init__(self):
        """
        Convert absolute path to relative path if necessary.
        """
        os.makedirs(self.path, exist_ok=True) 
        if os.path.isabs(self.path):
            self.path = os.path.relpath(self.path)


#only implementing for filesystem for now
class Store(IStore):
    def __init__(self, name: str, store_type: IStoreType, path: PathLike):
        self.name = name  # name of file, table, etc.
        self.store_type = store_type # type of store
        self.path = path # parent directory

    def save(self, obj):
        if self.store_type == IStoreType.FILE:
            os.makedirs(self.path, exist_ok=True) 
            file_path = os.path.join(self.path, self.name)
            with open(file_path, 'w') as file:
                if isinstance(obj, str) and os.path.exists(obj):
                    with open(obj, 'r') as object_file:
                        file.write(object_file.read())
                else:
                    file.write(str(obj))

    def load(self):
        if self.store_type == IStoreType.FILE:
            file_path = os.path.join(self.path, self.name)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Store file '{file_path}' does not exist.")
            with open(file_path, 'r') as file:
                return file.read()

    def delete(self) -> None:
       if self.store_type == IStoreType.FILESYSTEM:
            file_path = os.path.join(self.path, self.name)
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                raise FileNotFoundError(f"Store file '{file_path}' does not exist.")

import os
import pandas as pd

def test_save_dataframe():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    # Define the path and store
    path = PathLike('./test_dir')
    store = Store('test_df.csv', IStoreType.FILE, path)

    # Save the DataFrame to a CSV file
    df.to_csv(os.path.join(path.path, store.name), index=False)
    store.save(os.path.join(path.path, store.name))

    # Load the saved DataFrame
    loaded_df = pd.read_csv(os.path.join(path.path, store.name))

    # Check if the saved DataFrame matches the original DataFrame
    pd.testing.assert_frame_equal(df, loaded_df)

    # Clean up
    store.delete()
    os.rmdir(path.path)

if __name__ == '__main__':
    test_save_dataframe()
    print("Test passed.")