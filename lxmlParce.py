'''
En récupérant les xml dispo sur le [site](http://data.assemblee-nationale.fr) et après avoir un peu exploré la structure du fichier scrutins:
'''
    from lxml import etree
    from collections import defaultdict

    scrutin_filename = "Scrutins_XIV"

    fp = open(scrutin_filename+".xml","r")
    scrutin_tree = etree.parse(fp)
    fp.close()
    for scrutin in scrutin_tree.findall(".//scrutin"):
        current_uid = scrutin.find("uid").text
        acteur_pours = scrutin.findall(".//pours/votant/acteurRef")
        for pour in acteur_pours:
            acteur_scrutin_pour[pour.text].append(current_uid)

'''
Tu as *acteur_scrutin_pour* un dictionnaire d'acteur qui on voté pour une liste de scrutins.
Tu fais pareil pour ceux qui ont voté contre, absenté.

Un exemple:
'''
    acteur_filename = "AMO10_deputes_actifs_mandats_actifs_organes_XIV"

    fp = open(acteur_filename+".xml","r")
    acteur_tree = etree.parse(fp)
    fp.close()
    for acteur in acteur_tree.findall(".//acteur"):
        current_uid = acteur.find("uid").text
        civ = acteur.find("etatCivil/ident/civ").text
        nom = acteur.find("etatCivil/ident/nom").text
        prenom = acteur.find("etatCivil/ident/prenom").text
        print civ,nom,prenom, "a vote POUR dans les scrutins suivant", acteur_scrutin_pour[current_uid]
        break
'''
Output: 

    M. Claireaux Stéphane a vote POUR dans les scrutins ['VTANR5L14V900', 'VTANR5L14V901', 'VTANR5L14V902', .....

Une fois que tu as fait la relation acteurRef et acteur.uid tu fais un peu ce que tu veux avec les données.

Dans le fichier acteur il y a les acteurs et les organes qui te seront utiles pour le fichier scrutin.
'''
