############
Introduction
############

Contenu
#######

raw data from http://data.assemblee-nationale.fr/travaux-parlementaires/votes au format html
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

AMO20_dep_sen_min_tous_mandats_et_organes_XIV.json.html.zip_ Correspond aux données individuelles des députés et sénateurs

.. _https://github.com/deputes/deputes.github.io/blob/master/AMO20_dep_sen_min_tous_mandats_et_organes_XIV.json.html.zip

Scrutins_XIV.json.html_ corrsepond aux détail des votes de l'assemblée nationale

.. _https://github.com/deputes/deputes.github.io/blob/master/Scrutins_XIV.json.html

codes d'extraction, de recherche et d'analyse
"""""""""""""""""""""""""""""""""""""""""""""""

lxmlParce.py_ permet de récuperer des informations de Scrutins_XIV.lxml

.. _https://github.com/deputes/deputes.github.io/blob/master/lxmlParce.py 

j2p.py_ permet de récuperer les informations de Scrutins_XIV.json. Les fichiers HTML précédemment cités ont étés construits avec ce code. Permet aussi l'écriture de fichiers intermédiaires pour réduire le runtime.

*InOutDep.py* permet de faire tourner *deputes_assembly.py*, qui permet de faire une première analyse superficielle des données:

- nombre de votes pours/contres/abstentions/nonVotants (ou tous) pour chaque individu, et l'intitulé des lois pours/contres etc.
- le classement des personnes votant le plus / le moins en accord avec leur groupe parlementaire (+ détail)

Les prochains commits porteront sur (députés par lieu), (lois par types de votes).

.. _https://github.com/deputes/deputes.github.io/blob/master/json2Html.py


Don't expect anything great.


