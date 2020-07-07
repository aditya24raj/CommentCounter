import re
import filePicker


"""
fileExtensionAndComments={
"languageExtension":
"single line comment character",
"mulitple line comment begin character",
"multiple line comment end character"
}
"""

#add extension and comment character of
#respective language for counting their 
#comments

fileExtensionAndComments={
"py":("#",("'''",'"""'),("'''",'"""'))
}


#add filenames in files to count their comments
files=filePicker.SelectedFiles()


def Counter(filename):
	
	try:
		fileExtension=re.findall("^.*\.([a-z,A-Z]+)$",filename)[0]
		
		singleLineCommentChar=fileExtensionAndComments[fileExtension][0]
		multiLineCommentCharStart=fileExtensionAndComments[fileExtension][1]
		multiLineCommentCharEnd=fileExtensionAndComments[fileExtension][2]
		
	except KeyError:
		return(print("Sorry, Unsupported FileType!"))
	except IndexError:
		return(print("Sorry, Unable To detect File Extension!"))
	
	counts={
	"file":filename,
	"Total Lines":0,
	"Lines of Code":0,
	"Commented Lines":0,
	"Blank Lines":0
	}
	
	try:
		multiLineComments=False
		
		with open(filename,"r") as sourceFile:
			for line in sourceFile:
				counts["Total Lines"]+=1
				
				if line.startswith(multiLineCommentCharStart):
					multiLineComments=not multiLineComments
					counts["Commented Lines"]+=1
					continue
					
					
				if multiLineComments:
					counts["Commented Lines"]+=1
					
					if line.endswith(multiLineCommentCharEnd):
						multiLineComments=False
				
				elif line.startswith(singleLineCommentChar):
					counts["Commented Lines"]+=1
				
				elif line.strip()=="":
					counts["Blank Lines"]+=1
		
		counts["Lines of Code"]=counts["Total Lines"]-(counts["Commented Lines"]+counts["Blank Lines"])
		
		for k,v in counts.items():
					print(k+":",v)
					
		
	except FileNotFoundError:
		return(print("Sorry, File Not Found!"))






for filename in files:
	Counter(filename)
	print("\n")













