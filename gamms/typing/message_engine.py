from abc import ABC, abstractmethod
from typing import Optional, Any, List

class IMessageEngine(ABC):
    @abstractmethod
    def generate_channel_name(self) -> str:
        pass

    @abstractmethod
    def create_publisher(
        self,
        tensor: Any,
        channel_name: Optional[str],
        ttl: int,
        ) -> None:
        pass

    @abstractmethod
    def create_subscriber(
        self,
        channel_name: str,
        ) -> None:
        pass

    @abstractmethod
    def list_active_channels(self) -> List[str]:
        pass