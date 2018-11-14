import argparse


def get_parameters() :
    #create the top-level parser
    parser = argparse.ArgumentParser(prog='PROG') 
    subparsers = parser.add_subparsers(help='prog help')

    # "cpu" command parser
    cpu_parser = subparsers.add_parser('cpu', help='cpu help')
    cpu_subparsers = cpu_parser.add_subparsers(help='check help')
    cpu_parser.set_defaults(which='cpu')

    # "cpu load" command parser
    check_cpu_parser = cpu_subparsers.add_parser('load', help='check help')
    check_cpu_parser.add_argument('--entries',type = int, required = True, default = 10)
    check_cpu_parser.set_defaults(which='load')

    # "cpu model" command parser
    model_cpu_parser = cpu_subparsers.add_parser('model', help='check help')
    model_cpu_parser.set_defaults(which='model')

    # "memory" command parser
    mem_parser = subparsers.add_parser('memory', help='cpu help')
    mem_subparsers = mem_parser.add_subparsers(help='check help')
    mem_parser.set_defaults(which='memory')

    # "memory stats" command parser
    mem_stats_parser = mem_subparsers.add_parser('stats', help='check help')
    mem_stats_parser.set_defaults(which='stats')

    return parser.parse_args()
