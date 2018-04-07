import json

filename = 'udata'
filename2 = 'odata'

#initialize list
records = []

#add records from the file to the list
with open(filename) as f:
    for line in f:
        # print(json.loads(line))
        records.append(json.loads(line))

#function to return sequenceNumber when dictionary is passed
def myfunction(k):
    return int(k['id'])

"""sort the records according to sequenceNumber"""
# print("Records before sorting: \ns")
# print(records)
sorted_records = sorted(records, key=myfunction)
# print("Records after sorting: \n")
# print(sorted_records)

#convert the list into string to output to a file
sorted_string = ""
for rec in sorted_records:
    sorted_string += str(rec) + "\n"
# sorted_string = json.dumps(sorted_records)
# print(sorted_string)

#write the sorted data to the file
with open(filename2, 'w') as f:
    f.write(sorted_string)
    f.close()
