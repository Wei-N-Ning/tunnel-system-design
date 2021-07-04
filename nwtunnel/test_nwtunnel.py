from nwtunnel.max_flow import MaxFlowCalculator, NoPathException
import unittest

import collections

edges = [
  ["S", "A", 4],
  ["S", "B", 8],
  ["A", "C", 6],
  ["C", "D", 3],
  ["C", "T", 11],
  ["D", "T", 2],
  ["B", "A", 3],
  ["B", "C", 6],
  ["B", "D", 2]
]

class TestEdmondsKarp(unittest.TestCase):
    def setUp(self):
        self.f = MaxFlowCalculator()

    def test_create_graph_from_edges(self):
        graph = collections.defaultdict(
                    list,
                    {
                        'S': [['A', 4], ['B', 8]],
                        'A': [['C', 6]],
                        'C': [['D', 3], ['T', 11]],
                        'D': [['T', 2]],
                        'B': [['A', 3], ['C', 6], ['D', 2]],
                    })
        g = MaxFlowCalculator.create_graph(edges)
        self.assertEqual(g, graph)

    def test_happy_path_deterministic_throughput(self):
        throughput = self.f(edges, 'S', 'T')
        self.assertEqual(throughput, 12)

    def test_no_path(self):
        self.assertRaises(NoPathException, self.f, edges, 'A', 'S')

    def test_correct_dfs_no_double_visiting(self):
        throughput = self.f(edges, 'A', 'D')
        self.assertEqual(throughput, 3)


if __name__ == '__main__':
    unittest.main()
