from ..Piece import Piece

class Queen(Piece):
    def __str__(self):
        return 'q' if self.color == 'black' else 'Q'

    def is_king(self):
        return False