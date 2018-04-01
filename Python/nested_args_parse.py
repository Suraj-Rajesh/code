import sys
from argparse import ArgumentParser

__author__='Suraj'

def parse_arguments():
    commands = ['setup', 'enable']
    parser = ArgumentParser(\
                 description = 'Setup and enable disks for root restriction',\
                 usage = '''nested_args_parse.py <command> [args]

          setup     Sets up VM with required policies for root restriction
          enable    Enables root restriction for user''')
    parser.add_argument('command', help = 'Subcommand to run')
        
    args = parser.parse_args(sys.argv[1:2])
    
    if not args.command in commands:
	print 'Unrecognized command'
	parser.print_help()
        exit(1)
    else:
    	return args.command

def parse_enable_arguments():
    # parse sub-arguments
    parser = ArgumentParser(\
             description = 'Sets up VM with required policies for root restriction',\
                   usage = 'ht_restrict.py enable -u user -d device_mapper -m mount_directory')

    parser.add_argument('-u', '--user', help = 'user who requested root restrict', required = True)
    parser.add_argument('-d', '--device', help = 'clear device mapper that needs root restriction', required = True)
    parser.add_argument('-m', '--mount', help = 'directory to mount to', required = True)
    args = parser.parse_args(sys.argv[2:])

    return (args.user, args.device, args.mount)

class Utility(object):

    def __init__(self):
	pass

    def setup(self):
        print 'Do the setup here'

    def enable(self):
	(user, device, mount) = parse_enable_arguments()

	print user
	print device
	print mount

	# sub arguments parsed successfully, continue
	pass

if __name__ == '__main__':
    util = Utility()
    cmd = parse_arguments()

    if 'enable' == cmd:
	util.enable()
    if 'setup' == cmd:
	util.setup()
