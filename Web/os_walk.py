import os

for dirPath, dirNames, fileNames in os.walk("."):
    print dirPath
    print dirNames
    print fileNames
    for f in fileNames:
        print os.path.join(dirPath, f)


