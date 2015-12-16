import random

# Genetic ALgorithm

# Generate population
# pop_size is the size of population interested
# sign_vec is a vector with the same dimension of the
# weight vector and indicating the sign of each entry of
# the weight vector
def pop_gen(pop_size, sign_vec):
    pop = [0]*pop_size
    for i in xrange(pop_size):
        w = vec_gen(sign_vec)
        pop[i] = w
    return pop

def vec_gen(sign_vec):
    dim = len(sign_vec)
    w = [0]*dim
    for i in xrange(dim):
        w[i] = random.random()*sign_vec[i]
    return normed(w)

def normed(vector):
    norm = 0
    for c in vector:
        norm += c**2
    norm = norm**0.5
    for c in vector:
        c = c/norm
    return vector

#print pop_gen(5,[1,-1,1])

# Evaluate fitness
# pop is the list of all vectors
# num_pieces is number of poeces assigned to each game
# num_game is the number of games for the bot to play
def evaluate(pop,num_games):
    score_sheet = {}
    print "generating score sheet..."
    for i in xrange(len(pop)):
        score = 0
        for n in xrange(num_games):
            score += f_eval(pop[i],pop)/float(num_games)
        score_sheet[(score,i)] = pop[i]
    print "score sheet completed!"
    return score_sheet

# f_eval
# round robin style
# w is the candidate to be evaluated
# pop is the rest of other candidates
# make w battle with all other vectors in pop and record num of wins
def f_eval(w, pop):
    score = 0
    for wi in pop:
        score += ((w[0]+w[1])**2 < (wi[0]+wi[1])**2)*1
    return score

# Cross_over
# score_sheet is a dictionary with format of {(score,i):w}
# mutation is a very small amount that w can mutate
# elim is the number of vectors to be eliminated for each generation
def cross_over(score_sheet,mutation,elim):
    sorted_keys = sorted(score_sheet.keys())
    score_copy = score_sheet.copy()
    print "starting cross over elimination..."
    for i in xrange(elim):
        pick1 = random.randint(0,len(score_sheet)/10*9)
        pick2 = random.randint(0,len(score_sheet)/10*9)
        key1 = max(score_sheet.keys()[pick1:(pick1+len(score_sheet)/10)])
        key2 = max(score_sheet.keys()[pick2:(pick2+len(score_sheet)/10)])
        parent1 = score_sheet[key1]
        parent2 = score_sheet[key2]
        baby = avg(score_sheet[key1],score_sheet[key2],key1[0],key2[0])

        # mutation
        baby[random.randint(0,len(baby)-1)]+random.randint(-1,1)*mutation
        baby = normed(baby)
        score_copy[sorted_keys[i]] = baby
    print "elimination completed!"
    return score_copy.values()

def avg(vec1, vec2, wt1, wt2):
    result = [0]*len(vec1)
    for i in xrange(len(vec1)):
        result[i] = (wt1*vec1[i]+wt2*vec2[i])/float(wt1+wt2)
    return result

# Run
def ga(generations, num_games, pop_size, sign_vec, mutation, elim):
    pop = pop_gen(pop_size, sign_vec)
    for i in xrange(generations):
        score_sheet = evaluate(pop,num_games)
        new_pop = cross_over(score_sheet, mutation, elim)
        pop = new_pop
    return pop[0]

print ga(100,10,100,[1,-1,1],0.05,30)
    
