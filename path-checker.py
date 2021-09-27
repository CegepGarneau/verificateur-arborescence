import re
import os
import sys

def extractNameAndDa(path):
    """
    Extracts the name and DA from path generated from Omnivox's files
    Ex : Noel-Parise_1944993_TP_1_-_Recherche_Int_Remis_le_2021-09-06_17h51m51s
    """
    return re.search("[A-Za-z\-]+\_\d{7}", path).group(0)

def validate(test, message):
    """Displays a message if a test is false"""
    if (not test):
        print("### " + message)

def checkFile(basepath, path, message="Missing file"):
    """Checks whether a file exists and if not, displays an error message"""
    validate(os.path.isfile(os.path.join(basePath, path)), message + " : " + path)

def checkDir(basepath, path, message="Missing directory"):
    """Checks whether a directory exists and if not, displays an error message"""
    validate(os.path.isdir(os.path.join(basePath, path)), message + " : " + path)

def checkDirectoryStructure(basePath):
    """Checks the general directory structure"""
    checkDir(basePath, "Importations")

    checkDir(basePath, "Importations\\Photos")
    checkDir(basePath, "Importations\\Textes")
    
    checkDir(basePath, "Recherches")

    checkDir(basePath, "Recherches\\Images")
    checkDir(basePath, "Recherches\\Images\\gif")
    checkDir(basePath, "Recherches\\Images\\jpg")
    checkDir(basePath, "Recherches\\Images\\png")
    
    checkDir(basePath, "Recherches\\Projet")
    
    checkDir(basePath, "Traitement d'images")
    checkDir(basePath, "Traitement d'images\\Originaux")

def checkImportation(basePath):
    """Checks files located in \\Importations"""
    checkFile(basePath, "Importations\\Photos\\1.jpg")
    checkFile(basePath, "Importations\\Photos\\2.png")
    checkFile(basePath, "Importations\\Photos\\4.gif")
    
    checkFile(basePath, "Importations\\textes\\3.txt")
    checkFile(basePath, "Importations\\textes\\5.docx")

def checkProjet(basePath):
    """Checks Images located in Recherches\\Projet"""
    checkFile(basePath, "Recherches\\Projet\\Projet.docx")


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write("Base directory needed")
        exit(1)

    basePath = sys.argv[1]
    if (not os.path.isdir(basePath)):
        sys.stderr.write("The argument must be a directory : " + basePath)
        exit(2)

    os.system("cls")

    print(extractNameAndDa(basePath))

    checkDirectoryStructure(basePath)
    checkImportation(basePath)
    checkProjet(basePath)

    print()
    print("Done")