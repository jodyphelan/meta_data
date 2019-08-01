import metadata
import sys
import argparse

def main(args):
	tbl = metadata.csv_table(args.csv)
	tbl.table(args.col1,args.col2,sep=args.sep,output=args.out)

parser = argparse.ArgumentParser(description='TBProfiler pipeline',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('csv')
parser.add_argument('col1')
parser.add_argument('col2')
parser.add_argument('--sep',type=str,default="\t")
parser.add_argument('--out',type=str)
parser.set_defaults(func=main)

args = parser.parse_args()
args.func(args)
