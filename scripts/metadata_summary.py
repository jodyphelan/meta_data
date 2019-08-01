import metadata
import sys
import argparse

def main(args):
	tbl = metadata.csv_table(args.csv)
	if args.samples=="-": args.samples = sys.stdin
	tbl.summary(args.col,sep=args.sep,output=args.out,percentage=args.pct,samples_file=args.samples)

parser = argparse.ArgumentParser(description='TBProfiler pipeline',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('csv')
parser.add_argument('col')
parser.add_argument('--sep',type=str,default="\t")
parser.add_argument('--out',type=str)
parser.add_argument('--pct',action="store_true")
parser.add_argument('--samples',type=str)
parser.set_defaults(func=main)

args = parser.parse_args()
args.func(args)
