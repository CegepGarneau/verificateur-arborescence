import re
import os
import sys
import xml.dom.minidom as minidom


def extractNameAndDa(path):
    """
    Extracts the name and DA from path generated from Omnivox's files
    Ex : 
    Noel-Parise_1944993_TP_1_-_Recherche_Int_Remis_le_2021-09-06_17h51m51s
    Yergeau-Rhéaume_2042114_TP_1_Remis_le_2021-09-09_13h37m17s
    """
    return re.search("(-|[^\W\d])+\_\d{7}", path).group(0)


def validate(test, message):
    """Displays a message if test is false"""
    if (not test):
        print("### " + message)
    return test


def checkFile(dirpath, filename, message="Missing file"):
    """Checks if a file exists and if not, displays an error message"""
    filepath = os.path.join(dirpath, filename)
    return validate(os.path.isfile(filepath), message + " : " + filepath)


def checkDir(path, message="Missing directory"):
    """Checks whether a directory exists and if not, displays an error message"""
    return validate(os.path.isdir(path), message + " : " + path)


def checkDirectoryStructure(parentPath, currentNode):
    """Checks the general directory structure"""
    type = currentNode.nodeName

    if(type == "file"):
        checkFile(parentPath, currentNode.getAttribute("name"))
    elif(type == "dir"):
        currentPath = os.path.join(
            parentPath, currentNode.getAttribute("name"))
        if(checkDir(currentPath)):
            for child in currentNode.childNodes:
                if (child.nodeType == minidom.Node.ELEMENT_NODE):
                    checkDirectoryStructure(currentPath, child)


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        sys.stderr.write("Config file and base directory missing")
        exit(1)

    configPath = sys.argv[1]
    if (not os.path.isfile(configPath)):
        sys.stderr.write("First argument must be a file : " + configPath)
        exit(2)

    basePath = sys.argv[2]
    if (not os.path.isdir(basePath)):
        sys.stderr.write("Second argument must be a directory : " + basePath)
        exit(3)


    print(extractNameAndDa(basePath))

    try:
        with open(configPath) as configFile:
            config = minidom.parse(configFile)
        checkDirectoryStructure(basePath, config.documentElement)
    except Exception as ex:
        sys.stderr.write("Error checking " + basePath, ex)
        exit(4)