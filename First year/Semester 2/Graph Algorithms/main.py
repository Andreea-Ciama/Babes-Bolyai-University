from queue import PriorityQueue
from random import randint

from graph import TripleDictGraph, write_graph_to_file, read_graph_from_file



class UI:
    def __init__(self):
        self._graphs = []
        self._current = None

    def findLowestLengthPathBFS(self, start, end):
        '''
        find the lowest length path between start and end, in graph, using a forward BFS from the starting vertex
        if start or end are not valid vertices in the graph, we raise ValueError
        if there is no path between start and end, we raise ValueError
        :param start: the starting vertex
        :param end: the ending vertex
        :return: returns the path from start to end if it exists, otherwise it raises ValueError
        '''

        # all the visited nodes
        visit = []
        #all the possible paths in a queue
        queue = [[start]]
        if start == end:
            return []  #he path is empty
        while queue:  # while we have paths unchecked
            # we pop the first path
            path = queue.pop(0)
            # the last node in the path
            vertex = path[-1]
            # if the vertex is not visited, for each of its outbound vertex, we create a new path from the
            # previous one by adding the outbound vertex.
            # If the outbound vertex coincides with the end vertex
            # we return the path we just created
            if vertex not in visit:
                outboundVertices = self._graphs[self._current].parse_outbound(vertex)
                for outbound in outboundVertices:
                    newPath = list(path)
                    newPath.append(outbound)
                    queue.append(newPath)
                    if outbound == end:
                        return newPath
                # we add the vertex to the list of visited vertices
                visit.append(vertex)
        # we raise a ValueError if we've visited all vertices that can be visited from start
        #and we couldn't find a path between start and end
        raise ValueError("No path between start and end")

    def get_edge_cost(self, having_start, having_end):
        """
        Returns the cost of a defined edge for a given start and end vertex

        :param having_start: int
        :param having_end: int
        :return: int
        """
        having_start_vertex = self.get_vertex_with_value(having_start)
        having_end_vertex = self.get_vertex_with_value(having_end)

        try:
            return self.store_cost[(having_start_vertex, having_end_vertex)]
        except KeyError:
            raise Exception("The specified edge has no cost")

    def find_lowest_cost_path(self, source, target):
        """
        Returns the shortest path between the given source and target

        :param source: int
        :param target: int
        :return: (list, int)
        """
        queue = PriorityQueue()
        previous = [source]
        queue.put((0, source))
        distance = {source: 0}
        while queue:
            x = queue.get()[1]
            if x == target:
                break
            for y in self._graphs[self._current].out_degree(x):
                if y not in distance.keys() or distance[x] + self.get_edge_cost(x, y) < distance[y]:
                    distance[y] = distance[x] + self.get_edge_cost(x, y)
                    queue.put((distance[y], y))
                    if y in previous:
                        previous.remove(y)
                    previous += [y]
        return previous, distance[target]

    def find_shortest_path_ui(self):
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        try:
            path = self.findLowestLengthPathBFS(start, end)
        except ValueError as ve:
            print(ve)
            return
        if len(path) == 0:
            print('start node is end node!')
        else:
            for vertrex in path[:-1]:
                print(str(vertrex) + '->', end='')
            print(path[-1])
            print('length: ', len(path)-1)

    def add_empty_graph(self):
        if self._current is None:
            self._current = 0
        graph = TripleDictGraph(0, 0)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def create_random_graph_ui(self):
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        graph = self.generate_random(vertices, edges)
        if self._current is None:
            self._current = 0
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def generate_random(self, vertices, edges):
        if edges > vertices * vertices:
            raise ValueError("Too many edges!")
        graph = TripleDictGraph(vertices, 0)
        i = 0
        while i < edges:
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            cost = randint(0, 500)
            if graph.add_edge(x, y, cost):
                i += 1
        return graph

    def read_graph_from_file_ui(self):
        filename = input("Enter the name of the file: ")
        if self._current is None:
            self._current = 0
        graph = read_graph_from_file(filename)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def write_graph_to_file_ui(self):
        current_graph = self._graphs[self._current]
        output_file = "output" + str(self._current) + ".txt"
        write_graph_to_file(current_graph, output_file)

    def switch_graph_ui(self):
        print("You are on the graph number: {}".format(self._current))
        print("Available graphs: 0 - {}".format(str(len(self._graphs) - 1)))
        number = int(input("Enter the graph number you want to switch to: "))
        if not 0 <= number < len(self._graphs):
            raise ValueError("Trying to switch to a non existing graph!")
        self._current = number

    def get_number_of_vertices_ui(self):
        print("The number of vertices is: {}.".format(self._graphs[self._current].number_of_vertices))

    def get_number_of_edges_ui(self):
        print("The number of edges is: {}.".format(self._graphs[self._current].number_of_edges))

    def list_all_outbound(self):
        for x in self._graphs[self._current].parse_vertices():
            line = str(x) + " :"
            for y in self._graphs[self._current].parse_outbound(x):
                line = line + " " + str(y)
            print(line)

    def list_outbound(self):
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        for y in self._graphs[self._current].parse_outbound(vertex):
            line = line + " " + "({}, {})".format(str(vertex), str(y))
        print(line)

    def list_all_inbound(self):
        for x in self._graphs[self._current].parse_vertices():
            line = str(x) + " :"
            for y in self._graphs[self._current].parse_inbound(x):
                line = line + " " + str(y)
            print(line)

    def list_inbound(self):
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        for y in self._graphs[self._current].parse_inbound(vertex):
            line = line + " " + "({}, {})".format(str(y), str(vertex))
        print(line)

    def list_all_costs(self):
        for key in self._graphs[self._current].parse_cost():
            line = "({}, {})".format(key[0], key[1]) + " :" + str(self._graphs[self._current].dictionary_cost[key])
            print(line)

    def parse_all_vertices(self):
        for vertex in self._graphs[self._current].parse_vertices():
            print("{}".format(vertex))

    def add_vertex_ui(self):
        vertex = int(input("Enter the new vertex: "))
        added = self._graphs[self._current].add_vertex(vertex)
        if added:
            print("Vertex added successfully!")
        else:
            print("Cannot add this vertex, it already exists!")

    def delete_vertex_ui(self):
        vertex = int(input("Enter the vertex to be deleted: "))
        deleted = self._graphs[self._current].remove_vertex(vertex)
        if deleted:
            print("Vertex deleted successfully!")
        else:
            print("Cannot delete this vertex, it does not exist!")

    def add_edge_ui(self):
        print("Add an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        added = self._graphs[self._current].add_edge(vertex_x, vertex_y, cost)
        if added:
            print("Edge added successfully!")
        else:
            print("Cannot add this edge, it already exists!")

    def remove_edge_ui(self):
        print("Remove an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        deleted = self._graphs[self._current].remove_edge(vertex_x, vertex_y)
        if deleted:
            print("Edge deleted successfully!")
        else:
            print("Cannot remove this edge, it does not exist!")

    def modify_cost_ui(self):
        print("Modify the cost of an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        mod = self._graphs[self._current].change_cost(vertex_x, vertex_y, cost)
        if mod:
            print("Cost modified successfully!")
        else:
            print("Cannot modify the cost, the edge does not exist!")

    def get_in_degree_ui(self):
        vertex = int(input("Enter the vertex:"))
        degree = self._graphs[self._current].in_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The in degree of the vertex {} is {}.".format(vertex, degree))

    def get_out_degree_ui(self):
        vertex = int(input("Enter the vertex:"))
        degree = self._graphs[self._current].out_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The out degree of the vertex {} is {}.".format(vertex, degree))

    def check_if_edge_ui(self):
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        edge = self._graphs[self._current].find_if_edge(vertex_x, vertex_y)
        if edge is not False:
            print("({}, {}) is an edge and its cost is {}!".format(vertex_x, vertex_y, edge))
        else:
            print("({}, {}) is not an edge!".format(vertex_x, vertex_y))

    def copy_current_graph_ui(self):
        copy = self._graphs[self._current].make_copy()
        self._graphs.append(copy)

    def print_menu(self):
        print("MENU:\n"
              "0. EXIT.\n"
              "1. Create a random graph with specified number of vertices and edges.\n"
              "2. Read the graph from a text file.\n"
              "3. Write the graph in a text file.\n"
              "4. Switch the graph.\n"
              "5. Get the number of vertices.\n"
              "6. Get the number of edges.\n"
              "7. List the outbound edges of a given vertex.\n"
              "8. List all outbound vertices of the graph.\n"
              "9. List the inbound edges of a given vertex.\n"
              "10. List all inbound vertices of the graph. \n"
              "11. List the edges and their costs.\n"
              "12. Add a vertex.\n"
              "13. Remove a vertex.\n"
              "14. Add an edge.\n"
              "15. Remove an edge.\n"
              "16. Modify the cost of an edge.\n"
              "17. Get the in degree of a vertex.\n"
              "18. Get the out degree of a vertex.\n"
              "19. Check if there is an edge between two given vertices.\n"
              "20. Make a copy of the graph.\n"
              "21. Add an empty graph.\n"
              "22. Parse all the vertices.\n"
              "23. lowest length path between two vertices"
              )

    def start(self):
        print("Welcome!")
        done = False
        self.add_empty_graph()
        print("The current graph is an empty graph!")
        command_dict = {"1": self.create_random_graph_ui, "2": self.read_graph_from_file_ui,
                        "3": self.write_graph_to_file_ui, "4": self.switch_graph_ui,
                        "5": self.get_number_of_vertices_ui, "6": self.get_number_of_edges_ui,
                        "7": self.list_outbound, "8": self.list_all_outbound,
                        "9": self.list_inbound, "10": self.list_all_inbound,
                        "11": self.list_all_costs, "12": self.add_vertex_ui,
                        "13": self.delete_vertex_ui, "14": self.add_edge_ui,
                        "15": self.remove_edge_ui, "16": self.modify_cost_ui,
                        "17": self.get_in_degree_ui, "18": self.get_out_degree_ui,
                        "19": self.check_if_edge_ui, "20": self.copy_current_graph_ui,
                        "21": self.add_empty_graph, "22": self.parse_all_vertices,
                        "23": self.find_shortest_path_ui}
        while not done:
            try:
                self.print_menu()
                option = input("Choose an option from the menu: \n")
                if option == "0":
                    done = True
                    print("Bye!")
                elif option in command_dict:
                    command_dict[option]()
                else:
                    print("Bad input!\n")
            except ValueError as ve:
                print(str(ve))
            except FileNotFoundError as fnfe:
                print(str(fnfe).strip("[Errno 2] "))




UI().start()
