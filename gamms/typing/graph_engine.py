from abc import ABC, abstractmethod
from typing import Any, Dict, Type, List, Tuple
from dataclasses import dataclass

@dataclass
#change name in future
class Node:
    id: int
    x: float
    y: float

@dataclass
class OSMEdge:
    id: int
    source: int #Node ID
    target: int #Node ID
    length: float
    linestring: List[Tuple[float, float]] = None


class IGraph(ABC):
    @abstractmethod
    def add_node(self, node_data: Dict[str, Any]):
        pass

    @abstractmethod
    def add_edge(self, edge_data: Dict[str, Any]):
        pass

    @abstractmethod
    def get_nodes(self) -> List[int]:
        pass

    @abstractmethod
    def get_edges(self) -> List[int]:
        pass

    @abstractmethod
    def update_node(self, node_data: Dict[str, Any]):
        pass

    @abstractmethod
    def update_edge(self, edge_data: Dict[str, Any]):
        pass

    @abstractmethod
    def remove_node(self, node_id: int):
        pass

    @abstractmethod
    def remove_edge(self, edge_id: int):
        pass

    @abstractmethod
    def get_node(self, node_id: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_edge(self, edge_id: int) -> Dict[str, Any]:
        pass


class IGraphEngine(ABC):
    @property
    @abstractmethod
    def graph(self) -> IGraph:
        pass

    @abstractmethod
    def create_graph(self, node_struct: Type, edge_struct: Type):
        pass

    @abstractmethod
    def terminate(self):
        pass