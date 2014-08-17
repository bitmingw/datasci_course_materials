import MapReduce
import sys

"""
Non-symmetric friend check based on Python MapReduce Framework.
In this case the social network is a directed graph.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = [personA, personB], type = str, str
    # B is A's friend, but A is NOT B's friend
    # key: (personA, personB) and (personB, personA)
    # value: 1 and -1
    key = (record[0], record[1])
    value = 1
    mr.emit_intermediate(key, value)
    key = (record[1], record[0])
    value = -1
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person friend pair, in two orders
    # value: 1 or -1
    # Output: asymmetric relation, 
    # i.e. (personA, personB) and (personB, personA)
    # if A is NOT B's friend
    direction = sum(list_of_values)
    if direction != 0:
        mr.emit(key)
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
