from gamms.VisualizationEngine import Color
from gamms.VisualizationEngine.Nodes.render_node import RenderNode
from gamms.VisualizationEngine.Nodes.circle_node import CircleNode
from gamms.context import Context
import pygame


class RenderManager:
    def __init__(self, ctx: Context):
        self.ctx: Context = ctx
        self._render_nodes: dict[str, RenderNode] = {}

    def add_render_node(self, name: str, render_node: RenderNode):
        self._render_nodes[name] = render_node

    def remove_render_node(self, name: str):
        self._render_nodes.pop(name)

    def handle_render(self):
        for render_node in self._render_nodes.values():
            if isinstance(render_node, CircleNode):
                self._render_circle(render_node.x, render_node.y, render_node.radius, render_node.color)
            else:
                raise NotImplementedError("Render node not implemented")

    def _render_circle(self, x: float, y: float, radius: float, color: tuple=Color.Black):
        (x, y) = self.ctx.visual._graph_visual.ScalePositionToScreen((x, y))
        pygame.draw.circle(self.ctx.visual._screen, color, (x, y), radius)