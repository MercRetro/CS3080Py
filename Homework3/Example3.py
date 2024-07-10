#Mercury Goodwin

#Open file
readFile=open("Auto.csv","r")
writeFile=open("copy_Content.txt","w")

#Print and write to new file
for line in readFile:
  print(line)
  writeFile.write(line)

#Close files
readFile.close()
writeFile.close()