from ..Piece import Piece

class Knight(Piece):
    def __str__(self):
        return 'n' if self.color == 'black' else 'N'

    def is_king(self):
        return False