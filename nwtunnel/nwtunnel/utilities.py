from nwtunnel.max_flow import MaxFlowCalculator, NoPathException

import collections
import itertools
import random
import string
import time


def create_nodes(num_nodes):
    if num_nodes <= 10:
        return string.ascii_uppercase[:num_nodes]
    elif num_nodes > 10 and num_nodes <= 100:
        return string.printable[:num_nodes]
    elif num_nodes > 100 and num_nodes <= 1000:
        return list(''.join(p)
                    for p in itertools.permutations('ABCDEFG'))[:num_nodes]
    elif num_nodes > 1000 and num_nodes <= 100000:
        return list(''.join(p)
                    for p in itertools.permutations('ABCDEFGHI'))[:num_nodes]
    raise ValueError(f'can not create more than 100000 nodes!')


def create_graph(nodes, num_edges, flow_f=lambda a, b: random.randint(1, 100)):
    """Create a mock graph for performance testing.

    nodes: a list of hashable objects

    num_edges: how many edges can each vertex have

    flow_f: a function that takes two nodes and returns their edge flow;
        by default the flow is a random number between 1 and 100
    """
    graph = collections.defaultdict(list, dict())
    for fr in nodes:
        for to_ in (n for n in random.sample(nodes, num_edges) if n != fr):
            graph[fr].append((to_, flow_f(fr, to_)))
    return graph


def perf_n_nodes_m_edges(n, m):
    """Create a dense graph with n nodes, m edges/node and random
    edge flow (between 1 and 100).

    Return the time taken to complete the max-flow computation.
    """

    nodes = create_nodes(n)
    src = nodes[0]
    sink = nodes[-1]
    g = create_graph(nodes, num_edges=m)
    f = MaxFlowCalculator()
    start = time.perf_counter()
    try:
        f(g, src, sink)
    except NoPathException:
        pass
    return time.perf_counter() - start