# Password Guesser

Ce projet est un g�n�rateur de mots de passe qui prend en compte diff�rentes options de manipulation de mots, de dates et de caract�res sp�ciaux.

## Options pour les mots

- Basculer toutes les lettres en minuscule
- Basculer toutes les lettres en majuscule
- Basculer la premi�re lettre en majuscule
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

- S�parer les informations des dates pour les combiner avec les mots (comportement par d�faut)
- Utiliser les nombres des dates
- Transformer les dates en langage humain pour les mois
- Utiliser l'ann�e sur 2 chiffres
- Utiliser l'ann�e sur 4 chiffres
- Ajouter la possibilit� de choisir la langue utilis�e pour r�cup�rer les noms des jours / mois

## Options caract�res sp�ciaux

- Ajouter les caract�res sp�ciaux les plus communs (.$?!*)
- Ajouter tous les caract�res sp�ciaux
- Nombre de caract�res sp�ciaux maximum dans la combinaison : [sp�cifiez le nombre maximum]

## Fonctionnalit�s de l'application

- G�n�ration de mots de passe bas�e sur les options choisies
- Affichage du nombre de combinaisons possibles
- Exemple : 'J04EL14.-S23'
## Structure du code

Le code est impl�ment� en utilisant la programmation orient�e objet. Voici les principaux fichiers et classes utilis�s :

- `main.py` : Point d'entr�e de l'application, contient la fonction principale `main()` qui instancie les objets n�cessaires et utilise le g�n�rateur de mots de passe.


## Utilisation de concepts de POO

Le projet utilise plusieurs concepts de la programmation orient�e objet :

- Polymorphism : Def:
				 Lien: 
- Encapsulation : Def: Les diff�rentes fonctionnalit�s sont encapsul�es dans des classes, permettant une meilleure organisation et r�utilisation du code.
				  Lien:
- H�ritage : Def: 
			 Lien: La classe `CommonSpecialCharacters` h�rite de la classe `SpecialCharacters`.
- Composition : Def: 
				Lien: La classe `Checker` utilise les objets `OptionWord`, `OptionDate`, `AllSpecialCharacters` et `CommonSpecialCharacters`.
- Interface : Def:
			  Lien: 
- M�thodes et attributs d'objets : Def: Les diff�rentes classes contiennent des m�thodes pour manipuler les mots, les dates et les caract�res sp�ciaux, ainsi que des attributs pour stocker les options et les donn�es personnelles.
								   Lien: 
- M�thodes et attributs de classe : Def: 
									Lien: Les m�thodes `generate_common_special_characters()` et `generate_all_special_characters()` dans la classe `Checker` sont des m�thodes de classe.

Pour plus de d�tails sur la mise en �uvre de ces concepts, veuillez consulter le code source des fichiers correspondants.

## Comment ex�cuter l'application

1. Assurez-vous d'avoir Python install� sur votre machine.
2. Clonez ce d�p�t Git sur votre machine.
3. Ex�cutez le fichier `main.py` � l'aide de la commande `python main.py`.
4. Les mots de passe g�n�r�s et le nombre de combinaisons possibles seront affich�s dans la console.

N'h�sitez pas � explorer le code source et � apporter des modifications pour r�pondre � vos besoins sp�cifiques.

---



