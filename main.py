import argparse


def main():
    parser = argparse.ArgumentParser(description="Spawn - A simple Git clone!")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init Command
    init_parser = subparsers.add_parser("init", help="Initialize a new repository")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    print(args)


main()
