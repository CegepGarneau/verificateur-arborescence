import os
import sys


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
    checkDir(basePath, "importations")

    checkDir(basePath, "importations\\photos")
    checkDir(basePath, "importations\\textes")
    
    checkDir(basePath, "recherches")

    checkDir(basePath, "recherches\\images")
    checkDir(basePath, "recherches\\images\\gif")
    checkDir(basePath, "recherches\\images\\jpg")
    checkDir(basePath, "recherches\\images\\png")
    
    checkDir(basePath, "recherches\\liens")
    checkDir(basePath, "recherches\\réponses")

def checkImportation(basePath):
    """Checks files located in \\importations"""
    checkFile(basePath, "Importations\\Photos\\1.jpg")
    checkFile(basePath, "Importations\\Photos\\2.png")
    checkFile(basePath, "Importations\\Photos\\4.gif")
    
    checkFile(basePath, "Importations\\textes\\3.txt")
    checkFile(basePath, "Importations\\textes\\5.docx")

def checkImages(basePath):
    """Checks images located in Recherches\\images"""
    checkFile(basePath, "Recherches\\Images\\gif\\athlète.gif")
    checkFile(basePath, "Recherches\\Images\\jpg\\épreuve-olympique.jpg")
    checkFile(basePath, "Recherches\\Images\\png\\passion.png")

def checkLinks(basePath):
    """Checks if a Word file is located in Recherches\\liens"""
    checkFile(basePath, "Recherches\\liens\\liens.docx")

def checkAnswers(basePath):
    """Checks for Word files located in Recherches\\réponses"""
    checkFile(basePath, "Recherches\\réponses\\recherche.docx")    
    checkFile(basePath, "Recherches\\réponses\\réponses.docx")    


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write("Base directory needed")
        exit(1)

    basePath = sys.argv[1]
    if (not os.path.isdir(basePath)):
        sys.stderr.write("The argument must be a directory : " + basePath)
        exit(2)

    os.system("cls")

    print("DirectoryStructure")
    checkDirectoryStructure(basePath)
    
    print("Importations")
    checkImportation(basePath)

    print("Images")
    checkImages(basePath)

    print("Liens")
    checkLinks(basePath)

    print("Réponses")
    checkAnswers(basePath)