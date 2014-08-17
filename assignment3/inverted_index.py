import MapReduce
import sys

"""
Inverted index based on Python MapReduce Framework.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = [document_id, text], type = str, str
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    words = list(set(words)) # Avoid duplicate words in doc
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document ID
    # Output: (word, document_id), type = str, list(str)
    documents = []
    for doc in list_of_values:
        documents.append(doc)
    mr.emit((key, documents))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
