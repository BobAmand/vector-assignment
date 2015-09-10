class ShapeException(Exception):
    pass

def shape(vector):
    shape = len(vector)
    return (shape, )

def is_equal(x, y, tolerance=0.001):
    return abs(x-y) <= tolerance

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

def vector_sum():
    '''
    No input! But needs all vectors of same length.
    Conditional on all vectors are the same length.

    '''
    # need to ripple through the parings of all vectors and compare length:
    #


def dot(v, w):
    new_sum = 0
    newmat = [(v[r] * w[r]) for r in range(len(v))]
    for n in range(len(newmat)):
        new_sum += newmat[n]
    return new_sum
    '''
    TODO: integrate the sum of the newmat list into the list comprehensives
    '''

def vector_multiply(vector, constant):
    '''
    No input in the test function.  Do not understand the error/how test is testing.
    '''
    vector_prod = [(vector[r] * constant) for r in range(len(vector))]
    return vector_prod

def vector_mean(vect_a, vect_b, vect_c):
    '''
    No input in the test function. Started with old school coding.
    '''
    sum_list =[]
    mean_list =[]
    denom = len(vect_a)
    for a in range(len(vect_a)):
        for b in range(len(vect_b)):
            for c in range(len(vect_c)):
                sum_list.append(vect_a[a] + vect_b[b] + vect_c[c])
    for i in range(len(sum_list)):
        mean_list.append(sum_list[i]/denom)
    return mean_list
    '''
    TODO translate into list conditional.
    '''
    





#
# def magnitude():
