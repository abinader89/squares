import argparse

parser = argparse.ArgumentParser(description="This calculates everyones position on the 10*10 grid.")

parser.add_argument("add", nargs='*', metavar="num", type=int, help="enter the owner name and the number of squares owned.")

args = parser.parse_args()

if len(args.add) != 0:
    print(sum(args.add))
