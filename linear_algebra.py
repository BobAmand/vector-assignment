from math import sqrt


class ShapeException(Exception):
    pass
bad_shape = "The vectors must be the same size."


def shape(vec):
    return(len(vec), )


def is_equal(x, y, tolerance=0.001):
    return abs(x-y) <= tolerance


def vector_add(v, w):
    if shape(v) != shape(w):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    '''
    Adds two lists by aligned indexes:
    old way first, list comprehensive second.
    '''
    # newmat = []
    # for r in range(len(v)):
    #     newmat.append(v[r] + w[r])
    # return newmat
    newmat = [(v[r] + w[r]) for r in range(len(v))]
    return newmat


def vector_sub(v, w):
    if shape(v) != shape(w):
        raise ShapeException("Shape rule: the vectors must be the same size.")
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


def vector_sum(*args):
    lst = [len(x) for x in args]
    if any(x != lst[0] for x in lst):
        raise ShapeException("Shape rule: the vectors must be the same size.")
    else:
        return [sum(x) for x in zip(*args)]
'''
my initial:
    ret = [0] * len(args[0])  # initialize with series of zeros
    for x in args:
        ret = vector_add(ret, x)
    return ret
'''
'''
alternate:
    return [sum(x) for x in zip(*args)]

    res [len(x) for x in args]          #ShapeException check
    if any(x != res[0] for x in res):
        raise ShapeException

    for r in x != res[0] for x in res:  #ShapeException check
        if r == True:
            raise ShapeException

            another alternative Jon's:
            if len(args) == 2:
                check_shape(args[0], args[1])
                return vector_add(args[0], args[1])
            else:
                return vector_add(args[0], vector_sum(*args(1:]))

'''
#  My initial effort:
'''
# sum_list =[]
# for a in range(len(vect_a)):
#     for b in range(len(vect_b)):
#         for c in range(len(vect_c)):
#             for d in range(len)vect_d)):
#                 sum_list.append(vect_a[a] + vect_b[b] + vect_c[c] + vect_d[d])
# return sum_list
'''
#    TODO translate into list conditional.


def dot(v, w):
    if len(v) != len(w):
        raise ShapeException("ShapeException: lists are not the same size.")
    else:
        newmat = [(v[r] * w[r]) for r in range(len(v))]  # list of products
        return sum(newmat)    # sums list contents


def vector_multiply(vec, sca):   # multiply by a constant (scalar)
    return [sca * x for x in vec]
'''
    Assume vector, constant are being passed in.
    Initial effort:

    vector_prod = [(vector[r] * constant) for r in range(len(vector))]
    return vector_prod
'''


def vector_mean(*args):
    return([v/len([x for x in args]) for v in vector_sum(*[x for x in args])])

    # num = len(args)         # how many tuples in the args list
    # vector = vector_sum(*args)  # unpacks the args.
    # return vector/num

    '''
    Alternative:
    return([v/len([x for x in args]) for v in vector_sum(*[x for x in args])])
     - glenn hurley solution!

    Started with old school coding.
    Assumed (vect_a, vect_b, vect_c) are being passed in.
    My initial effort:

    sum_list = []
    mean_list = []
    denom = len(vect_a)
    for a in range(len(vect_a)):
        for b in range(len(vect_b)):
            for c in range(len(vect_c)):
                sum_list.append(vect_a[a] + vect_b[b] + vect_c[c])
    for i in range(len(sum_list)):
        mean_list.append(sum_list[i]/denom)
    return mean_list
    '''


def magnitude(vec):
    return sqrt(sum([x**2 for x in vec]))
    '''
    My initial effort:
    return math.sqrt(dot(vec, vec))

    magnitude = [(vect_a[i]**2 + vect_b[i]**2)**0.5 for i in range(len(vect_a))]
    return magnitude
    '''
