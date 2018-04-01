import sys
import argparse

__author__='Suraj'


def parse_arguments():
    # parse arguments
    parser = argparse.ArgumentParser(\
             description = 'Set up VM with Access Controls',\
                   usage = 'python arg_parse.py -h htadmin')

    parser.add_argument('-H', '--htadmin', help='HTAdmin for Access\
            Controls', required=True)
    args = parser.parse_args(sys.argv[1:])

    return args.htadmin

if __name__ == '__main__':
    print parse_arguments()
