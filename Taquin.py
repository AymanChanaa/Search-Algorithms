class Node:
    def __init__(self, state, level, fval):
        """
        Initialise un nœud avec l'état actuel, le niveau de profondeur et la valeur de la fonction f.
        """
        self.state = state  # État actuel du puzzle
        self.level = level  # Niveau de profondeur dans l'arborescence
        self.fval = fval  # Valeur de la fonction f (coût total)

    def generate_child(self):
        """
        Génère les enfants possibles à partir de l'état actuel en effectuant les mouvements valides.
        """
        x, y = self.find(
            self.state, '_')  # Trouve les coordonnées de la case vide
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y],
                    [x + 1, y]]  # Déplacements possibles
        children = []
        for i in val_list:
            child_state = self.move_blank(
                self.state, x, y, i[0], i[1])  # Effectue un mouvement
            if child_state is not None:
                child_node = Node(child_state, self.level + 1, 0)
                children.append(child_node)
        return children

    def move_blank(self, puzzle, x1, y1, x2, y2):
        """
        Déplace la case vide (_), si possible, vers la position spécifiée.
        """
        if x2 >= 0 and x2 < len(self.state) and y2 >= 0 and y2 < len(self.state):
            temp_puzzle = self.copy_puzzle(puzzle)
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:
            return None

    def copy_puzzle(self, root):
        """
        Effectue une copie du puzzle.
        """
        temp = []
        for row in root:
            temp_row = []
            for element in row:
                temp_row.append(element)
            temp.append(temp_row)
        return temp

    def find(self, puzzle, x):
        """
        Trouve les coordonnées de la case spécifiée dans le puzzle.
        """
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if puzzle[i][j] == x:
                    return i, j


class PuzzleSolver:
    def __init__(self, size):
        """
        Initialise le solveur de puzzle avec la taille du puzzle.
        """
        self.size = size
        self.open_list = []  # Liste des nœuds à explorer
        self.closed_list = []  # Liste des nœuds explorés

    def accept_puzzle(self):
        """
        Demande à l'utilisateur de saisir le puzzle.
        """
        puzzle = []
        print("Enter the puzzle matrix:")
        for i in range(0, self.size):
            row = input().split(" ")
            puzzle.append(row)
        return puzzle

    def f(self, current, goal):
        """
        Fonction d'évaluation f(n) = h(n) + g(n).
        """
        return self.h(current.state, goal) + current.level

    def h(self, current, goal):
        """
        Fonction heuristique qui estime le coût restant pour atteindre l'état final.
        """
        temp = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if current[i][j] != goal[i][j] and current[i][j] != '_':
                    temp += 1
        return temp

    def solve(self):
        """
        Résout le puzzle en utilisant l'algorithme A*.
        """
        print("Enter the start state matrix:")
        start_state = self.accept_puzzle()
        print("Enter the goal state matrix:")
        goal_state = self.accept_puzzle()

        start_node = Node(start_state, 0, 0)
        start_node.fval = self.f(start_node, goal_state)

        self.open_list.append(start_node)

        while True:
            current_node = self.open_list[0]

            print("Current state:")
            for row in current_node.state:
                for element in row:
                    print(element, end=" ")
                print("")

            if self.h(current_node.state, goal_state) == 0:
                print("Puzzle solved!")
                break

            for child in current_node.generate_child():
                child.fval = self.f(child, goal_state)
                self.open_list.append(child)

            self.closed_list.append(current_node)
            del self.open_list[0]

            self.open_list.sort(key=lambda x: x.fval, reverse=False)


solver = PuzzleSolver(3)
solver.solve()
