import argparse
import sys

APP_DESC="""
This tool could help you to get the information about different blockchains.
"""
print(APP_DESC)
if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()
parser.add_argument('-b','--blockchain',default=0,help="Input the name of blockchain you want to explore.eg: Bitcoin")
parser.add_argument('-v','--verbose', default=0,help="print more debuging information")
parser.add_argument('-t','--transaction',help="Input the transaction hash of the transaction you want to know.")
parser.add_argument('-i','--id',default=0,help="Input the block id of the block you want to know")
args = parser.parse_args()
