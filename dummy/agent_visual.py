import pygame
import math
from agent_engine import AgentEngine, Agent


class AgentVisual:
    def __init__(self, agent_engine):
        """
        Initialize AgentVisual with an AgentEngine.
        """
        self.agent_engine: AgentEngine = agent_engine

    def move_agents(self):
        """
        Update the movement of all agents.
        """
        self.agent_engine.step_all_agents()

    def draw_agents(self, screen, scale_func, x_min, x_max, screen_width, screen_height, y_min, y_max):
        """
        Draw all agents on the screen using their updated state and respective color.
        """
        for agent_state in self.agent_engine.get_all_states():
            position = agent_state["position"]
            color = agent_state.get("color", (255, 0, 0))  # Default color is red if not provided
            (scaled_x, scaled_y) = scale_func(position)
            # Draw each agent as a triangle at its current position
            size = 8  # Triangle size
            angle = math.radians(45)
            point1 = (scaled_x + size * math.cos(angle), scaled_y + size * math.sin(angle))
            point2 = (scaled_x + size * math.cos(angle + 2.5), scaled_y + size * math.sin(angle + 2.5))
            point3 = (scaled_x + size * math.cos(angle - 2.5), scaled_y + size * math.sin(angle - 2.5))

            pygame.draw.polygon(screen, color, [point1, point2, point3])

    def get_closest_agent(self, x, y) -> Agent:
        """
        Get the closest agent to a given position (x, y).
        """
        closest_agent = None
        closest_distance = float("inf")
        for agent in self.agent_engine.agents:
            position = agent.position
            distance = math.hypot(position[0] - x, position[1] - y)
            if distance < closest_distance:
                closest_distance = distance
                closest_agent = agent
        return closest_agent
