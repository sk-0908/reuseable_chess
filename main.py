# main.py
from package.game.Chess_Game import ChessGame

# チェスゲームの開始
if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play()