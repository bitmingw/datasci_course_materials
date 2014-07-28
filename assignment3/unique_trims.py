import MapReduce
import sys

"""
Unique DNA sequence trimmer based on Python MapReduce Framework.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = [sequence_id, nucleotides], type = str, str
    # key: trimmed nucleotides
    # value: nucleotides
    seq_len = len(record[1])
    key = record[1][0:(seq_len - 10)]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: trimmed nucleotides
    # value: list of nucleotides
    # Output: trimmed_nucleotide, type = str
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
