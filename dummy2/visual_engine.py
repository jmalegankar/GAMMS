from gamms.typing import IVisualizationEngine
from constants import *
from camera import Camera
import pygame
import math

class VisualizationEngine(IVisualizationEngine):
    width: int
    """
    The width of the screen.
    """

    height: int
    """
    The height of the screen.
    """

    screen: pygame.Surface
    """
    The pygame screen object.
    """

    clock: pygame.time.Clock
    """
    The pygame clock object.
    """

    default_font: pygame.font.Font
    """
    The default font for rendering text.
    """

    camera: Camera
    """
    The scene camera.
    """

    def __init__(self, tick_callback, graph_visual, agent_visual, width=1980, height=1080):
        pygame.init()
        self.width = width
        self.height = height
        self.graph_visual = graph_visual
        self.agent_visual = agent_visual
        self.zoom = 1.0
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.default_font = pygame.font.Font(None, 36)
        self.camera = Camera(self, 0, 0, 15)
        self.graph_visual.setCamera(self.camera)
    
    def handle_input(self):
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            # Multi key Event
            if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_w]:
                self.camera.x += 1
                self.camera.y += -1
                return
            if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_s]:
                self.camera.x += 1
                self.camera.y += 1
                return
            if pressed_keys[pygame.K_s] and pressed_keys[pygame.K_d]:
                self.camera.x += -1
                self.camera.y += 1
                return
            if pressed_keys[pygame.K_d] and pressed_keys[pygame.K_w]:
                self.camera.x += -1
                self.camera.y += -1
                return
            if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_d]:
                return
            if pressed_keys[pygame.K_w] and pressed_keys[pygame.K_s]:
                return
            
            # Single Input Event
            if pressed_keys[pygame.K_a]:
                self.camera.x += 1
                self.camera.y += 0
                return
            if pressed_keys[pygame.K_s]:
                self.camera.x += 0
                self.camera.y += 1
                return
            if pressed_keys[pygame.K_d]:
                self.camera.x += -1
                self.camera.y += 0
                return
            if pressed_keys[pygame.K_w]:
                self.camera.x += 0
                self.camera.y += -1
                return
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.camera.size /= 1.05
                    if(self.camera.size > 2):
                        self.zoom *= 1.05
                        self.zoom = self.graph_visual.setZoom(self.zoom)
                else:
                    self.camera.size *= 1.05
                    if(self.camera.size < 350):
                        self.zoom /= 1.05
                        self.zoom = self.graph_visual.setZoom(self.zoom)
            if event.type == pygame.QUIT:
                self.will_quit = True
            if event.type == pygame.VIDEORESIZE:
                self.width = event.w
                self.height = event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def handle_tick(self):
        self.clock.tick()

    def handle_single_draw(self):
        self.screen.fill(Color.White)
        self._draw_grid()

        top = 10
        size_x, size_y = self.render_text("Some instructions here", 10, top, Space.Screen)
        top += size_y + 10
        size_x, size_y = self.render_text(f"Camera size: {self.camera.size:.2f}", 10, top, Space.Screen)
        top += size_y + 10
        size_x, size_y = self.render_text("Current turn: Red", 10, top, Space.Screen)

        # Draw the graph
        self.graph_visual.draw_graph(self.screen)

        # Update agent positions and draw them
        # self.agent_visual.move_agents()  # Step all agents
        # self.agent_visual.draw_agents(
        #     self.screen,
        #     self.graph_visual.ScalePositionToScreen,
        #     self.graph_visual.x_min,
        #     self.graph_visual.x_max,
        #     self.width,
        #     self.height,
        #     self.graph_visual.y_min,
        #     self.graph_visual.y_max
        # )

    def cleanup(self):
        pygame.quit()

    def render_text(self, text: str, x: int, y: int, coord_space: Space=Space.World, color: tuple=Color.Black):
        # self.default_font.size
        if coord_space == Space.World:
            screen_x, screen_y = self.camera.world_to_screen(x, y)
        elif coord_space == Space.Screen:
            screen_x, screen_y = x, y
        elif coord_space == Space.Viewport:
            screen_x, screen_y = self.camera.viewport_to_screen(x, y)
        else:
            raise ValueError("Invalid coord_space value. Must be one of the values in the Space enum.")
        
        text_surface = self.default_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(screen_x, screen_y))
        text_size = self.default_font.size(text)
        text_rect = text_rect.move(text_size[0] // 2, text_size[1] // 2)
        self.screen.blit(text_surface, text_rect)

        if coord_space == Space.World:
            return self.camera.screen_to_world_scale(text_size[0]), self.camera.screen_to_world_scale(text_size[1])
        elif coord_space == Space.Screen:
            return text_size
        elif coord_space == Space.Viewport:
            return self.camera.screen_to_viewport_scale(text_size[0]), self.camera.screen_to_viewport_scale(text_size[1])
        else:
            raise ValueError("Invalid coord_space value. Must be one of the values in the Space enum.")

    def render_circle(self, x: float, y: float, radius: float, color: tuple=Color.Black):
        screen_x, screen_y = self.camera.world_to_screen(x, y)
        screen_radius = self.camera.world_to_screen_scale(radius)
        pygame.draw.circle(self.screen, color, (screen_x, screen_y), screen_radius)

    def render_rectangle(self, x: float, y: float, width: float, height: float, color: tuple=Color.Black):
        """
        Renders a rectangle on the screen. x and y are the left and top world coordinates of the rectangle.
        """
        screen_x, screen_y = self.camera.world_to_screen(x, y)
        screen_width = self.camera.world_to_screen_scale(width)
        screen_height = self.camera.world_to_screen_scale(height)
        pygame.draw.rect(self.screen, color, pygame.Rect(screen_x, screen_y, screen_width, screen_height))


    def render_line(self, start_x: float, start_y: float, end_x: float, end_y: float, color: tuple=Color.Black, width: int=1, isAA: bool=False):
        """
        Renders a line on the screen. Coordinates are in world space.
        Args:
            start_x (float): The x-coordinate of the starting point in world coordinates.
            start_y (float): The y-coordinate of the starting point in world coordinates.
            end_x (float): The x-coordinate of the ending point in world coordinates.
            end_y (float): The y-coordinate of the ending point in world coordinates.
            color (tuple, optional): The color of the line. Defaults to Color.Black.
            width (int, optional): The width of the line. Only works when drawing non anti-aliasing line. Defaults to 1.
            isAA (bool, optional): Whether to use anti-aliasing for the line. Defaults to False.
        Returns:
            None
        """
        
        screen_start_x, screen_start_y = self.camera.world_to_screen(start_x, start_y)
        screen_end_x, screen_end_y = self.camera.world_to_screen(end_x, end_y)
        if isAA:
            pygame.draw.aaline(self.screen, color, (screen_start_x, screen_start_y), (screen_end_x, screen_end_y))
        else:
            pygame.draw.line(self.screen, color, (screen_start_x, screen_start_y), (screen_end_x, screen_end_y), width)

    def _draw_grid(self):
        """
        Draws the grid on the screen.
        """
        x_min = self.camera.x - self.camera.size * 4
        x_max = self.camera.x + self.camera.size * 4
        y_min = self.camera.y - self.camera.size_y * 4
        y_max = self.camera.y + self.camera.size_y * 4
        step = 1
        for x in range(int(x_min), int(x_max) + 1, step):
            self.render_line(x, y_min, x, y_max, Color.LightGray, 3 if x % 5 == 0 else 1, False)

        for y in range(int(y_min), int(y_max) + 1, step):
            self.render_line(x_min, y, x_max, y, Color.LightGray, 3 if y % 5 == 0 else 1, False)
    


        

