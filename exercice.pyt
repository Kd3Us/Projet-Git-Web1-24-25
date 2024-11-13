# Fonction pour lister les todos - à réaliser
def lister_todos():
 print('Fonctionnalité "lister les todos" à venir')

# Fonction pour créer un todo - à réaliser
def creer_todo():
 print('Fonctionnalité "créer un todo" à venir')

# Fonction pour modifier le statut d'un todo - à réaliser
def modifier_statut_todo():
 print('Fonctionnalité "modifier le statut d\'un todo" à venir')

# Fonction pour supprimer un todo - à réaliser
def supprimer_todo():
 print('Fonctionnalité "supprimer un todo" à venir')

# Menu principal
choix = ''
while choix != 'q':

 # Affichage des choix
 print('\n==== Menu principal ====')
 print('1: Lister les todos')
 print('2: Créer un todo')
 print('3: Changer le statut d\'un todo')
 print('4: Supprimer un todo')
 print('q: quitter')
 print('========================')

 # Actions suivant le choix
 choix = input('=> Choix : ')
 match choix:
    case '1': lister_todos()
    case '2': creer_todo()
    case '3': modifier_statut_todo()
    case '4': supprimer_todo()
    case 'q': print('Au revoir')
    case _: print('Choix invalide')