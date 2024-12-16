from graph_engine import GraphEngine
from agent_engine import AgentEngine
from graph_visual import GraphVisual
from agent_visual import AgentVisual
from visual_engine import VisualizationEngine

if __name__ == "__main__":
    # Initialize the graph engine and create the graph
    graph_engine = GraphEngine()
    location = "West Point, New York, USA"
    graph = graph_engine.create_graph_from_location(location)

    # Initialize the agent engine (5 red agents and 5 blue agents)
    agent_engine = AgentEngine(graph, num_red_agents=5, num_blue_agents=5)

    # Set up the visualization components
    graph_visual = GraphVisual(graph)
    agent_visual = AgentVisual(agent_engine)

    # Initialize and run the visualization engine
    visualization = VisualizationEngine(None, graph_visual, agent_visual)
    visualization.run_game_loop()
