import MapReduce
import sys

"""
Relational join based on Python MapReduce Framework.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record = a tuple in database, type = list(str)
    # key: order_id, index = 1
    # value: the record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of records, from both "LineItem" table 
    # and "Order" table
    # Output: joined record, type = list(str)
    
    # Split "line_item" records and "order" records
    line_item = []
    order = []
    for record in list_of_values:
        if record[0] == "line_item":
            line_item.append(record)
        elif record[0] == "order":
            order.append(record)
    
    # Do inner join
    for order_record in order:
        for item_record in line_item:
            joined = []
            joined += order_record
            joined += item_record
            mr.emit(joined)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
    
