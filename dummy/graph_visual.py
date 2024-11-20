import pygame


class GraphVisual:
    def __init__(self, graph, width=1920, height=1080):
        self.graph = graph
        self.width = width
        self.height = height

        # Find the min and max x, y coordinates for scaling
        self.x_min = min(node.x for node in self.graph.nodes.values())
        self.x_max = max(node.x for node in self.graph.nodes.values())
        self.y_min = min(node.y for node in self.graph.nodes.values())
        self.y_max = max(node.y for node in self.graph.nodes.values())

    def scale(self, value, min_val, max_val, screen_min, screen_max):
        """Scale a coordinate value to fit within the screen."""
        return screen_min + (value - min_val) * (screen_max - screen_min) / (max_val - min_val)

    def draw_node(self, screen, node):
        """Draw a node as a circle with a light greenish color."""
        x = self.scale(node.x, self.x_min, self.x_max, 50, self.width - 50)
        y = self.scale(node.y, self.y_min, self.y_max, 50, self.height - 50)
        pygame.draw.circle(screen, (173, 255, 47), (int(x), int(y)), 6)  # Light greenish color

    def draw_edge(self, screen, edge):
        """Draw an edge as a curve or straight line based on the linestring."""
        source = self.graph.nodes[edge.source]
        target = self.graph.nodes[edge.target]

        # If linestring is present, draw it as a curve
        if edge.linestring:
            linestring = [(source.x, source.y)] + edge.linestring[1:-1] + [(target.x, target.y)]
            scaled_points = [
                (self.scale(x, self.x_min, self.x_max, 50, self.width - 50),
                 self.scale(y, self.y_min, self.y_max, 50, self.height - 50))
                for x, y in linestring
            ]
            pygame.draw.aalines(screen, (0, 0, 0), False, scaled_points, 2)
        else:
            # Straight line
            x1 = self.scale(source.x, self.x_min, self.x_max, 50, self.width - 50)
            y1 = self.scale(source.y, self.y_min, self.y_max, 50, self.height - 50)
            x2 = self.scale(target.x, self.x_min, self.x_max, 50, self.width - 50)
            y2 = self.scale(target.y, self.y_min, self.y_max, 50, self.height - 50)
            pygame.draw.line(screen, (0, 0, 0), (int(x1), int(y1)), (int(x2), int(y2)), 2)

    def draw_graph(self, screen):
        """Draw the entire graph (edges and nodes)."""
        for edge in self.graph.edges.values():
            self.draw_edge(screen, edge)

        for node in self.graph.nodes.values():
            self.draw_node(screen, node)
