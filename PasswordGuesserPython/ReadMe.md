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

- Polymorphism : **Def**: Le polymorphisme permet à des objets de différentes classes de répondre de manière différente à une même méthode. Cela signifie que vous pouvez utiliser une même méthode sur des objets de classes différentes et obtenir des résultats différents en fonction de la classe réelle de chaque objet.
				 **Lien**: Entre la classe `AllSpecChar` et la class `Commonchar` elles utilisent toutes les deux une méthodes hérités de `CheckCaractere` mais 					ne renvoie pas au même résultat.
- Encapsulation : **Def**: L'encapsulation est un concept qui consiste à regrouper les données et les méthodes qui les manipulent en une seule entité, appelée classe. L'encapsulation permet de cacher les détails internes de la classe et de fournir une interface publique pour interagir avec l'objet. Cela permet de garantir l'intégrité des données et de contrôler l'accès à celles-ci. 
				  **Lien**: Le constructeur `__init__` de la classe `CheckDate` qui est en mode
- Héritage : **Def**:  L'héritage est un concept de la programmation orientée objet qui permet à une classe d'hériter des attributs et des méthodes d'une classe parente. La classe héritière, appelée sous-classe, peut étendre ou modifier le comportement de la classe parente, appelée superclasse. L'héritage facilite la réutilisation du code et permet de créer des hiérarchies de classes.
			**Lien**: La classe `CommonSpecialCharacters` hérite de la classe `SpecialCharacters`.
- Composition : **Def**: La composition est un concept dans lequel une classe est composée d'autres objets. Cela signifie qu'un objet peut contenir des instances d'autres classes en tant qu'attributs. La composition permet de créer des relations complexes entre les objets en les combinant de manière flexible.
				**Lien**: La classe `CheckMot` utilise les objets `OptionWord`, `OptionDate`, `AllSpecialCharacters` et `CommonSpecialCharacters`. Dans le fichier `main.py`.
- Interface : Def: Une interface est un contrat définissant un ensemble de méthodes et de signatures que les classes doivent implémenter. Une interface spécifie le comportement que les classes doivent fournir sans se soucier de l'implémentation concrète. L'utilisation d'interfaces permet de définir un contrat clair entre les différentes parties du code.
			  **Lien**: La classe `CheckMot` il y a une interface `ligne 13`.
- Méthodes et attributs statiques : Def: Les méthodes et les attributs statiques sont des membres de classe qui sont partagés par toutes les instances d'une classe. Ils sont définis au niveau de la classe plutôt qu'au niveau de l'instance. Les méthodes statiques peuvent être appelées directement sur la classe elle-même, sans avoir besoin d'instancier un objet.
				    **Lien**: Dans la classe `CheckMot`, il y a une méthode statique `removeAccents` ligne 168.
- Méthodes et attributs d'objets :**Def**: Les méthodes et les attributs d'objets sont des membres spécifiques à une instance particulière d'une classe. Chaque objet créé à partir d'une classe possède ses propres valeurs d'attributs et peut exécuter des méthodes qui manipulent ces attributs ou effectuent d'autres actions spécifiques à cet objet.
		                    **Lien**: Utilisation dans le fichier `main.py` ligne 17.
- Méthodes et attributs de classe : **Def**:  Les méthodes et les attributs de classe sont des membres de classe qui sont partagés par toutes les instances de la classe, mais ils peuvent également être accédés via la classe elle-même. Cependant, contrairement aux méthodes et attributs statiques, les méthodes et attributs de classe peuvent être hérités par les sous-classes et peuvent être modifiés par celles-ci.
				    **Lien**: Les méthodes `generate_common_special_characters()` et `generate_all_special_characters()` de dans la classe `CheckMot` sont des méthodes de classe.

Pour plus de détails sur la mise en œuvre de ces concepts, veuillez consulter le code source des fichiers correspondants.

## Comment exécuter l'application

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt Git sur votre machine.
3. Exécutez le fichier `main.py` à l'aide de la commande `python main.py`.
4. Les mots de passe générés et le nombre de combinaisons possibles seront affichés dans la console.

N'hésitez pas à explorer le code source et à apporter des modifications pour répondre à vos besoins spécifiques.

---



