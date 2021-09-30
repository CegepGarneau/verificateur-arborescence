# Vérificateur d'arborescence
Permet de vérifier l'existance de fichiers et de dossier dans une arborescence, 
par exemple pour un travail pratique où l'on doit vérifier si une arborescence 
possède les bons fichiers et les bons répertoires, aux bons endroits.

# Fichier de configuration
Le fichier `config.xml.example` contient un exemple d'arborescence à vérifier, comme ceci :
```xml
<dir name=".">
    <dir name="Importations">
        <dir name="Photos">
            <file name="1.jpg"/>
            <file name="2.png"/>
            <file name="4.gif"/>
        </dir>
        <dir name="Textes">
            <file name="3.txt"/>
            <file name="5.docx"/>
        </dir>
    </dir>
    <dir name="Recherches">
        <dir name="Images">
            <dir name="gif"/>
            <dir name="jpg"/>
            <dir name="png"/>
        </dir>
        <dir name="Projet">
            <file name="Projet.docx"/>
        </dir>
    </dir>
    <dir name="Traitement d'images">
        <dir name="Originaux"/>
    </dir>
</dir>
```
**Important:** L'élément racine du fichier de configuration doit être une dossier nommé "."
# Utilisation 
```terminal
path-checker.py config.xml chemin\vers\le\dossier\a\verifier
```
