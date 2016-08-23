#Gets metadata from PDF files. Modified from the one in Violent Python so that it takes directories as input as well.

import pyPdf
import optparse
import os
from pyPdf import PdfFileReader
def printMeta(fileName):
	try:
		pdfFile	=	PdfFileReader(file(fileName, 'rb'))
		docInfo	=	pdfFile.getDocumentInfo()
		print '[*] PDF MetaData For: ' + str(fileName)
		for metaItem in docInfo:
			print '[+] ' + metaItem + ':' + docInfo[metaItem]
		print '\n\n\n\n\n'
	except Exception, e:
		print "[!] Error reading file ===================>	" + fileName
		#print e
		print '\n\n\n\n\n\n'
		
def main():
	parser = optparse.OptionParser('usage %prog -F <PDF file name')
	parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')
	parser.add_option('-d', dest='directory', type='string', help='specify the directory')
	(options, args) = parser.parse_args()
	if (options.fileName == None and options.directory == None) or (options.fileName != None and options.directory != None):
		print parser.usage
		exit(0)
	else:
		if options.fileName != None:
			fileName = options.fileName
			printMeta(fileName)
			exit(0)
		elif options.directory != None:
			directory = options.directory
			files = os.listdir(directory)	
			for file in files:
				if file.endswith('.pdf'):
					printMeta(directory + '\\' + file)
			exit(0)
	
	
	
if __name__ == '__main__':
	main()
