class AbstractStrategy:
    def __init__(self, game):
        self._game = game

    def choose(self):
        player = self._game.me
        field = player.field
        piece = self._game.piece  # piece object
        pieceBlocks = piece.positions()
        piecePosition = self._game.piecePosition
        nextPiece = self._game.nextPiece

        # get the frontier of the field
        # find place to fit
        # find corresponding moves
        moves = []
        return moves