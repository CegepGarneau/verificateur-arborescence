"""
Permet de vérifier l'existance de fichiers et de dossier dans une arborescence,
par exemple pour un travail pratique où l'on doit vérifier si une arborescence
possède les bons fichiers et les bons répertoires, aux bons endroits.
"""

import re
import os
import sys
import traceback
import xml.dom.minidom as minidom


def extract_name_and_da(path):
    """
    Extracts the name and DA from path generated from Omnivox's files
    Ex :
    Noel-Parise_1944993_TP_1_-_Recherche_Int_Remis_le_2021-09-06_17h51m51s
    Yergeau-Rhéaume_2042114_TP_1_Remis_le_2021-09-09_13h37m17s
    """
    return re.search("(-|[^\W\d])+\_\d{7}", path).group(0)


def validate(test, message):
    """Displays a message if test is false"""
    if not test:
        print("### " + message)
    return test


def check_file(dirpath, filename, message="Missing file"):
    """Checks if a file exists and if not, displays an error message"""
    filepath = os.path.join(dirpath, filename)
    return validate(os.path.isfile(filepath), message + " : " + filepath)


def check_dir(path, message="Missing directory"):
    """Checks whether a directory exists and if not, displays an error message"""
    return validate(os.path.isdir(path), message + " : " + path)


def check_directory_structure(parent_path, current_node):
    """Checks the general directory structure"""
    arg_type = current_node.nodeName

    if arg_type == "file":
        check_file(parent_path, current_node.getAttribute("name"))
    elif arg_type == "dir":
        current_path = os.path.join(
            parent_path, current_node.getAttribute("name"))
        if check_dir(current_path):
            for child in current_node.childNodes:
                if child.nodeType == minidom.Node.ELEMENT_NODE:
                    check_directory_structure(current_path, child)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Two arguments needed : config file and base directory")
        exit(1)

    config_path = sys.argv[1]
    if not os.path.isfile(config_path):
        sys.stderr.write("First argument must be a file : " + config_path)
        exit(2)

    base_path = sys.argv[2]
    if not os.path.isdir(base_path):
        sys.stderr.write("Second argument must be a directory : " + base_path)
        exit(3)

    print(extract_name_and_da(base_path))

    try:
        with open(config_path) as configFile:
            config = minidom.parse(configFile)
        check_directory_structure(base_path, config.documentElement)
    except Exception as ex:
        print("Error checking " + base_path, file=sys.stderr)
        traceback.print_exc()
        exit(4)
