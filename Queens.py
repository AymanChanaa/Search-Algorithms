class Etat:
    def __init__(self, queens, n):
        self.queens = queens  # Position des reines sur l'échiquier
        self.n = n  # Taille de l'échiquier (n x n)

    # Vérifie si l'état actuel est valide (respecter les règles d'échecs)
    def validation(self):
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                # Vérifie si deux reines sont sur la même colonne
                if self.queens[i] == self.queens[j]:
                    return False
                # Vérifie si deux reines sont sur la même diagonale
                if abs(self.queens[i] - self.queens[j]) == j - i:
                    return False
        return True

    # Retourne une représentation de l'état sous forme de chaîne de caractères
    def __str__(self):
        board = []
        for i in range(self.n):
            row = ['-'] * self.n
            # Marque la position de la reine sur l'échiquier
            row[self.queens[i]] = 'Q'
            board.append(' '.join(row))
        return '\n'.join(board)

# breadth_first_search
# Implémentation de la recherche en largeur d'abord
def parcours_par_largeur(n):
    frontiere = [Etat([], n)]  # Commence avec un état vide
    while frontiere:
        state = frontiere.pop(0)  # Prend le premier état de la frontière FIFO
        if len(state.queens) == n:  # Vérifie si toutes les reines ont été placées
            return state
        else:
            for col in range(n):  # Pour chaque colonne
                if col not in state.queens:  # Vérifie si la colonne est disponible pour placer une reine
                    # Crée un nouvel état en ajoutant une reine dans cette colonne
                    tmp = Etat(state.queens + [col], n)
                    if tmp.validation():  # Vérifie si le nouvel état est valide
                        # Ajoute le nouvel état à la frontière
                        frontiere.append(tmp)

# depth_first_search
# Implémentation de la recherche en profondeur d'abord
def parcours_par_profondeur(n):
    pile = [Etat([], n)]
    while pile:
        state = pile.pop()  # Prend le dernier état de la pile LIFO
        if len(state.queens) == n:  # Vérifie si toutes les reines ont été placées
            return state
        else:
            for col in range(n):  # Pour chaque colonne
                if col not in state.queens:  # Vérifie si la colonne est disponible pour placer une reine
                    # Crée un nouvel état en ajoutant une reine dans cette colonne
                    tmp = Etat(state.queens + [col], n)
                    if tmp.validation():  # Vérifie si le nouvel état est valide
                        pile.append(tmp)  # Ajoute le nouvel état à la pile

# Affiche la solution trouvée
def print_solution(solution):
    if solution:
        print(solution)
    else:
        print("Pas de solution trouvée.")


n = 8
bfs_solution = parcours_par_largeur(n)
print("Solution par largeur d'abord:")
print_solution(bfs_solution)

dfs_solution = parcours_par_profondeur(n)
print("\nSolution par profondeur d'abord:")
print_solution(dfs_solution)
