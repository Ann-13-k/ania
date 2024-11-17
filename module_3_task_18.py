from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def get_possible_moves(self):
        pass
class Pawn(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white":
            return [(1, 1), (1, 2)]
        else:
            return [(-1, 1), (-1, 2)]
    def __str__(self):
        return f"Пешка: {self.color}"
class Rook(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white":
            return [(1, 1), (8, 1)]
        else:
            return [(1, 8), (8, 8)]
    def __str__(self):
        return f"Ладья: {self.color}"
class Bishop(ChessPiece):
    def get_possible_moves(self):
        if self.color == "white":
            return [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        else:
            return [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    def __str__(self):
        return f"Слон: {self.color}"

pawn = Pawn("black")
print(pawn)
print(f"Возможные ходы для черной пешки: {pawn.get_possible_moves()}")
pawn = Pawn("white")
print(pawn)
print(f"Возможные ходы для белой пешки: {pawn.get_possible_moves()}\n")

rook = Rook("black")
print(rook)
print(f"Возможные ходы для черной ладьи: {rook.get_possible_moves()}")
rook = Rook("white")
print(rook)
print(f"Возможные ходы для белой ладьи: {rook.get_possible_moves()}\n")

bishop = Bishop("black")
print(bishop)
print(f"Возможные ходы для черного слона: {bishop.get_possible_moves()}")
bishop = Bishop("white")
print(bishop)
print(f"Возможные ходы для белого слона: {bishop.get_possible_moves()}")