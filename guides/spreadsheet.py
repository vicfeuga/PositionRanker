import gspread 
import json

#Connexion
#Recuperer la clé privé pour se connecter au compte sheets
gc = gspread.service_account(filename='credentials.json')
#connexion au fichier de test
sh = gc.open_by_key('1opCI0k4ZEksc5HGvaYveSefHwGN8gwFdaWjV1qFIi0M')
#Connexion à la feuille 1
worksheet = sh.sheet1
#Connexion à la feuille par le nom
worksheet = sh.worksheet("Mots-clés")

liste=sh.worksheets()
liste_name=[]
for sheet in liste:
    liste_name.append(sheet.title)
print(liste_name[3:])
#affichage
#affiche toutes les données -> [{ 'Name':'Victor',...},{'Name':'Hugo',...},...]
res = worksheet.get_all_records() 
#affiche les valeurs -> [['Name, 'Age','City'],['Victor,'20','Bordeaux'],...]
res2 = worksheet.get_all_values()
#affiche les valeurs de la ligne 1 -> ['Name','Age','City']
res3 = worksheet.row_values(1)
#affiache les valeurs dans la plage A2:C2 -> [['Victor','20','Bordeaux']]
#res4 = worksheet.get('A2:C2')

#print(res)
#print(res2)
#print(res3)
#print(res4)

#Ajout d'un nouvel utilisateur dans les données
#user = ["Bapt",22,"Biarritz"]
#Ajout dans le doc à la derniere ligne
#worksheet.append_row(user)

#mise a jour de la cellule ligne 3 colonne 2
#worksheet.update_cell(3,2,30)

#suppression de la ligne 1
#worksheet.delete_rows(1)


