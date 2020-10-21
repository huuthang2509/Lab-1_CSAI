import pygame
import graphUI
import time
from node_color import white, yellow, black, red, blue, purple, orange, green

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""


def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # if edge_id(0,2) == edge_id(2,0):
    #     print("That true bro!")


    list_path = [[start]]
    while graph[goal][2] != white:
        path = list_path.pop(0)
        temp_node = path[-1]
        if graph[temp_node][3] != blue:
            graph[temp_node][3] = yellow
            graph[temp_node][2] = white
            graphUI.updateUI()
            restructed_node = list(graph[temp_node][1])
            for adjacency_node in graph[temp_node][1]:
                if graph[adjacency_node][3] != black and adjacency_node != goal:
                    restructed_node.remove(adjacency_node)
            for adjacency_node in restructed_node:
                graph[adjacency_node][3] = red
                graph[adjacency_node][2] = white
                edges[edge_id(temp_node, adjacency_node)][1] = white
                graphUI.updateUI()
                new_path = list(path)
                new_path.append(adjacency_node)
                list_path.append(new_path)
                if adjacency_node == goal:
                    result_path = new_path
                    break          
            graph[temp_node][3] = blue
            graphUI.updateUI()
    # print(result_path)
    for i in range (0, len(result_path) - 1):
        edges[edge_id(result_path[i], result_path[i+1])][1] = green
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
        
    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()

    previous_node = []
    for node in range(0, len(graph)):
        previous_node.append((node, None))
    previous_node = dict(previous_node) 
    previous_node[0] = -1

    def _dfs(curr_node):
        
        for adjacency_node in graph[curr_node][1]:
            if previous_node[adjacency_node] == None:
                graph[adjacency_node][3] = red
                graph[adjacency_node][2] = white
                edges[edge_id(curr_node, adjacency_node)][1] = white
                graphUI.updateUI()
                graph[adjacency_node][3] = yellow
                previous_node[adjacency_node] = curr_node
                if adjacency_node == goal:
                    return True
                elif _dfs(adjacency_node):
                    return True
        graph[curr_node][3] = blue
        graphUI.updateUI()
                    # for discovered_node in previous_node:
                    #     if previous_node[discovered_node] != None:
                    #         graph[discovered_node][3] = blue
                    # graphUI.updateUI()
                    # return True
        return False
                
    if _dfs(start):
        
        temp_node = goal
        result_path = []
        while temp_node != start:
            result_path.append(int(temp_node))
            temp_node = previous_node[temp_node]
        result_path.append(start)
        for i in range (0, len(result_path) - 1):
            edges[edge_id(result_path[i], result_path[i+1])][1] = green

        graph[start][3] = orange
        graph[goal][3] = purple
        graphUI.updateUI()
    else:
        print("Khong co duong di tu Node", start, "den", goal)

    print("Implement DFS algorithm.")
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    graph[1][3] = orange
    graph[0][3] = yellow
    graphUI.updateUI()
    time.sleep(2)
    graph[6][3] = purple
    graph[10][3] = purple
    graphUI.updateUI()
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()
    time.sleep(2)

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
