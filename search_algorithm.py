import pygame
import graphUI
import time
import math
from queue import PriorityQueue     # Dùng thêm PriorityQueue từ thư viện queue
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
    # Set màu cho node Start và Goal

    # if edge_id(0,2) == edge_id(2,0):
    #     print("That true bro!")


    list_path = [[start]] # list_path là mảng lưu lại đường đi từ node Start đến các node (chứa các new_path)

    while graph[goal][2] != white:      # Lặp đến khi tìm thấy node Goal
        path = list_path.pop(0)     # Lần lượt pop từng path ra để duyệt
        temp_node = path[-1]        # Node chưa được duyệt đến
        if graph[temp_node][3] != blue:     # Nếu node có màu blue = node đã đc duyệt
            graph[temp_node][3] = yellow
            graph[temp_node][2] = white
            graphUI.updateUI()
            # Set màu cho node đang duyệt

            restructed_node = list(graph[temp_node][1])
            for adjacency_node in graph[temp_node][1]:
                if graph[adjacency_node][3] != black and adjacency_node != goal:
                    restructed_node.remove(adjacency_node)
            # Chỉ duyệt những node chưa tìm thấy (để loại đi trường hợp có cùng node con)

            for adjacency_node in restructed_node:
                graph[adjacency_node][3] = red
                graph[adjacency_node][2] = white
                edges[edge_id(temp_node, adjacency_node)][1] = white
                graphUI.updateUI()
                # Set màu cho node và cạnh đc tìm thấy

                new_path = list(path)
                new_path.append(adjacency_node)
                list_path.append(new_path)
                # Lưu lại đường đi đến node tìm thấy vào new_path, sau đó thêm vào list_path

                if adjacency_node == goal:      # Nếu tìm thấy Goal thì return path và thoát vòng while
                    result_path = new_path
                    break          
            graph[temp_node][3] = blue
            graphUI.updateUI()
            # Set màu xanh để đánh dấu là đã duyệt qua node

    # print(result_path)
    for i in range (0, len(result_path) - 1):
        edges[edge_id(result_path[i], result_path[i+1])][1] = green
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # Update màu cho kết quả
        
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
    # Set màu cho node Start và Goal

    previous_node = {}      # previous_node dùng để lưu lại node cha của từng node
    previous_node.update({start: -1})       # Node gốc ko có node cha

    def _dfs(curr_node):
        
        for adjacency_node in graph[curr_node][1]:
            if adjacency_node not in previous_node:       # Kiểm tra xem có phải node lá ko, nếu là lá thì ko duyệt
                graph[adjacency_node][3] = red
                graph[adjacency_node][2] = white
                edges[edge_id(curr_node, adjacency_node)][1] = white
                graphUI.updateUI()
                # Set màu cho các node đã tìm thấy

                graph[adjacency_node][3] = yellow
                graphUI.updateUI()
                # Set màu cho node(path) đang đc duyệt

                previous_node.update({adjacency_node:curr_node})
                if adjacency_node == goal:      # Nếu tìm thấy Goal thì dừng, còn không thì tiếp tục duyệt node con của nó
                    return True
                elif _dfs(adjacency_node):      # (tiếp tục duyệt node con)
                    return True
        graph[curr_node][3] = blue
        graphUI.updateUI()
        # Set màu blue để đánh dấu đã duyệt qua node

        return False
                
    if _dfs(start):
        
        temp_node = goal
        result_path = []
        while temp_node != start:
            result_path.append(int(temp_node))
            temp_node = previous_node[temp_node]
        result_path.append(start)
        # Dựa previous_node để đưa ra path khi đi ngược từ Goal

        for i in range (0, len(result_path) - 1):
            edges[edge_id(result_path[i], result_path[i+1])][1] = green
        graph[start][3] = orange
        graph[goal][3] = purple
        graphUI.updateUI()
        # Update màu cho kết quả

    print("Implement DFS algorithm.")
    pass


