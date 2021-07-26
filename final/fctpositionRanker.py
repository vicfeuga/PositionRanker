#!/usr/bin/env python

import os 
import gspread
from fctClassement import *
from fctRankDomaine import *

def fctpositionRanker(id_workbook):
    #pour etre identifié sur internet
    #suivre guidePython~Googlesheet
    gc = gspread.service_account(filename='credentials.json')
        
    #/!\ a modifier si nouveau workbook
    #Connexion à la google sheet
    #identifiant du workbook dans la barre de recherche google (partie avant le /edit) 
    try:
        sh = gc.open_by_key(id_workbook)
    except:
        print("\n"+"~"*30)
        print("Erreur avec les credentials")
        quit()        

    #prend la page des mots-clés
    try:
        worksheet = sh.worksheet("Mots-clés")
    except:
        print("\n"+"~"*30)
        print("Erreur de connexion au workbook")
        quit()
    #recupere les mots clés dans la page mots-clés
    res = worksheet.get_all_values()
    data=[]
    for d in res:
        data.append(d[0])

    os.remove("classement.json")
    open("classement.json","x")

    #appel de la fonction de classement pour tous les mots clés
    get_classement(data)

    liste=sh.worksheets()
    #recupere tous les noms des feuilles -> liste_name[3:]=domaines
    liste_name=[]
    for sheet in liste:
        liste_name.append(sheet.title)

    #créer la liste des noms de domaine en feuille
    liste_dom=liste_name[3:]
    print(liste_dom)

    get_rankdomaine(liste_dom)

    #selection de la google sheet
    worksheetData=sh.worksheet('Data')

    #recupere les positions et infos des domaines
    data=[]
    with open('rankinMonDom.json','r') as f:
        data=json.load(f)
        
    #ecrit dans la sheet
    for d in data:
        new = [d['domaine'],d['mot_cle'],d['rank'],d['date'],d['lien']]
        worksheetData.append_row(new,table_range="A2")
        print(new)
