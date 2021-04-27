import os, time, shutil
from threading import Thread

PATH = "D:/Downloads" #TargetFolder
DOWNLOADS_PATH = "C:/Users/<User>/Downloads" #Source Folder

fileList = os.listdir(DOWNLOADS_PATH)

fileDict = {
    "Excel"         : list(),
    "Word"          : list(),
    "PPT"           : list(),
    "PDF"           : list(),
    "ZIP"           : list(),
    "HTML"          : list(),
    "Videos"        : list(),
    "Images"        : list(),
    "Scripts"       : list(),
    "Text"          : list(),
    "Executables"   : list(),
    "XML"           : list(),
    "Other"         : list()
}

switcher = {
    ""              : "Other",
    "ini"           : "Other",
    "properties"    : "Other",
    "ics"           : "Other",
    "site"          : "Other",
    "tgz"           : "Other",
    "1-win32"       : "Other",
    "rdp"           : "Other",
    "dotx"          : "Other",
    "ALL"           : "Other",
    "key"           : "Scripts",
    "pem"           : "Scripts",    
    "crt"           : "Scripts",
    "key"           : "Scripts",
    "cls"           : "Scripts",
    "profile"       : "Scripts",
    "css"           : "Scripts",
    "js"            : "Scripts",
    "log"           : "Scripts",
    "json"          : "Text",
    "xml"           : "XML",
    "zip"           : "ZIP",
    "bat"           : "Executables",
    "exe"           : "Executables",
    "docx"          : "Word",
    "doc"           : "Word",
    "webm"          : "Videos",
    "jpg"           : "Images",
    "PNG"           : "Images",
    "png"           : "Images",
    "html"          : "HTML",
    "csv"           : "Excel",
    "xls"           : "Excel",
    "xlsx"          : "Excel",
    "pptx"          : "PPT",
    "txt"           : "Text",
    "pdf"           : "PDF"
}

monthMap = {
    1 : "JAN",
    2 : "FEB",
    3 : "MAR",
    4 : "APR", 
    5 : "MAY",
    6 : "JUN",
    7 : "JUL",
    8 : "AUG",
    9 : "SEP",
    10: "OCT",
    11: "NOV",
    12: "DEC"
}

def processFile(pathList):    
    for path in pathList:
        try:            
            date = time.localtime( os.path.getmtime( path["sourcePath"] ) )
            stringFormat = monthMap.get(date.tm_mon) + '-' + str(date.tm_year)
            targetPath = path["targetPath"] + '/' + stringFormat
            
            if os.path.exists( targetPath ):
                shutil.move( path["sourcePath"], targetPath )
            else:
                os.makedirs(targetPath)
                shutil.move( path["sourcePath"], targetPath )
        except Exception as error:
            print('Exception ' )
            print( error)
    print('Done processing.')


for file in fileList:
    fileName, fileExtension = os.path.splitext(file)

    try:
        fileExtension = fileExtension[1:]
        if fileExtension == '':
            continue

        sourcePath = DOWNLOADS_PATH + '/' + file
        folderType = switcher.get(fileExtension)
        targetPath = PATH + '/' + folderType

        tmp = {
            "sourcePath" : sourcePath,
            "targetPath" : targetPath,
        }

        currentList = fileDict[folderType]        
        currentList.append(tmp)
        fileDict[folderType]  = currentList

        if os.path.exists( targetPath ):
            continue            
        else:
            os.makedirs(targetPath)

    except Exception as inst:
        print('Error for :' + file)
        #print(type(inst))
        #print(inst.args)
        #print(inst)

for fileType in fileDict:    
    thread = Thread(target=processFile, args=(fileDict[fileType],) )
    thread.start()
