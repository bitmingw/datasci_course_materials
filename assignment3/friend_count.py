import MapReduce
import sys

"""
Friend count based on Python MapReduce Framework.
In this case the social network is a directed graph.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = [personA, personB], type = str, str
    # B is A's friend, but A is NOT B's friend
    # key: personA
    # value: personA's friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: personA
    # value: list of personA's friends
    # Output: (person, friend_count)
    friend_list = []
    friend_count = 0
    for friend in list_of_values:
        if friend not in friend_list:
            friend_list.append(friend)
            friend_count += 1
    mr.emit((key, friend_count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
