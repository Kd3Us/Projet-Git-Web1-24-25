# Liste pour stocker les todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    if not todos:
        print("Aucun todo à afficher.")
        return
    print("\n=== Liste des todos ===")
    for index, todo in enumerate(todos):
        print(f"{index + 1}: {todo['titre']} - Statut: {todo['statut']}")
    print("========================")

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append({'titre': titre, 'statut': 'À faire'})
    print(f'Todo "{titre}" créé avec succès.')

# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if index < 0 or index >= len(todos):
            print("Numéro de todo invalide.")
            return

        statut = todos[index]['statut']
        if statut == 'À faire':
            todos[index]['statut'] = 'Fait'
        elif statut == 'Fait':
            # Erreur volontaire : mettre le statut en "À fair" au lieu de "À faire"
            todos[index]['statut'] = 'À fair'
        print(f'Statut du todo "{todos[index]["titre"]}" modifié en "{todos[index]["statut"]}".')
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")

# Fonction pour supprimer un todo
def supprimer_todo():
    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo à supprimer : ")) - 1
        if index < 0 or index >= len(todos):
            print("Numéro de todo invalide.")
            return

        confirmation = input(f"Êtes-vous sûr de vouloir supprimer le todo '{todos[index]['titre']}' ? (o/n) : ")
        if confirmation.lower() == 'o':
            removed_todo = todos.pop(index)
            print(f'Todo "{removed_todo["titre"]}" supprimé avec succès.')
        else:
            print("Suppression annulée.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro.")

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