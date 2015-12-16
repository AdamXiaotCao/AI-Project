from AbstractStrategy import AbstractStrategy
import math, copy, sys

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

        # best_fit = None
        max_score = -sys.maxint - 1
        best_moves = []
        counter = 0
        #TODO iterate over all possible moves, compute heuristic

        for j in range(1, field.width/2):
            current_moves = []
            for i in range(1, field.height-1):
                for turn in range(0,4):
                    counter += 1
                    # print "checking is on ground ", counter
                    if isOnGround(piece.positions(), field,i, j):
                        tmp_score = self.getScore(field.projectPieceDown(piece, (i, j)))
                        print "tmp_score is ", tmp_score
                        if tmp_score > max_score:
                            max_score = tmp_score
                            best_moves = current_moves
                            # best_fit = (i, j)
                        break
                    if turn != 0:
                        turn_result = piece.turnRight()
                        if not turn_result:
                            break
                        current_moves += ["turnright"]
                        piecePosition = piece.positions()
                current_moves += ['down']
            current_moves += ['right']
        # given the best fit, find corresponding moves
        moves = best_moves
        # print moves
        moves += ['drop']
        return moves

    def getScore(self, field):
        agg_h = self.agg_height(field)
        com_l = self.complete_lines(field)
        num_h = self.num_holes(field)
        t_spin_r = self.T_spin_readiness(field)
        print("----------")
        print("getScore result")
        print "agg_h: ", agg_h, "\n com_l: ", com_l, "\nnum_h: ", num_h, "\nt_spin_r: ", t_spin_r
        print("----------")
        return self.a * self.agg_height(field) + self.b * self.complete_lines(field) \
               + self.c * self.num_holes(field) + self.d * self.T_spin_readiness(field)

    # return an array of int that represents the highest point
    # for each column
    def getHeights(self, field):
        heights = [0] * len(field[0])
        num_col = len(field[0])
        num_row = len(field)
        for col in range(0,num_col):
            for row in range(0, num_row):
                if(field[row][col] == 4):
                    heights[col] = num_row - row
                    break
        #
        # for row in field:
        #     row_num = 0
        #     index = 0
        #     for col in row:
        #         if row[col] == 4 and heights[index] == 0:
        #             heights[index] =row_num
        #             break
        #         index += 1
        #     row_num += 1
        # heights = map(lambda x: len(field) - x, heights)
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
        printField(field)


        heights = self.getHeights(field)
        print("---------heights----------")
        print(heights)
        print("-----------End------------")
        agg_sum = 0
        for h in heights:
            agg_sum += h
        return agg_sum

    def complete_lines(self, field):
        count = 0
        for layer in field:
            if layer.__contains__(0):
                continue
            else:
                count += 1
        return count

    def num_holes(self, field):
        count = 0
        for i in range(1, len(field)-1):
            for j in range(1, len(field[0])-1):
                if field[i-1][j] == 0 or field[i-1][j-1] == 0 or field[i-1][j+1] == 0:
                    continue
                else:
                    count += 1
        return count


    def T_spin_readiness(self, field):
        # This heuristic is designed for leaving a T-spin block
        # In other words, 3 out of 4 corners of the T-shape bounding box
        # are occupied with blocks in the field

        # Find the top blocks
        for x in xrange(1,len(field[0])-1):
            for y in xrange(1,len(field)-1):
                if field[y][x] > 1:
                    if (field[y-1][x-1] > 1 and
                        field[y-1][x+1] > 1 and
                        field[y-2][x-1] == 0 and
                        field[y-2][x+1] == 0 and
                        (bool(field[y-3][x-1]) ^
                         bool(field[y-3][x+1]))):
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


def isOnGround(piecePositions, field, i, j):
    result = (field.fitPiece(piecePositions, (i,j)) is not None) and (field.fitPiece(piecePositions,(i+1,j)) is None)
    # result = checkIfPieceFits(field, piecePositions) and \
        #    (not checkIfPieceFits(field, offsetPiece(piecePositions, (0, 1))))
    print "is on ground result is ", result
    return result

def printField(field):
    print("-------Field--------")
    for row in range(0,len(field)):
        output = ""
        for col in range(0, len(field[0])):
            output += str(field[row][col])
        output+="\n"
        print(output)
    print("---------End--------")
# settings timebank 10000
# settings time_per_move 500
# settings player_names player1,player2
# settings your_bot player1
# settings field_height 20
# settings field_width 10
# update game round 1
# update game this_piece_type O
# update game next_piece_type I
# update game this_piece_position 4,-1
# update player1 row_points 0
# update player1 combo 0
# update player1 skips 0
# update player1 field 0,0,0,0,1,1,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0
# update player2 row_points 0
# update player2 combo 0
# update player2 field 0,0,0,0,1,1,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,0,0,0,0
# action moves 10000

# Genetic Algorithm
