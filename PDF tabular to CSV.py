#################################################
# CREATED BY: YOGI SAPUTRO						#
# This program reads tabular data in PDF file	#
# and convert them into a csv file, and then	#
# format it accordingly							#
#################################################

#dependencies
import PyPDF2

#internal functions
def file_input():
	return input('Please input the file name: \n')

#setup & program
print ("PDF input needed.")
inputFile = file_input()
print ("CSV output needed.")
outputFile = file_input()
pdfFileObj = open(inputFile,'rb')
readPDF = PyPDF2.PdfFileReader(pdfFileObj)

csvFileObj = open(outputFile,'w')
for i in range(readPDF.numPages):
	pageObj = readPDF.getPage(i)
	csvFileObj.write(pageObj.extractText())

pdfFileObj.close()