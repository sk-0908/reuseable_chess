from ..Piece import Piece

class Bishop(Piece):
    def __str__(self):
        return 'b' if self.color == 'black' else 'B'

    def is_king(self):
        return False