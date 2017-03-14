# -*- coding: utf8 -*-
import AMO20_dep_sen_min_tous_mandats_et_organes_XIV
import Scrutins_XIV
import operator
import time

def all(b):
    bucket = []
    for export, exportant in b.iteritems() :
        for acteurs, values in exportant.iteritems():
            if acteurs == 'acteurs':
                for acteur, acteurInfo in values.iteritems():
                    for acteurInfoDicts in acteurInfo:
                            bucket.append(acteurInfoDicts)
    return bucket


def getAllDepRefs(tous):
    bucket = []
    for mandats in tous:
        for mandat in mandats[u'mandats'][u'mandat']:
            pitcher = {}
            if mandat[u'typeOrgane'] == u'ASSEMBLEE':
#				pitcher[u'organeRef'] = mandat[u'organes'][u'organeRef']
                pitcher[u'acteurRef'] = mandat[u'acteurRef']
                pitcher[u'nom'] = mandats[u'etatCivil'][u'ident'][u'nom']
                pitcher[u'prenom'] = mandats[u'etatCivil'][u'ident'][u'prenom']
                if pitcher not in bucket:
                    bucket.append(pitcher)
    return bucket

def votes(refs,a):
    bucket = {}
    for ref in refs:
        pitcher=[]
        for scrutins in Scrutins_XIV.data().values():
            for scrutinList in scrutins.values():
                for scrutin in scrutinList:
                    for groupe in scrutin[u'ventilationVotes'][u'organe'][u'groupes'][u'groupe']:
                        for intention, votes in groupe[u'vote'][u'decompteNominatif'].iteritems():
#							print votes
                            if a == u'tout':
                                if type(votes) is dict:
                                    if type(votes[u'votant']) is dict :
                                        if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:
                                            pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                    elif type(votes[u'votant']) is list :
                                        for votants in votes[u'votant']:
                                            if votants[u'acteurRef'] == ref[u'acteurRef']:
                                                pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                else :
                                    pass
                            elif a== u'pours':
                                if intention == u'pours':
                                    if type(votes) is dict:
                                        if type(votes[u'votant']) is dict :
                                            if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:
#												print "pouuuuuuurs", votes
                                                pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
#												print "pourrrrs"
                                        elif type(votes[u'votant']) is list :
                                            for votants in votes[u'votant']:
                                                if votants[u'acteurRef'] == ref[u'acteurRef']:
                                                    pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                    else :
                                        pass
                            elif a== u'contres':
                                if intention == u'contres':
                                    if type(votes) is dict:
                                        if type(votes[u'votant']) is dict :
                                            if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:
                                                pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                        elif type(votes[u'votant']) is list :
                                            for votants in votes[u'votant']:
                                                if votants[u'acteurRef'] == ref[u'acteurRef']:
                                                    pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                    else :
                                        pass
                            elif a== u'abstentions':
                                if intention == u'abstentions':
                                    if type(votes) is dict:
                                        if type(votes[u'votant']) is dict :
                                            if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:
                                                pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                        elif type(votes[u'votant']) is list :
                                            for votants in votes[u'votant']:
                                                if votants[u'acteurRef'] == ref[u'acteurRef']:
                                                    pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                    else :
                                        pass

                            elif a== u'nonVotant':
                                if intention == u'nonVotant':
                                    if type(votes) is dict:
                                        if type(votes[u'votant']) is dict :
                                            if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:
                                                pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                        elif type(votes[u'votant']) is list :
                                            for votants in votes[u'votant']:
                                                if votants[u'acteurRef'] == ref[u'acteurRef']:
                                                    pitcher.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                                    else :
                                        pass

                            else :
                                pass
            if pitcher != []:
                ref[u'lois'] = pitcher
    return refs

''' meme  == le voteur vote pareil que son groupe
oppose == le voteur vote pour, son groupe vote contre
neutre == le voteur vote abstentions alors que son groupe a voté pour/contre
rogue == le voteur vote pour/contre alors que son groupe vote abstention'''
def compareWithGroupe(voteParIntention):
    gallon = {}

    for voteur in voteParIntention:
        pitcher = {u'nbMemes':[], u'nbOppose':[], u'nbNeutres':[], u'nbRogues':[], u'nbAbs':[]}
        glass = {u'nbPours':[], u'nbContres':[], u'nbAbstentions':[], u'nbAbsences':[]}
        if voteur[u'acteurRef'] not in gallon.keys():
            bucket = {voteur[u'acteurRef']: pitcher}
            gallon.update(bucket)
        try:
            for loi in voteur[u'lois']:
                if loi[u'positionMajoritaire']+u's' == loi[u'position']:
                    pitcher[u'nbMemes'].append(loi)
                    if loi[u'position']==u'pours':
                        glass[u'nbPours'].append(loi)
                    if loi[u'position']==u'contres':
                        glass[u'nbContres'].append(loi)

                elif loi[u'position'] == u'nonVotants':
                    pitcher[u'nbAbs'].append(loi)
                    glass[u'nbAbsences'].append(loi)

                elif loi[u'positionMajoritaire'] == u'contre':
                    if loi[u'position'] == u'pours':
                        pitcher[u'nbOppose'].append(loi)
                        glass[u'nbPours'].append(loi)
                    if loi[u'position'] == u'abstentions':
                        pitcher[u'nbNeutres'].append(loi)
                        glass[u'nbAbstentions'].append(loi)

                elif loi[u'positionMajoritaire'] == u'pour':
                    if loi[u'position'] == u'contres':
                        pitcher[u'nbOppose'].append(loi)
                        glass[u'nbContres'].append(loi)
                    if loi[u'position'] == u'abstentions':
                        pitcher[u'nbNeutres'].append(loi)
                        glass[u'nbAbstentions'].append(loi)

                elif loi[u'positionMajoritaire'] == u'abstention':
                    if loi[u'position'] == u'abstentions':
                        pitcher[u'nbMemes'].append(loi)
                        glass[u'nbAbstentions'].append(loi)

                    if loi[u'position'] == u'pours':
                        pitcher[u'nbRogues'].append(loi)
                        glass[u'nbPours'].append(loi)

                    if loi[u'position'] == u'contres':
                        pitcher[u'nbRogues'].append(loi)
                        glass[u'nbContres'].append(loi)
        except:
            pass
        voteur[u'votes']= glass
        voteur[u'comparaison']=pitcher
