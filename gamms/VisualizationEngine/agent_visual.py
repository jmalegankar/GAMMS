import pygame
import math


class AgentVisual:
    def __init__(self, name, **kwargs):
        """
        Initialize AgentVisual with an AgentEngine.
        """
        self.name = name
        self.color = kwargs.get('color', (255, 0, 0))
        self.size = kwargs.get('size', 500)
        self.shape = kwargs.get('shape', None)
        self.prev_position = None
        self.position = None
    

    def set_positions(self, prev_position, position):
        self.prev_position = prev_position
        self.position = position
    
    def follow_path(self, path):
        pass
        #etc etc etc 

    

        
    

"""

class AgentVisual:
    def __init__(self, agent_engine):

        self.agent_engine = agent_engine

    def move_agents(self):
        self.agent_engine.step_all_agents()

    def draw_agents(self, screen, scale_func, x_min, x_max, screen_width, screen_height, y_min, y_max):

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
"""