import sys
import csv
from collections import Counter,defaultdict
class csv_table:
	def __init__(self,filename):
		self.data = {}
		self.columns = []
		self.samples = []
		self.column_values = defaultdict(set)
		for row in csv.DictReader(open(filename)):
			if "id" not in row:
				sys.stderr.write("No columns named 'id' found... Exiting!")
				quit()
			self.data[row["id"]] = row
			for col in row:
				self.column_values[col].add(row[col])
			self.columns = list(row.keys())
			self.samples.append(row["id"])
		for col in self.column_values:
			self.column_values[col] = sorted(list(self.column_values[col]))
	def summary(self,column,output=None,sep="\t",percentage=False,samples_file=None):
		if type(samples_file)!=str:
			samples = [x.rstrip() for x in samples_file]
		else:
			samples = [x.rstrip() for x in open(samples_file)]
		counts = Counter([self.data[s][column] for s in samples])
		O = open(output,"w") if output else sys.stdout
		for key,val in counts.most_common():
			if percentage:
				O.write("%s%s%s%s%.1f\n" % (key,sep,val,sep,val/len(samples)*100))
			else:
				O.write("%s%s%s\n" % (key,sep,val))
		O.close()
	def extract_columns(self, columns, output = None, sep = "\t", samples_file = None):
		samples = [x.rstrip() for x in open(samples_file)] if samples_file else self.samples
		for col in columns:
			if col not in self.columns:
				sys.stderr.write("No columns named '%s' found... Exiting!" % col)
				quit()
		O = open(output,"w") if output else sys.stdout
		O.write("%s\n" % (sep.join(columns)))
		for s in samples:
			O.write("%s\n" % (sep.join([self.data[s][c] for c in columns])))
		O.close()
	def table(self,colx,coly,output = None,sep="\t"):
		values = []
		xcounts = defaultdict(int)
		ycounts = defaultdict(int)
		for row in self.data.values():
			values.append((row[coly],row[colx]))
			xcounts[row[coly]]+=1
			ycounts[row[colx]]+=1
		counts = Counter(values)
		O = open(output,"w") if output else sys.stdout
		O.write("%s%stotal%s%s\n" % (coly,sep,sep,sep.join(self.column_values[colx])))
		for valy in self.column_values[coly]:
			tmp = [str(counts[(valy,valx)]) for valx in self.column_values[colx]]
			O.write("%s%s%s%s%s\n" % (valy,sep,xcounts[valy],sep,sep.join(tmp)))
		tmp = [str(ycounts[valx]) for valx in self.column_values[colx]]
		O.write("total%s%s%s%s\n" % (sep,len(values),sep,sep.join(tmp)))
		O.close()
