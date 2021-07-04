import collections
import copy


class NoPathException(Exception):
    def __init__(self, fr, to_):
        super().__init__(f'there is no path from {fr} to {to_}')


class MaxFlowCalculator:
    """Given a schema-compliant graph object, a "source" and 
    a "sink", it calculates the maximum flow using the Edmonds-Karp
    algorithm. 
    """

    graph_schema = collections.defaultdict(
        list,
        {
            # graph is expected to be a defaultdict with the
            # value-factory function being `list` (the builtin list ctor).

            # each k-v pair is:
            # <from_node: list of (to_node, edge_flow)>

            # example:
            'S': [('A', 4), ('B', 8)],
        })

    @staticmethod
    def _create_residual_graph(graph):
        """For each edge (A, B, edge_flow), add a back edge (B, A, 0)
        """
        residual_graph = copy.deepcopy(graph)
        for fr in list(residual_graph.keys()):
            for to_node, _ in graph[fr]:
                residual_graph[to_node].append((fr, 0))
        return residual_graph

    @staticmethod
    def _extract_path(graph, src, sink):
        """Extract one path that has no zero-flow edge.
        Each path is a list of (from_node, to_node, edge_flow).
        If it is impossible to find a path from src to sink, return None to signal termination 
        or exception.
        """
        def iterate_dfs(node):
            Q = collections.deque([([], src)])  # a list of (path, node)
            visited = set()
            while Q:
                path, node = Q.popleft()
                visited.add(node)
                if path:
                    yield path
                for to_node, edge_flow in graph[node]:
                    if edge_flow <= 0:
                        continue
                    if to_node in visited:
                        continue
                    new_path = path + [(node, to_node, edge_flow)]
                    Q.append((new_path, to_node))

        for path in iterate_dfs(src):
            fr, to_, edge_flow = path[-1]
            if to_ == sink:
                return path
        return None

    @staticmethod
    def _min_edge_flow(path):
        return min(edge_flow for _, _, edge_flow in path)

    @staticmethod
    def _update_residual_graph(residual_graph, fr, to_, delta):
        edges = []
        for (to_node, edge_flow) in residual_graph[fr]:
            if to_ == to_node:
                edge_flow += delta
            edges.append((to_node, edge_flow))
        residual_graph[fr] = edges

    def __call__(self, graph, src, sink):
        """Return the maximum flow from src to sink.

        Raise NoPathException if it is impossible to travel from src to sink.
        """
        # is there a path from src sink at all
        if not self._extract_path(graph, src, sink):
            raise NoPathException(src, sink)
        residual_graph = self._create_residual_graph(graph)
        result = 0
        while True:
            path = self._extract_path(residual_graph, src, sink)
            if not path:
                break
            min_flow = self._min_edge_flow(path)
            result += min_flow
            for (fr, to_, edge_flow) in path:
                self._update_residual_graph(residual_graph, fr, to_, -min_flow)
                self._update_residual_graph(residual_graph, to_, fr, min_flow)
        return result