def distance(graph, node_1, node_2):        # Trọng số của cạnh (chi phí đường đi) = khoảng cách giữa các node trên mặt phẳng tọa độ
    x_1, y_1 = graph[node_1][0]
    x_2, y_2 = graph[node_2][0]
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # Set màu cho node Start và Goal

    visited_node = []       # Lưu các node đã duyệt qua
    ucs_node = {start:[start, 0]}       # Lưu lại node 'x', node cha của 'x', chi phí đi từ Start đến 'x'
    ucs_node_temp = PriorityQueue()
    ucs_node_temp.put((0, start))
    # ucs_node_temp là queue dùng để lưu lại các node và chi phí để đi đến node đó từ Start, sau đó quêu sẽ tự động sort lại theo thứ tự tăng dần về chi phí đường đi

    while 1: 
        temp = ucs_node_temp.get()
        print(ucs_node)
        print(temp)       
        curr_node = temp[1]
        if curr_node == goal:
            break
        graph[curr_node][2] = white
        graph[curr_node][3] = yellow
        graphUI.updateUI()
        for adjacency_node in graph[curr_node][1]:
            if adjacency_node not in visited_node:
                edges[edge_id(curr_node, adjacency_node)][1] = white
                graph[adjacency_node][3] = red
                graphUI.updateUI()

                # Nếu node chưa có trong ucs_node thì thêm vào hoặc nếu tìm đc đường đi ngắn hơn đến node đó thì update lại đường đi
                if (adjacency_node not in ucs_node) or (ucs_node[adjacency_node][1] > ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node)):
                    ucs_node.update({adjacency_node: [curr_node, ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node)]})
                    ucs_node_temp.put((ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node), adjacency_node))
                  
        visited_node.append(curr_node)
        graph[curr_node][3] = blue
        graphUI.updateUI()
        # Set màu blue cho node đã được duyệt

    result_path = [goal]
    temp = goal
    while temp != start:
            for node_temp in ucs_node:
                if node_temp == temp:
                    temp = ucs_node[node_temp][0]
                    result_path.append(temp)
                    # Tìm path từ Goal dựa vào dict ucs_node

    for i in range (0, len(result_path) - 1):
        edges[edge_id(result_path[i], result_path[i+1])][1] = green
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # Update màu cho kết quả


    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):      # Gần giống như ucs, chỉ là thêm hàm heristic
    """
    A star search
    """
    # TODO: your code
    graph[start][2] = white
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # Set màu cho node Start và Goal

    visited_node = []
    ucs_node = {start:[start, 0]}
    ucs_node_temp = PriorityQueue()
    ucs_node_temp.put((0, start))
    while 1:
        # Hàm heuristic h(n) = khoảng cách trực tiếp (euclide) từ node đang xét đến node goal trên mặt phẳng tọa độ
        # -> f(n) = g(n) + h(n) = tổng đường đi từ start đến node (n) + khoảng cách trực tiếp (euclide) từ node đang xét đến node goal trên mặt phẳng tọa độ
        temp = ucs_node_temp.get()
        print(ucs_node)
        print(temp)       
        curr_node = temp[1]
        if curr_node == goal:
            break
        graph[curr_node][2] = white
        graph[curr_node][3] = yellow
        graphUI.updateUI()
        for adjacency_node in graph[curr_node][1]:
            if adjacency_node not in visited_node:
                edges[edge_id(curr_node, adjacency_node)][1] = white
                graph[adjacency_node][3] = red
                graphUI.updateUI()
                if (adjacency_node not in ucs_node) or (ucs_node[adjacency_node][1] > ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node)):
                    # g(n) = distance(graph, adjacency_node, goal)
                    ucs_node.update({adjacency_node: [curr_node, ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node) + distance(graph, adjacency_node, goal)]})
                    ucs_node_temp.put((ucs_node[curr_node][1] + distance(graph, curr_node, adjacency_node) + distance(graph, adjacency_node, goal), adjacency_node))
                  
        visited_node.append(curr_node)
        graph[curr_node][3] = blue
        graphUI.updateUI()
    
    result_path = [goal]
    temp = goal
    while temp != start:
            for node_temp in ucs_node:
                if node_temp == temp:
                    temp = ucs_node[node_temp][0]
                    result_path.append(temp)
    for i in range (0, len(result_path) - 1):
        edges[edge_id(result_path[i], result_path[i+1])][1] = green

    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()
    # Update màu cho kết quả

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