#	for voteur in voteParIntention:
#		for position, lenPos in voteur[u'comparaison'].iteritems():
#			print position, len(lenPos)
    return voteParIntention

def printVotes(voteParIntention):
    for voteur in voteParIntention:

        print '\n',voteur[u'nom'], voteur[u'prenom']
        for typeDeVote, lenVotes in voteur[u'votes'].iteritems():
            print typeDeVote,'\t', len(lenVotes)

def expl(voteParIntention, a):
    for voteur in voteParIntention:
#		try:
        if len(voteur[u'comparaison'][a])>0:
            print voteur[u'nom'], voteur[u'prenom']
            for loi in voteur[u'comparaison'][a]:
                print loi[u'libelle'], u'\nposition de la personne: ', loi[u'position'], u'\tpositionMajoritaire:', loi[u'positionMajoritaire'],'\n'


def badBoy(voteParIntention):
    classement = []
# TODO [u'2':u'mandatRef':u'i', u'nbOppose':3},{u'3':{u'mandatRef':u'i', u'nbOppose':3}]
# {u'meme':[], u'oppose':[], u'neutre':[], u'rogue':[], u'abs':[]}
    for voteur in voteParIntention:
        indiv = {u'ident':{u'nom':voteur[u'nom'], u'prenom':voteur[u'prenom']}, u'nbOppose':len(voteur[u'comparaison'][u'nbOppose']),u'nbMemes' : len(voteur[u'comparaison'][u'nbMemes']), u'nbNeutres' : len(voteur[u'comparaison'][u'nbNeutres']), u'nbRogues' : len(voteur[u'comparaison'][u'nbRogues']),
                 u'nbAbs' : len(voteur[u'comparaison'][u'nbAbs'])}
        classement.append(indiv)
    DictDeClass = {u'nbOppose':sorted(classement, key = lambda k: k[u'nbOppose'], reverse=True), u'nbMemes':sorted(
        classement, key = lambda k: k[u'nbMemes'], reverse=True), u'nbNeutres':sorted(classement, key = lambda k: k[u'nbNeutres'], reverse=True), u'nbRogues':sorted(classement, key = lambda k: k[u'nbRogues'], reverse=True), u'nbAbs':sorted(classement, key = lambda k: k[u'nbAbs'], reverse=True)}
    for classType, sortedClassement in DictDeClass.iteritems():
        print classType
        try:
            topTen = sortedClassement[:10]
            for indiv in topTen:
                print topTen.index(indiv), '\t', indiv[u'ident'][u'prenom'], indiv[u'ident'][u'nom'], '\t', \
                    indiv[classType]
        except:
            print sortedClassement[0][classType]
    return DictDeClass

def indiv(b, nom, prenom):
    bucket = []
    for export, exportant in b.iteritems() :
        for acteurs, values in exportant.iteritems():
            if acteurs == 'acteurs':
                for acteur, acteurInfo in values.iteritems():
                    for acteurInfoDicts in acteurInfo:
                        for uid_etatCivil_mandats, uidEtatCivilMandatsInfos in acteurInfoDicts.iteritems():
                            if uid_etatCivil_mandats == 'etatCivil':
                                for persInfoKey, PersInfo in uidEtatCivilMandatsInfos.iteritems():
                                    if persInfoKey == u'ident':
                                        if PersInfo[u'nom']== nom:
                                            bucket.append(acteurInfoDicts)
    return bucket

def getRefs(indiv, choixNom, choixPreNom):

    bucket = []
    for mandats in indiv:
        for mandat in mandats[u'mandats'][u'mandat']:
            pitcher = {}
            if mandat[u'typeOrgane'] == u'ASSEMBLEE':
#				pitcher[u'organeRef'] = mandat[u'organes'][u'organeRef']
                pitcher[u'acteurRef'] = mandat[u'acteurRef']
                pitcher[u'nom'] = mandats[u'etatCivil'][u'ident'][u'nom']
                pitcher[u'prenom'] = mandats[u'etatCivil'][u'ident'][u'prenom']
                if pitcher not in bucket:
                    bucket.append(pitcher)
    return bucket

def votesIndivs(a, refs):
    bucket = {}
    for scrutins in Scrutins_XIV.data().values():
        for scrutinList in scrutins.values():
            for scrutin in scrutinList:
                for groupe in scrutin[u'ventilationVotes'][u'organe'][u'groupes'][u'groupe']:
                    for intention, votes in groupe[u'vote'][u'decompteNominatif'].iteritems():
                        if type(votes) is dict:
                            if type(votes[u'votant']) is list:
                                for votants in votes[u'votant']:
                                    for ref in refs:
                                        if votants[u'acteurRef'] == ref[u'acteurRef']:
                                            bucket.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                            elif type(votes[u'votant']) is dict:
                                if votes[u'votant'][u'acteurRef'] == ref[u'acteurRef']:

                                    bucket.append({u'libelle': scrutin[u'objet'][u'libelle'], u'position' : intention, u'positionMajoritaire': groupe[u'vote'][u'positionMajoritaire']})
                        else:
                            pass
    return bucket
