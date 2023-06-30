# Password Guesser

Ce projet est un générateur de mots de passe qui prend en compte différentes options de manipulation de mots, de dates et de caractères spéciaux.

## Options pour les mots

- Basculer toutes les lettres en minuscule
- Basculer toutes les lettres en majuscule
- Basculer la première lettre en majuscule
- Retirer les accents
- Utiliser le L33T (trouver toutes les combinaisons possibles)

Les combinaisons L33T prises en compte sont :
- a => 4
- e => 3
- i => 1
- o => 0
- l => 1
- s => 5
- b => 8
- t => 7
- z => 2
- g => 6

## Options pour les dates

- Séparer les informations des dates pour les combiner avec les mots (comportement par défaut)
- Utiliser les nombres des dates
- Transformer les dates en langage humain pour les mois
- Utiliser l'année sur 2 chiffres
- Utiliser l'année sur 4 chiffres
- Ajouter la possibilité de choisir la langue utilisée pour récupérer les noms des jours / mois

## Options caractères spéciaux

- Ajouter les caractères spéciaux les plus communs (.$?!*)
- Ajouter tous les caractères spéciaux
- Nombre de caractères spéciaux maximum dans la combinaison : [spécifiez le nombre maximum]

## Fonctionnalités de l'application

- Génération de mots de passe basée sur les options choisies
- Affichage du nombre de combinaisons possibles
- Exemple : 'J04EL14.-S23'
## Structure du code

Le code est implémenté en utilisant la programmation orientée objet. Voici les principaux fichiers et classes utilisés :

- `main.py` : Point d'entrée de l'application, contient la fonction principale `main()` qui instancie les objets nécessaires et utilise le générateur de mots de passe.


## Utilisation de concepts de POO

Le projet utilise plusieurs concepts de la programmation orientée objet :

- Polymorphism : Def:
				 Lien: 
- Encapsulation : Def: Les différentes fonctionnalités sont encapsulées dans des classes, permettant une meilleure organisation et réutilisation du code.
				  Lien:
- Héritage : Def: 
			 Lien: La classe `CommonSpecialCharacters` hérite de la classe `SpecialCharacters`.
- Composition : Def: 
				Lien: La classe `Checker` utilise les objets `OptionWord`, `OptionDate`, `AllSpecialCharacters` et `CommonSpecialCharacters`.
- Interface : Def:
			  Lien: 
- Méthodes et attributs d'objets : Def: Les différentes classes contiennent des méthodes pour manipuler les mots, les dates et les caractères spéciaux, ainsi que des attributs pour stocker les options et les données personnelles.
								   Lien: 
- Méthodes et attributs de classe : Def: 
									Lien: Les méthodes `generate_common_special_characters()` et `generate_all_special_characters()` dans la classe `Checker` sont des méthodes de classe.

Pour plus de détails sur la mise en œuvre de ces concepts, veuillez consulter le code source des fichiers correspondants.

## Comment exécuter l'application

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt Git sur votre machine.
3. Exécutez le fichier `main.py` à l'aide de la commande `python main.py`.
4. Les mots de passe générés et le nombre de combinaisons possibles seront affichés dans la console.

N'hésitez pas à explorer le code source et à apporter des modifications pour répondre à vos besoins spécifiques.

---



