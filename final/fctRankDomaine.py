#!/usr/bin/env python
import json

#permet de recuperer la/les positions de notre nom de domaine
def get_rankdomaine(liste_domaines):
    data=[]
    #recupere les datas du classement
    with open('classement.json','r') as f:
        data=json.load(f)

    #nouveau data avec qu'avec mon nom de domaine
    data_monDom=[]
    data_monDom_bis=[]
    for nom_domaine in liste_domaines:
	#recupere si 'domaine' == monDom
        data_monDom_bis=[d for d in data if d['domaine']== nom_domaine]
        data_monDom.extend(data_monDom_bis)
    
    print(data_monDom_bis)
    #ecrit le ranking de mon domaine
    with open('rankinMonDom.json','w') as f:
        json.dump(data_monDom,f,indent=4)
