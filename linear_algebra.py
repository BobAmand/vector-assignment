class ShapeException(Exception):
    pass

def shape(vector):
    shape = len(vector)
    return (shape, )

# v = [1, 3, 0]
# w = [0, 2, 4]

def vector_add(v, w):
    '''
    Adds two lists by aligned indexes:
    old way first, list comprehensive second.
    '''
    # newmat = []
    # for r in range(len(v)):
    #     newmat.append(v[r] + w[r])
    # return newmat
    newmat = [(v[r]+ w[r]) for r in range(len(v))]
    return newmat

def vector_sub(v, w):
    '''
    Subtracts two lists by aligned indexes:
    old way first, list comprehensive second.
    '''
    # newmat = []
    # for r in range(len(v)):
    #     newmat.append(v[r] - w[r])
    # return newmat
    newmat = [(v[r] - w[r]) for r in range(len(v))]
    return newmat
