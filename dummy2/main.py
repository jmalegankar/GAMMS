from gamms.GraphEngine.graph_engine import GraphEngine
from agent_engine import AgentEngine
from graph_visual import GraphVisual
from agent_visual import AgentVisual
from gamms.VisualizationEngine.visualization_engine import VisualizationEngine
#from visualization_engine import VisualizationEngine
import pygame


if __name__ == "__main__":
    # Initialize the graph engine and create the graph
    graph = GraphEngine()
    G = graph.load('/Users/jmalegaonkar/Desktop/GAMMS/examples/base/graph.npz')
    #G.visualize()

    # # Initialize the agent engine (5 red agents and 5 blue agents)
    # agent_engine = AgentEngine(G, num_red_agents=5, num_blue_agents=5)

    # # Set up the visualization components
    graph_visual = GraphVisual(G)
    # agent_visual = AgentVisual(agent_engine)

    # # # # Initialize and run the visualization engine
    visualization = VisualizationEngine(None, graph_visual, None)
    camera = visualization.camera
    screen = visualization.screen
    # while True:
    #     screen.fill((255, 255, 255))
    #     visualization.graph_visual.draw_graph(screen)
    #     pygame.display.flip()
    
    visualization.run_game_loop()
