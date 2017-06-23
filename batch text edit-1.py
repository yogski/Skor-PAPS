#################################################
# CREATED BY: YOGI SAPUTRO						#
# This program corrects the format of CSV 		#
# created by PDF tabular to CSV.py to standard	#
# CSV in batch mode								#
#################################################

#dependencies
import re
import fileinput
import sys

#internal functions
def fileBatch(txt):
	fileList = []
	with open(txt, "r") as ins:
		for line in ins:
			fileList.append(line.strip('\n'))
	return fileList

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

#setup & program
batch = input('Please input text file containing paths of file to be edited')
batchList = fileBatch(batch)

for i in range(len(batchList)):
	f_in = open(batchList[i],"r")
	f_out = open("Skor PAPS"+str(i+1)+"rev.csv","w")
	#print(f_in.read()) #testing whether file content is actually readable
	
	for line in f_in:
	    regex = re.compile(r"[0-9]{1,3},[0-9]{9},\w{2}-\w{2}-\w{4},\w{3},\w{3},\w{3},\w{3}")
	    matched = regex.findall(f_in.read())
	    for i in range(len(matched)):
	    	f_out.write(matched[i])
	    	f_out.write('\n')
	f_in.close()
	f_out.close()
