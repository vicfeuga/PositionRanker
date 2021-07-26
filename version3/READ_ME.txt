Voici la documentation de la version 3 du Position Google Tracker.

Le package est composé d'un dossier "final" qui contient le programme final
et ses différents fichiers. Et un dossier "guide" qui contient différents guides
pour mieux comprendre le code.

Dans cette version 3, le programme va dans un premier temps recuperer les 
nb premiers resultats de la recherche pour les mots clés contenus sur une page
google sheet. Puis, il va extraitre de ces requetes les lignes contenant les 
noms de domaines (noms des feuilles dans le fichier google sheet) voulus.
Ces données sont alors envoyées sur le google sheet. Et seront ensuite filtrées 
sur la page correspondante au nom de domaine approprié.

Pour lancer le programme, il suffit d'etre dans le repertoire "final" et entrer
la commande dans le terminal: python3 positionRanker.py (ou utiliser un 
compilateur python, ex:Thonny)
Une fois le progamme lancé, il va demander d'entrer l'id du workbook sur lequel
on souhaite travailler.

/!\ Le workbook doit etre sembable à celui utilisé en exemple /!\

Il faut s'assurer que l'utilisateur avec lequel on souhaite se connecter ait 
les droits. Pour cette partie, regarder le fichier guidePython~GoogleSheets.txt
dans le dossier guide.

