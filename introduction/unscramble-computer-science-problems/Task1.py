"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
texts_incoming = [row[0] for row in texts]
texts_answering = [row[1] for row in texts]
calls_incoming = [row[0] for row in calls]
calls_answering = [row[1] for row in calls]

Numbers = []
for i in texts_incoming:
    if i not in Numbers:
        Numbers.append(i)
    
for i in texts_answering:
    if i not in Numbers:
        Numbers.append(i)

for i in calls_incoming:
    if i not in Numbers:
        Numbers.append(i)

for i in calls_answering:
    if i not in Numbers:
        Numbers.append(i)

print(f"There are {len(Numbers)} different telephone numbers in the records.")
