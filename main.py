import argparse
from commands import InitCommand, EstimateCommand, IndexCommand, UserCommand, QueryCommand
from config import Config

def main():
    # Initialize config
    config = Config()

    # Initialize parser
    parser = argparse.ArgumentParser(description='A GitHub code summarizer.')

    # Adding commands
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func=InitCommand(config))

    estimate_parser = subparsers.add_parser('estimate')
    estimate_parser.set_defaults(func=EstimateCommand(config))

    index_parser = subparsers.add_parser('index')
    index_parser.set_defaults(func=IndexCommand(config))

    user_parser = subparsers.add_parser('user')
    user_parser.set_defaults(func=UserCommand(config))

    query_parser = subparsers.add_parser('query')
    query_parser.set_defaults(func=QueryCommand(config))

    # Parsing arguments
    args = parser.parse_args()
    
    # Call appropriate function based on argument
    args.func()

if __name__ == "__main__":
    main()
