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
        print(f'{num_nodes} nodes'.ljust(14), f'{num_edges} edges/n'.ljust(14),
              f'time: {duration:0.5f} seconds')


if __name__ == '__main__':
    run_tests()
