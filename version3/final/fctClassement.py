#!/usr/bin/env python
import json
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from datetime import date



#permet d'obtenir le top nb des sites pour un mot clé
def get_classement(mots):
    data=[]
    nb=25
    for mot_clé in mots:
        #nombre de resultats
        #URL
        url="https://www.google.com/search?q="+mot_clé+"&num="+str(nb)
        
        #User Agent
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
        #requete de connexion
        r = requests.get(url,headers=headers)
        
        #parse la page resultat
        soup = BeautifulSoup(r.content, 'html.parser')
        #recupere toutes les classes g
        rows = soup.select('.g')
        
        #data
        #rang 
        rank=0
        #date d'aujourd'hui
        today = date.today()
        d1=today.strftime("%d/%m/%Y")
        #navigue dans les rows
        for row in rows:
            rank=rank+1
            #dictionnaire pour un site
            d=dict()
            d['domaine']=urlparse(row.select_one('a')['href']).netloc #recupere le nom de domaine
            d['mot_cle']=mot_clé #mot clé
            d['rank']=rank #recupere le rang dans la recherche
            d['date']=d1 #recupere la date du jour
            d['lien']=row.select_one('a')['href'] #recupere le lien
            
            #concatenation des lignes
            data.append(d)
    #ecriture dans le fichier
    with open('classement.json','a') as f:
        json.dump(data,f,indent=4)
