from abc import ABC, abstractmethod
from typing import Any, Dict
from enum import Enum

class SensorType(Enum):
    NEIGHBOR = 1
    MAP = 2
    AGENT = 3

class ISensor(ABC):
    type: SensorType
    data: Dict[str, Any]

    @abstractmethod
    def sense(self, node_id: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def update(self, data: Dict[str, Any]):
        pass

class ISensorEngine(ABC):
    @abstractmethod
    def create_sensor(self, sensor_type: Enum, sensor_data: Dict[str, Any]):
        pass

    @abstractmethod
    def get_sensor(self, id) -> ISensor:
        pass

    @abstractmethod
    def terminate(self):
        pass