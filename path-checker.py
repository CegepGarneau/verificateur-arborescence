import os
import sys


def validate(test, message):
    if (not test):
        sys.stderr.write(message)

def checkFile(path, message="Missing file"):
    validate(not os.path.isfile(path), message + " : " + path)

def checkDir(path, message="Missing file"):
    validate(not os.path.isdir(path), message + " : " + path)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.stderr.write("Base directory needed")
        exit(1)

    basePath = sys.argv[1]
    if (not os.path.isdir(basePath)):
        sys.stderr.write("The argument must be a directory : " + basePath)
        exit(2)

    basePath = os.path.abspath(basePath)

    print("Working with " + basePath)