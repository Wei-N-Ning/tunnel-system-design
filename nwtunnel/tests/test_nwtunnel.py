from nwtunnel.max_flow import MaxFlowCalculator, NoPathException
import unittest

import collections

graph = collections.defaultdict(
    list,
    {
        # <from_node: list of (to_node, weight)>
        'S': [('A', 4), ('B', 8)],
        'A': [('C', 6)],
        'C': [('D', 3), ('T', 11)],
        'D': [('T', 2)],
        'B': [('A', 3), ('C', 6), ('D', 2)],
    })


class TestEdmondsKarp(unittest.TestCase):
    def setUp(self) -> None:
        self.f = MaxFlowCalculator()

    def test_happy_path_deterministic_throughput(self):
        throughput = self.f(graph, 'S', 'T')
        self.assertEqual(throughput, 12)

    def test_no_path(self):
        self.assertRaises(NoPathException, self.f, graph, 'A', 'S')

    def test_correct_dfs_no_double_visiting(self):
        throughput = self.f(graph, 'A', 'D')
        self.assertEqual(throughput, 3)


if __name__ == '__main__':
    unittest.main()
