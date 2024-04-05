# Définition des constantes pour les symboles X et O, ainsi que pour une case vide
SYMBOL_X = 'X'
SYMBOL_O = 'O'
EMPTY_CELL = ' '

# Fonction pour afficher le plateau de jeu
def display_board(board):
    """
    Affiche le plateau de jeu.
    """
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Fonction pour vérifier si un joueur a gagné
def check_win(board, player):
    """
    Vérifie si le joueur a gagné en vérifiant les lignes, colonnes et diagonales du plateau.
    """
    # Vérification des lignes et colonnes
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True

    # Vérification des diagonales
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Fonction pour vérifier si le plateau est rempli (match nul)
def check_board_full(board):
    """
    Vérifie si le plateau est rempli, ce qui signifie qu'il n'y a pas de cases vides.
    """
    for row in board:
        if EMPTY_CELL in row:
            return False
    return True

# Fonction pour évaluer le score du plateau pour le joueur actuel
def evaluate_board(board):
    """
    Évalue le score du plateau pour le joueur actuel.
    """
    if check_win(board, SYMBOL_X):
        return 1
    elif check_win(board, SYMBOL_O):
        return -1
    elif check_board_full(board):
        return 0

# Fonction pour implémenter l'algorithme Minimax
def minimax(board, depth, is_maximizing):
    """
    Implémente l'algorithme Minimax pour évaluer les coups possibles et choisir le meilleur coup.
    """
    score = evaluate_board(board)

    if score == 1 or score == -1 or score == 0:
        return score

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = SYMBOL_X
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY_CELL
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = SYMBOL_O
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY_CELL
                    best_score = min(best_score, score)
        return best_score

# Fonction pour trouver le meilleur coup pour l'ordinateur
def get_best_move(board):
    """
    Trouve le meilleur coup pour l'ordinateur en utilisant l'algorithme Minimax.
    """
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_CELL:
                board[i][j] = SYMBOL_X
                score = minimax(board, 0, False)
                board[i][j] = EMPTY_CELL
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Fonction principale pour jouer au jeu
def play_tictactoe():
    """
    Fonction principale pour jouer au jeu de Tic Tac Toe.
    """
    board = [[EMPTY_CELL]*3 for _ in range(3)]
    current_player = SYMBOL_X

    while True:
        display_board(board)
        if current_player == SYMBOL_X:
            row, col = get_best_move(board)
            board[row][col] = SYMBOL_X
        else:
            while True:
                row = int(input("Entrez la ligne (0, 1, 2): "))
                col = int(input("Entrez la colonne (0, 1, 2): "))
                if board[row][col] == EMPTY_CELL:
                    board[row][col] = SYMBOL_O
                    break
                else:
                    print("Case déjà occupée. Veuillez choisir une autre case.")

        if check_win(board, current_player):
            display_board(board)
            print(f"Le joueur {current_player} a gagné !")
            break
        elif check_board_full(board):
            display_board(board)
            print("Match nul !")
            break

        current_player = SYMBOL_O if current_player == SYMBOL_X else SYMBOL_X

# Appel de la fonction principale pour jouer au jeu
play_tictactoe()
