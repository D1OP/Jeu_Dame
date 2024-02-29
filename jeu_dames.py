# Importation et initialisation de la librairie pygame pour la mise en place graphique du damier
import pygame
pygame.init()


# La taille de la fenetre
WIDTH, HEIGHT = 600, 600


# Les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHESTNUT = (255, 255, 153) 


# Création de la fenêtre avec pygame
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JEU DE DAMES")


# Les variables globales
cell_size = WIDTH // 8
selected_piece = None
turn = "BLACK"


# Mise en place de la class Piece avec les fonctions draw qui gère les cellules et move qui gère le déplacement des pièces
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def draw(self):
        radius = cell_size // 2 - 5
        pygame.draw.circle(win, self.color, (self.col * cell_size + cell_size // 2, self.row * cell_size + cell_size // 2), radius)

    def move(self, new_row, new_col):
        board[self.row][self.col], board[new_row][new_col] = None, self
        self.row, self.col = new_row, new_col

board = [
    [Piece(0, 0, "BLACK"), " ", Piece(0, 2, "BLACK"), " ", Piece(0, 4, "BLACK"), " ", Piece(0, 6, "BLACK"), " "],
    [" ", Piece(1, 1, "BLACK"), " ", Piece(1, 3, "BLACK"), " ", Piece(1, 5, "BLACK"), " ", Piece(1, 7, "BLACK")],
    [Piece(2, 0, "BLACK"), " ", Piece(2, 2, "BLACK"), " ", Piece(2, 4, "BLACK"), " ", Piece(2, 6, "BLACK"), " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", Piece(5, 1, "CHESTNUT"), " ", Piece(5, 3, "CHESTNUT"), " ", Piece(5, 5, "CHESTNUT"), " ", Piece(5, 7, "CHESTNUT")],
    [Piece(6, 0, "CHESTNUT"), " ", Piece(6, 2, "CHESTNUT"), " ", Piece(6, 4, "CHESTNUT"), " ", Piece(6, 6, "CHESTNUT"), " "],
    [" ", Piece(7, 1, "CHESTNUT"), " ", Piece(7, 3, "CHESTNUT"), " ", Piece(7, 5, "CHESTNUT"), " ", Piece(7, 7, "CHESTNUT")]
]


# Mise en place du damier
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(win, color, (col * cell_size, row * cell_size, cell_size, cell_size))
 

# Mise en place des pièces
def draw_pieces():
    for row in range(8):
        for col in range(8):
            if board[row][col] != " ":
                color = BLACK if board[row][col] == "BLACK" else CHESTNUT
                piece = Piece(row, col, color)
                piece.draw()
                
               
# Récupérer les coordonnées de la cellule après click
def get_cell_from_mouse(pos):
    x, y = pos
    col = x // cell_size
    row = y // cell_size
    return row, col


# Vérifier si le mouvement est valide que ça soit pour une pièce simple ou un dame et leur sens de déplacement
def is_valid_move(piece, new_row, new_col):
    if new_row < 0 or new_row > 7 or new_col < 0 or new_col > 7:
        return False
    if board[new_row][new_col] is not None:
        return False
    
    if isinstance(piece, Piece) and piece.color == "BLACK" and new_row > piece.row:
        if piece.color == "BLACK" and new_row > piece.row:
            if new_row - piece.row == abs(new_col - piece.col):
                for i in range(1, new_row - piece.row):
                    if board[piece.row + i][piece.col + (new_col - piece.col) * i // abs(new_col - piece.col)] is not None:
                        return False
                return True
        elif isinstance(piece, Piece):
            if piece.row - new_row == abs(new_col - piece.col) and abs(new_col - piece.col) > 0:
                for i in range(1, piece.row - new_row):
                    if board[piece.row - i][piece.col + (new_col - piece.col) * i // abs(new_col - piece.col)] is not None:
                        return False
                return True
    return False    


# La fonction main avec la gestion des pièces et des tours de jeu
def main():
    global selected_piece, turn
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_cell_from_mouse(pygame.mouse.get_pos())
                if isinstance(board[row][col], Piece) and board[row][col].color == turn:
                    selected_piece = board[row][col]
                elif selected_piece:
                    new_row, new_col = get_cell_from_mouse(pygame.mouse.get_pos())
                    if is_valid_move(selected_piece, new_row, new_col):
                        selected_piece.move(new_row, new_col)
                        if turn == "BLACK":
                            turn = "CHESTNUT"
                        else:
                            turn = "BLACK"
                    selected_piece = None
        
        win.fill(WHITE)
        draw_board()
        draw_pieces()
        pygame.display.update()

    
if __name__ == "__main__":
    main()