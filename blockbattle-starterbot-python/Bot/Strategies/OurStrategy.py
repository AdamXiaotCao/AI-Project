from AbstractStrategy import AbstractStrategy
import math, copy

class OurStrategy(AbstractStrategy):
    def __init__(self, game):
        AbstractStrategy.__init__(self, game)
        self._actions = ['left', 'right', 'turnleft', 'turnright', 'down', 'drop']
        self.a = 1
        self.b = 1
        self.c = 1
        self.d = 1

    def choose(self):
        player = self._game.me
        field = player.field
        piece = self._game.piece  # piece object
        pieceBlocks = piece.positions()
        piecePosition = self._game.piecePosition
        nextPiece = self._game.nextPiece
        grid = field.field

        best_fit = None
        max_score = - math.inf
        #TODO iterate over all possible moves, compute heuristic
        for i in range(1, grid.height-1):
            for j in range(1, grid.width-1):
                if isOnGround(piecePosition, field):
                    tmp_score = self.getScore(field.projectPieceDown(piece, (i, j)))
                    if tmp_score > max_score:
                        max_score = tmp_score
                        best_fit = (i, j)

        # given the best fit, find corresponding moves

        moves = []
        return moves

    def getScore(self, field):
        return self.a * self.agg_height(field) + self.b * self.complete_lines(field) \
               + self.c * self.num_holes(field) + self.d * self.T_spin_readiness(field)

    # return an array of int that represents the highest point
    # for each column
    def getHeights(self, field):
        grid = field.field
        heights = [0] * len(grid[0])
        for row in grid:
            index = 0
            for col in row:
                if grid[row][col] == 4 and heights[index] == 0:
                    heights[index] = row
                index += 1
        heights = map(lambda x: len(grid) - x, heights)
        return heights

    # calculate the sum of absolute height difference
    def diff_height(self, field):
        heights = self.getHeights(field)
        abs_diff_sum = 0
        for i in xrange(0, len(heights) - 1):
            abs_diff_sum += abs(heights[i] - heights[i+1])
        return abs_diff_sum

    # sum up the heights in each column
    def agg_height(self, field):
        heights = self.getHeights(field)
        agg_sum = 0
        for h in heights:
            agg_sum += h
        return agg_sum

    def complete_lines(self, field):
        grid = field.field
        count = 0
        for layer in grid:
            if layer.__contains__(0):
                continue
            else:
                count += 1
        return count

    def num_holes(self, field):
        grid = field.field
        count = 0
        for i in range(1, grid.height-1):
            for j in range(1, grid.width-1):
                if grid[i-1][j] == 0 or grid[i-1][j-1] == 0 or grid[i-1][j+1] == 0:
                    continue
                else:
                    count += 1
        return count


    def T_spin_readiness(self, field):
        # This heuristic is designed for leaving a T-spin block
        # In other words, 3 out of 4 corners of the T-shape bounding box
        # are occupied with blocks in the field

        # Find the top blocks
        for x in xrange(1,field.width-1):
            for y in xrange(1,field.height-1):
                if field.field[y][x] > 1:
                    if (field.field[y-1][x-1] > 1 and
                        field.field[y-1][x+1] > 1 and
                        field.field[y-2][x-1] == 0 and
                        field.field[y-2][x+1] == 0 and
                        (bool(field.field[y-3][x-1]) ^
                         bool(field.field[y-3][x+1]))):
                        return 10
        return 0

    def T_spinning(field):

        pass



# Genetic Algorithm

def offsetPiece(piecePositions, offset):
        piece = copy.deepcopy(piecePositions)
        for pos in piece:
            pos[0] += offset[0]
            pos[1] += offset[1]
        return piece  # return type: piecePositions


def checkIfPieceFits(field, piecePositions):
        for x,y in piecePositions:
            if 0 <= x < field.width and 0 <= y < field.height:
                if field.field[y][x] > 1:
                    return False
            else:
                return False
        return True


def isOnGround(piecePositions, field):
    return checkIfPieceFits(field, piecePositions) and \
           (not checkIfPieceFits(field, offsetPiece(piecePositions, (0, 1))))
# Genetic Algorithm
