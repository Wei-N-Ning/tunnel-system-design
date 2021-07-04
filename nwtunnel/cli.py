import json
import sys
import collections
import argparse
from nwtunnel.max_flow import NoPathException, MaxFlowCalculator


def parse_arg(args):
    p = argparse.ArgumentParser('max flow calculator')
    p.add_argument(
        '-g', 
        '--graph-file', 
        help='a json file describing the tunnel system as a list of edges',
        required=True
    )
    p.add_argument('start')
    p.add_argument('end')
    return p.parse_args(args)


if __name__ == '__main__':
    args = parse_arg(sys.argv[1:])
    f = MaxFlowCalculator()
    try:
        with open(args.graph_file, 'r') as fp:
            edges = json.load(fp)
    except Exception as e:
        print(str(e))
        sys.exit(1)
    try:
        o = f(edges, args.start, args.end)
        print('the maximum capacity between {} and {} is {}'.format(
            args.start, args.end, o))
    except NoPathException as e:
        print(str(e))
        sys.exit(1)
