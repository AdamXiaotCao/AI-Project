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

    def num_holes(field):
        pass

    def I_readiness(field):
        # This heuristic is designed for leaving a single blank column for
        # I piece to get combo points
        
        pass

    def T_spin_readiness(self, field):
        # This heuristic is designed for leaving a T-spin block
        # In other words, 3 out of 4 corners of the T-shape bounding box
        # are occupied with blocks in the field

        # Find the top blocks
        for x in xrange(1,field.width-1):
            for y in xrange(1,field.height-1):
                if field.field[y][x] > 1:
                    if (field.field[y-1][x-1] > 1 and
                        filed.field[y-1][x+1] > 1 and
                        field.field[y-2][x-1] == 0and
                        field.field[y-2][x+1] == 0 and
                        (bool(field.field[y-3][x-1]) ^
                         bool(field.field[y-3][x+1]))):
                        return 10
        return 0
    
    def T_spinning(field):
        
        pass


# Genetic Algorithjm
