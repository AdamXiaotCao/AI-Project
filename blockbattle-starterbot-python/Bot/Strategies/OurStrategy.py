from AbstractStrategy import AbstractStrategy


class OurStrategy(AbstractStrategy):
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

        #TODO iterate over all possible moves, compute heuristic

        # get the frontier of the field
        # find place to fit
        # find corresponding moves
        moves = []
        return moves



# Heuristics
    def bumpiness(field):
        pass

    def agg_height(field):
        pass

    def complete_lines(field):
        count = 0
        for layer in field:
            if layer.__contains__(0):
                continue
            else:
                count += 1
        return count

    def num_holes(field):
        count = 0
        for i in range(1, len(field)-1):
            for j in range(1, len(field[i])-1):
                if field[i-1][j] == 0 or field[i][j-1] == 0 or field[i][j+1] == 0:
                    continue
                else:
                    count += 1
        return count

    def I_readiness(arg):
        pass

    def T_spin(field):
        pass

# Genetic Algorithjm
