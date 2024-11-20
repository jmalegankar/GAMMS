import random

class Agent:
    def __init__(self, graph, start_node_id, color=(255, 0, 0)):
        """Initialize the agent at a specific node with access to the graph and set the color."""
        self.graph = graph
        self.current_node_id = start_node_id
        self.previous_node_id = start_node_id
        self.target_node_id = None
        self.position = (self.graph.nodes[start_node_id].x, self.graph.nodes[start_node_id].y)
        self.path = []
        self.current_path_index = 0
        self.speed = 0.02  # Speed factor for animation
        self.color = color  # Color of the agent
        self.nearest_neighbors = []

    def update_nearest_neighbors(self):
        """Update the list of nearest neighbors based on the current node."""
        # Get neighbors based on graph edges
        self.nearest_neighbors = [
            edge.target if edge.source == self.current_node_id else edge.source
            for edge in self.graph.edges.values()
            if edge.source == self.current_node_id or edge.target == self.current_node_id
        ]

    def choose_random_edge(self):
        """Choose a random edge connected to the current node."""
        connected_edges = [
            edge for edge in self.graph.edges.values()
            if edge.source == self.current_node_id or edge.target == self.current_node_id
        ]
        if connected_edges:
            return random.choice(connected_edges)
        return None
    #move to agent visual
    def follow_edge(self, edge):
        """Set the agent to follow a given edge."""
        if edge.source == self.current_node_id:
            self.target_node_id = edge.target
            reverse = False
        else:
            self.target_node_id = edge.source
            reverse = True

        # Update the position to the final position of the last movement
        # (don't reset it to the node position, because it might be slightly off due to interpolation)
        self.position = (self.position[0], self.position[1])  # Keep the agent's current position

        # Get the path along the edge
        source = self.graph.nodes[edge.source]
        target = self.graph.nodes[edge.target]
        if edge.linestring:
            # If there's a curved edge (linestring), follow it
            self.path = [(source.x, source.y)] + edge.linestring[1:-1] + [(target.x, target.y)]
        else:
            # Otherwise, follow the straight line between nodes
            self.path = [(source.x, source.y), (target.x, target.y)]
        if reverse:
            self.path.reverse()

        if len(self.path) < 2:
            raise ValueError("Path between source and target must contain at least two points")

        self.current_path_index = 0
        self.speed = 0.02  # Reset the speed each time a new edge is followed


    #move to agent viusal 
    def move_along_path(self):
        """Move the agent smoothly along the current path."""
        if not self.path:
            return  # Exit if there's no path to follow

        if self.current_path_index < len(self.path) - 1:
            start = self.path[self.current_path_index]
            end = self.path[self.current_path_index + 1]

            #print(f"Agent {self} moving from {start} to {end} with speed {self.speed}")
            # Linear interpolation between start and end
            self.position = (
                start[0] * (1 - self.speed) + end[0] * self.speed,
                start[1] * (1 - self.speed) + end[1] * self.speed
            )

            # Gradually increase speed for smooth movement
            self.speed += 0.02
            if self.speed >= 1.0:
                #print(f"Agent {self} reached segment end, moving to next segment")
                # Move to the next segment of the path
                self.current_path_index += 1
                self.speed = 0.02  # Reset speed for the next segment

        # If the agent has reached the end of the path, snap to the final position
        if self.current_path_index >= len(self.path) - 1:
            #print(f"Agent {self} reached final position {self.path[-1]}")
            self.position = self.path[-1]  # Ensure the agent snaps to the final position
            self.previous_node_id = self.current_node_id  # Update previous node
            self.current_node_id = self.target_node_id  # Update to the new current node
            self.target_node_id = None  # Clear the target node
            self.current_path_index = 0  # Reset the path index
            self.path = []  # Clear the path



    def step(self):
        """Perform a full step, which updates neighbors, moves, and sends state to visualization."""
        if self.current_path_index >= len(self.path) - 1:
            # If we reached the end of the current path, choose a new edge
            self.update_nearest_neighbors()
            edge = self.choose_random_edge()
            if edge:
                self.follow_edge(edge)

        # Move along the current path
        self.move_along_path()

    def get_state(self) -> dict:
        """Get the current state of the agent."""
        return {"position": self.position, "current_node": self.current_node_id, "color": self.color}

class AgentEngine:
    def __init__(self, graph, num_red_agents=5, num_blue_agents=5):
        """Initialize the engine with two sets of agents: red and blue."""
        self.graph = graph
        self.agents = []

        # Create red agents, all starting at the same node
        node_ids = list(graph.nodes.keys())  # All agents start at the same node
        for _ in range(num_red_agents):
            red_agent = Agent(graph, random.choice(node_ids), color=(255, 0, 0))  # Red agents
            self.agents.append(red_agent)

        # Create blue agents, all starting at the same node
        for _ in range(num_blue_agents):
            blue_agent = Agent(graph, random.choice(node_ids) , color=(0, 0, 255))  # Blue agents
            self.agents.append(blue_agent)

    def step_all_agents(self):
        """Update all agents by calling their step function."""
        for agent in self.agents:
            agent.step()

    def get_all_states(self):
        """Get the state of all agents for visualization."""
        return [agent.get_state() for agent in self.agents]
