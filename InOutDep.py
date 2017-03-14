# -*- coding: utf8 -*-
# selectionable options
#coding: utf8


import depute_assembly
import AMO20_dep_sen_min_tous_mandats_et_organes_XIV
import j2p
import time


#TODO:

''' 
Concerning Individuals :
- organe Type : parti politique
- noms DONE
- prenoms DONE
- nb votes contres / pours tot DONE
- nb/% votes à l'encontre de son parti DONE
- nb/% votes à l'encontre du gouv
- historique
	- votes individuels DONE

Concerning Partis :
- names
- adherents
- historique des votes
- lois les plus clivantes/rassemblantes

Concerning votes parlementaires :
- nb/% totaux (periode de temps) pours/contres/abs/ nnv
		- par parti
			- par individu
- nb/% par loi pours/contres/abs/nnv
		- par parti
			- par individu
Concerning Lois :
- qui pour/contre
- passé/refusé
- à quel point biparti (groupe qui présente vs. ceux qui sont pours)

Concerning Regions


'''
#j2p.convertPy(*.json)

def UserInput():
	t0 = time.time()
	choixIndivAll= raw_input(u'voulez-vous tous les acteurs ou un seul acteur? \n répondez par tous / un \n'.encode('utf-8')).decode('utf-8')
	choixIndivAll.encode('utf-8')
	b = AMO20_dep_sen_min_tous_mandats_et_organes_XIV.data()
	if choixIndivAll == u'tous':
# Commentez à partir de ici
#		bucket = depute_assembly.all(b)
#		ref= depute_assembly.getAllDepRefs(bucket)
#		TypeDeVote = raw_input(u"trier par quel type de vote?\nentrez:\npours / contres / abstentions / nonVotants / tout\n").decode('utf-8')
#		bucket = depute_assembly.votes(ref, TypeDeVote)
#		savedTousDeps = j2p.writePy(u'tousDeps', bucket)
#		print "saved %tousDeps.py. Vous pouvez mettre en commentaire plusieurs lignes pour économiser du temps lors des prochaines recherches. Cf: InOutDep.py"
# Commentez jusque ici. Si vous voulez regarder un autre type de vote, vous devez recreer tousDeps.py. changez eventuellement le nom, par exemple: tousDeps, poursDeps, contresDep, absDeps...
		import tousDeps
		bucket = tousDeps.data()
		compar = depute_assembly.compareWithGroupe(bucket)
		printVotes = depute_assembly.printVotes(bucket)
		badBoy = depute_assembly.badBoy(bucket)
		questionDetails = raw_input(u'explicitez :\nposition\tpour expliciter la comparaison au groupe (memes/opposés...)'
									u'parlementaire\nvote\t\tpour expliciter les types de votes (pours/contres...)\npersonne\tpour '
									u'expliciter un individu\nATTENTION expliciter vote is broken in current version')
		if questionDetails == u'position':
			detailPosition = raw_input(u'quelle position expliciter? Entrez:\nnbMemes\npour le nombre de votes individuels identiques au vote majoritaire de leur groupe parlementaire\nnbContres\npour le nombre de votes individuels contraires au vote majoritaire de leur groupe parlementaire.\nnbNeutres\npour le nombre de votes individuels abstenus, lorsque son groupe majoritaire vote pour ou contre\nnbRogues\npour le nombre de votes individuels pours ou contres, lorsque la position Majoritaire est abstention\nnbAbs\npour le nombre de votes absents\n')
			expl = depute_assembly.expl(compar, detailPosition)
		if questionDetails == u'personne':
			choixPreNom = raw_input(u'entrez un prenom comme ceci : \n prenom : Manuel\nprenom : ').decode('utf-8')
			choixNom = raw_input(u'entrez un nom, comme ceci : \n nom : Valls\nnom : ').decode('utf-8')
			indiv = depute_assembly.indiv(b, choixNom, choixPreNom)
			refs = depute_assembly.getAllDepRefs(indiv)
			# TODO: GetLois()
			TypeDeVote = raw_input(u"afficher quel type de vote? \n pours / contres / neutres / abstentions / nonVotants / tout\n").decode('utf-8')
			votesIndivs = depute_assembly.votes(refs, TypeDeVote)
			compar = depute_assembly.compareWithGroupe(votesIndivs)
			printVotes = depute_assembly.printVotes(compar)
			badBoy = depute_assembly.badBoy(votesIndivs)
			detailPosition = raw_input(
				u'quelle position expliciter? Entrez:\nnbMemes\tpour le nombre de votes individuels identiques au '
				u'vote majoritaire de leur groupe parlementaire\nnbContres\tpour le nombre de votes individuels contraires au vote majoritaire de leur groupe parlementaire.\nnbNeutres\tpour le nombre de votes individuels abstenus, lorsque son groupe majoritaire vote pour ou contre\nnbRogues\tpour le nombre de votes individuels pours ou contres, lorsque la position Majoritaire est abstention\nnbAbs\t\tpour le nombre de votes absents\n')
			expl = depute_assembly.expl(compar, detailPosition)


	elif choixIndivAll == u'un':
		choixPreNom= raw_input(u'entrez un prenom comme ceci : \n prenom : Manuel\nprenom : ').decode('utf-8')
		choixNom= raw_input(u'entrez un nom, comme ceci : \n nom : Valls\nnom : ').decode('utf-8')
		indiv = depute_assembly.indiv(b, choixNom, choixPreNom)
		refs = depute_assembly.getAllDepRefs(indiv)
# TODO: GetLois(
		TypeDeVote = raw_input(u"afficher quel type de vote? \n pours / contres / neutres / abstentions / nonVotants / tout\n").decode('utf-8')
		votesIndivs=depute_assembly.votes(refs, TypeDeVote)
		compar = depute_assembly.compareWithGroupe(votesIndivs)
		badBoy = depute_assembly.badBoy(votesIndivs)
		detailPosition = raw_input(u'quelle position expliciter? Entrez:\nnbMemes\npour le nombre de votes individuels identiques au vote majoritaire de leur groupe parlementaire\nnbContres\npour le nombre de votes individuels contraires au vote majoritaire de leur groupe parlementaire.\nnbNeutres\npour le nombre de votes individuels abstenus, lorsque son groupe majoritaire vote pour ou contre\nnbRogues\npour le nombre de votes individuels pours ou contres, lorsque la position Majoritaire est abstention\nnbAbs\npour le nombre de votes absents\n')
		expl = depute_assembly.expl(compar, detailPosition)
#		detailPosition = raw_input(u'expliciter une position (oppose/meme/abs/rogue) ou une personne?')
#		explain = depute_assembly.expl(compar)

	t1= time.time()
	print t1-t0
UserInput()


'''
def choisissez():
#	choix1 = str(input ("voulez-vous regarder un acteur, un lieu, un parti, une loi ou un organisme? choisissez "))
	choix1 = "acteur"
	if choix1 == "acteur":
#		choix2 = input("précisez comme tel :: 'kader arif' ::")
		choix3 = input("voulez-vous tout savoir? o / n")
		if choix3 == "o":
			
			choix
	if choix1 == "loi":
		choix2 == input("par acteur, lieu, parti ou organisme?")
		if choix2 == 'acteur':
			pass
		if choix2 == "parti":
			pass
		if choix2 == 'organisme':
			pass 
'''
#choisissez()			
#depute_assembly.combineTousMandats(a,b)
