from gamms.VisualizationEngine import Color, Shape
from gamms.VisualizationEngine.Nodes.render_node import RenderNode
# from gamms.VisualizationEngine.Nodes.circle_node import CircleNode
from gamms.context import Context
import pygame


class RenderManager:
    def __init__(self, ctx: Context):
        self.ctx: Context = ctx
        self._render_nodes: dict[str, RenderNode] = {}

    def add_render_node(self, name: str, render_node: RenderNode):
        self._render_nodes[name] = render_node

    def remove_render_node(self, name: str):
        if name in self._render_nodes:
            del self._render_nodes[name]
        else:
            print(f"Warning: Render node {name} not found.")
        # self._render_nodes.pop(name)

    def handle_render(self):
        for render_node in self._render_nodes.values():
            if 'drawer' in render_node.data:
                drawer = render_node.drawer
                drawer(self.ctx, render_node.data)
                continue

            shape = render_node.shape
            if shape == Shape.Circle:
                RenderManager.render_circle(self.ctx, render_node.x, render_node.y, render_node.data['scale'], render_node.color)
            else:
                raise NotImplementedError("Render node not implemented")

    @staticmethod
    def render_circle(ctx: Context, x: float, y: float, radius: float, color: tuple=Color.Black):
        (x, y) = ctx.visual._graph_visual.ScalePositionToScreen((x, y))
        pygame.draw.circle(ctx.visual._screen, color, (x, y), radius)