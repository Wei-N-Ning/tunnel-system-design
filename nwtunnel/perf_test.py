from nwtunnel.utilities import perf_n_nodes_m_edges


def run_tests():
    for num_nodes, num_edges in [
        (10, 2),
            # 100 nodes, with increasing density
        (100, 20),
        (100, 40),
            # 1000 nodes, with increasing density
        (1000, 20),
        (1000, 40),
            # 10000 nodes
        (10000, 20),
    ]:
        duration = perf_n_nodes_m_edges(num_nodes, num_edges)
        print(
            '{num_nodes} nodes'.format(num_nodes=num_nodes).ljust(14) +\
            '{num_edges} edges/n'.format(num_edges=num_edges).ljust(14) +\
            'time: {duration:0.5f} seconds'.format(duration=duration))


if __name__ == '__main__':
    run_tests()
