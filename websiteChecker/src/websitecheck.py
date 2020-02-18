import os, sys
import argparse

from websitechecker import Websitechecker

def add_args(parser):

	parser.add_argument('-web', '--webaddress',
                        required=True,
                        action='store',
                        help="Web address that needs to be looked up")

  

def process(args):
        
    # import pdb;pdb.set_trace()
   
    webobj = Websitechecker()

    response = webobj.url_ok(webaddress=args.webaddress)

    if response:
    	return 'Website is reachable'
    else:
    	return 'Website is not reachable'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments for Webaddress lookup")
    add_args(parser)
    
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    print(process(args))



