#Mercury Goodwin
import os

#Open file
readFileName = "Auto.csv"
readFile=open(readFileName,"r")
print(readFile.read())  

#Create a directory called "To Process"
pathProcess = "To Process/"
os.mkdir(pathProcess)
#Move to that directory
os.chdir(pathProcess)

#Create another directory called "Work Copy"
pathWork = 'Work Copy/'
os.mkdir(pathWork)
#Take the .csv data, write it to a file called "copy_Content.txt" 
#Save it to the Work Copy directory
nameFile = "copy_Content"
completeName = os.path.join(pathWork, nameFile+".txt")         

writeFile = open(completeName, "w")

for line in readFile:
  writeFile.write(line)

#Close files
readFile.close()
writeFile.close()