from ..Piece import Piece

class King(Piece):
    def __str__(self):
        return 'k' if self.color == 'black' else 'K'
    
    def is_king(self):
        return True