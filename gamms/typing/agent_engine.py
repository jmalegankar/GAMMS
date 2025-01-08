from abc import ABC, abstractmethod

class IAgent(ABC):
    """
    Abstract base class representing an agent in the system.

    Attributes:
        name (str): The name identifier for the agent.
    """

    name: str

    @abstractmethod
    def step(self):
        """
        Execute a single operational step of the agent.

        This method should contain the logic that defines the agent's behavior
        during one iteration or time step in the system.
        """
        pass

    @abstractmethod
    def get_state(self):
        """
        Retrieve the current state of the agent.

        Returns:
            Any: The current state data of the agent, structure depends on implementation.
        """
        pass

    @abstractmethod
    def set_state(self, state):
        """
        Update the agent's state.

        Args:
            state (Any): The new state data to set for the agent.
        """
        pass

    @abstractmethod
    def register_sensor(self, name, sensor):
        """
        Register a sensor with the agent.

        Sensors can be used by the agent to perceive the environment or gather data.

        Args:
            name (str): The unique name identifier for the sensor.
            sensor (Any): The sensor instance or object to be registered.
        """
        pass

    @abstractmethod
    def register_strategy(self, strategy):
        """
        Register a strategy with the agent.

        Strategies define the decision-making or action-planning mechanisms for the agent.

        Args:
            strategy (Any): The strategy instance or object to be registered.
        """
        pass


class IAgentEngine(ABC):
    """
    Abstract base class representing the engine that manages agents.

    The engine is responsible for creating, managing, and terminating agents,
    as well as facilitating interactions between them.
    """

    @abstractmethod
    def create_iter(self):
        """
        Create an iterator for processing agent steps.

        Returns:
            Any: An iterator object that manages the execution flow of agent steps.
        """
        pass

    @abstractmethod
    def create_agent(self, start_node_id: int, **kwargs):
        """
        Instantiate a new agent within the engine.

        Args:
            start_node_id (int): The identifier for the starting node or position of the agent.
            **kwargs: Additional keyword arguments for agent initialization.

        Returns:
            IAgent: The newly created agent instance.
        """
        pass

    @abstractmethod
    def terminate(self):
        """
        Terminate the agent engine and perform necessary cleanup operations.

        This method should ensure that all resources are properly released and
        that agents are gracefully shut down.
        """
        pass

    @abstractmethod
    def get_agent(self, name: str) -> IAgent:
        pass

    @abstractmethod
    def delete_agent(self, name: str) -> None:
        """
        Retrieve an agent by its name.

        Args:
            name (str): The unique name identifier of the agent to retrieve.

        Returns:
            IAgent: The agent instance corresponding to the provided name.

        Raises:
            KeyError: If no agent with the specified name exists.
        """
        pass
