## Vérifier le résultat

Maintenant ajoutons du code pour voir qui a gagné.

+ Tu as besoin de comparer les variables `player` et `computer` pour voir qui a gagné.

  S'ils sont identiques, alors il s'agit d'égalité, un match nul :

  ![capture d'écran](images/rps-draw.png)

+ Teste ton code en jouant le jeu a quelques reprises jusqu'à tomber sur égalité.

  Tu auras besoin de cliquer sur `Run` pour démarrer un nouveau jeu.

+ Maintenant, regardons les cas où le joeur a choisi 'r' (rock) mais que l'ordinateur a choisi autre chose.

  Si l'ordinateur a choisi 's' (scissors) alors le joueur gagne (la pierre bat ciseaux).

  Si l'ordinateur a choisi 'p' (paper) alors c'est l'ordinateur qui gagne (la feuille bat la pierre).

  Nous pouvons vérifier le choix du jouer *et* le choix de l'ordinateur en utilisant `and`.

  ![capture d'écran](images/rps-player-rock.png)

+ Ensuite, regardons les cas où le jouer choisit 'p' (paper) mais pas l'ordinateur :

  ![capture d'écran](images/rps-player-paper.png)

+ Et enfin, saurais-tu ajouter le code pour vérifier qui a gagné quand le joueur a choisi 's' (scissors) et l'ordinateur a choisi la pierre ou la feuille ?

+ Maintenant lancer et jouer le jeu pour tester ton code.

  ![capture d'écran](images/rps-play.png)

  Cliquer sur `Run` pour démarrer un nouveau jeu.
  


