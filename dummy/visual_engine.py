import pygame


class VisualizationEngine:
    def __init__(self, graph_visual, agent_visual, width=1920, height=1080):
        pygame.init()
        self.graph_visual = graph_visual
        self.agent_visual = agent_visual
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Graph and Agent Visualization")
        self.clock = pygame.time.Clock()

    def run(self):
        """Main visualization loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))

            # Draw the graph
            self.graph_visual.draw_graph(self.screen)

            # Update agent positions and draw them
            self.agent_visual.move_agents()  # Step all agents
            self.agent_visual.draw_agents(
                self.screen,
                self.graph_visual.scale,
                self.graph_visual.x_min,
                self.graph_visual.x_max,
                self.width,
                self.height,
                self.graph_visual.y_min,
                self.graph_visual.y_max
            )

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
