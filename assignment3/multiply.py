import MapReduce
import sys

"""
Matrix multiply based on Python MapReduce Framework.
Assume the dimensions of matries are known
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Dimensions of input matries
DIM_I = 5
DIM_J = 5
DIM_K = 5

def mapper(record):
    # record = [matrix, i, j, value], type = str, int, int, int
    # key: (i, k)
    # value: (j, A[i, j]) or (j, B[j, k])
    matrix = record[0]
    mat_value = record[3]
    
    if matrix == "a":
        i = record[1]
        j = record[2]
        for k in range(DIM_K):
            key = (i, k)
            value = (j, mat_value)
            mr.emit_intermediate(key, value)
    elif matrix == "b":
        j = record[1]
        k = record[2]
        for i in range(DIM_I):
            key = (i, k)
            value = (j, mat_value)
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: (i, k)
    # value: list of multiply tuples
    # Output: (i, k, product), type = int, int, int
    list_of_values = sorted(list_of_values, key = lambda x: x[0])
    
    len_list = len(list_of_values)
    idx = 0
    product = 0
    while idx < len_list - 1:
        a_elem = list_of_values[idx]
        b_elem = list_of_values[idx + 1]
        # Check if the pair matches
        if a_elem[0] != b_elem[0]:
            idx += 1
            continue
        # Else add this pair to product
        product += int(a_elem[1]) * int(b_elem[1])
        idx += 2
        
    mr.emit((key[0], key[1], product))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
