
from AbstractStrategy import AbstractStrategy


class RandomStrategy(AbstractStrategy):
    def __init__(self, game):
        AbstractStrategy.__init__(self, game)
        self._actions = ['left', 'right', 'turnleft', 'turnright', 'down', 'drop']

    def choose(self):
        player = self._game.me
        field = player.field
        piece = self._game.piece  # piece object
        pieceBlocks = piece.positions()
        piecePosition = self._game.piecePosition
        nextPiece = self._game.nextPiece
        #TODO iterate over all possible moves, compute heristic
        # get the frontier of the field
        # find place to fit
        # find corresponding moves
        moves = []
        return moves



# Heuristics
    def bunpiness(field):
        pass

    def agg_height(field):
        pass

    def complete_lines(field):
        pass

    def T-spin(field):
        pass
        

# Genetic Algorithjm
