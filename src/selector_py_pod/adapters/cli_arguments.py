import argparse

parser = argparse.ArgumentParser(description='SelectorPyPod.')
parser.add_argument('--env', type=str, default='.env', help='env file')
parser.add_argument('--show_id', type=str, required=True)
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--description', type=str, default='')
parser.add_argument('--outputs', type=str, action='append')
parser.add_argument('--episodes_amount', type=int, default=5)

args = parser.parse_args()
