Travaux Pratiques : Apprentissage Automatique et Expressions Régulières
Introduction
Dans	ce	TP,	nous	allons	travailler	sur	deux	exercices	:
1.	Apprentissage	automatique	supervisé	:	Créer	un	modèle	de	classification	sur	un	jeu	de	
données.
2.	Utilisation	des	expressions	régulières	pour	extraire	des	informations	spécifiques	d’un	
texte,	avec	une	complexité	accrue.
Exercice 1 : Apprentissage automatique supervisé (Classification)
Objectif	:	Créer	un	modèle	d'IA	capable	de	reconnaître	et	de	classifier	des	images	à	l'aide	
d'un	réseau	de	neurones	convolutif	(CNN)	avec	la	bibliothèque	Keras.
Étape	1	:	Préparation	de	l'environnement
1. Installer	les	bibliothèques	nécessaires.	Utilisez	pip	pour	installer	tensorflow,	
keras,	et	matplotlib.
Étape	2	:	Chargement	du	dataset	et	normalisation
1. Chargement	du	dataset	Fashion-MNIST.	Utilisez	les	fonctions	appropriées	pour	
obtenir	les	ensembles	d'entraînement	et	de	test.
2. Normalisation	des	images.	Quelle	est	la	méthode	pour	normaliser	les	images	?
3. Affichage	d'une	image	du	dataset.	Affichez	une	image	et	affichez	son	étiquette.	
Comment	identifiez-vous	l'étiquette	associée	?
Étape	3	:	Création	du	modèle	CNN
1. Reshape	des	images.	Modifiez	la	forme	des	images	pour	les	adapter	à	l'entrée	du	
modèle	CNN.
2. Création	du	modèle	CNN.	Construisez	un	modèle	avec	plusieurs	couches	de	
convolution	et	de	pooling.	
3. Compilation	du	modèle.	Quels	sont	les	paramètres	importants	lors	de	la	
compilation	du	modèle	?
Étape	4	:	Entraînement	du	modèle
1. Entraînez	le	modèle en	utilisant	l'ensemble	d'entraînement.	Quels	paramètres	
définissez-vous	pour	l'entraînement	?
2. Évaluation	du	modèle.	Après	l'entraînement,	évaluez	la	précision	du	modèle	sur	
l'ensemble	de	test.
Étape	5	:	Visualisation	des	prédictions
1. Prédiction	sur	les	données	de	test.	Utilisez	le	modèle	pour	prédire	les	classes	des	
images	de	test.
2. Affichage	des	résultats.	Créez	une	fonction	pour	afficher	une	image,	la	prédiction	
du	modèle,	et	l'étiquette	réelle.	Que	devez-vous	observer	pour	évaluer	la	
performance	du	modèle	?
Livrables
Code	du	modèle	de	classification sur	Github
Exercice 2 : Expressions régulières avancées
Objectif	:	Extraire	des	informations	complexes	depuis	un	texte	avec	des	expressions	
régulières	avancées.
Consignes	:
1.	Fournir	un	fichier	texte	contenant	plusieurs	adresses	email,	numéros	de	téléphone,	dates	
et	URL.
2.	Extraire	toutes	les	adresses	email	valides.
3.	Extraire	les	numéros	de	téléphone	dans	plusieurs	formats	(par	exemple,	10	chiffres,	
formats	internationaux).
4.	Extraire	les	dates	(formats	DD/MM/YYYY,	MM-DD-YYYY,	etc.).
5.	Extraire	toutes	les	URL	et	vérifier	si	elles	utilisent	le	protocole	HTTPS.
6.	Outils suggérés
Python	(module	re),	sites	de	test	de	regex	(regex101.com)
Livrables
Code	des	expressions	régulières	avec	tests	et	capture	d’écran	des	résultats	sur	
regex101.com sur	Github
