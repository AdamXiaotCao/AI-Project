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

    # return an array of int that represents the highest point
    # for each column
    def getHeights(field):
        grid = field.field
        heights = [0] * self.width
        for row in grid:
            index = 0
            for col in row:
                if grid[row][col] == 4 and heights[index] == 0:
                    heights[index] = row
                index += 1
        return heights

    # calculate the sum of absolute height difference
    def diff_height(field):
        heights = getHeights(field)
        abs_diff_sum = 0
        for i in xrange(0, len(heights) - 1):
            abs_diff_sum += abs(heights[i] - heights[i+1])
        return abs_diff_sum

    # sum up the heights in each column
    def agg_height(field):
        heights = getHeights(field)
        agg_sum = 0
        for h in heights:
            agg_sum += h
        return agg_sum

    def complete_lines(field):

        pass

    def num_holes(field):
        pass

    def I_readiness(arg):
        pass

    def T_spin(field):
        pass

# Genetic Algorithjm
