"""εντοπίζει τα κεφαλαία γράμματα μέσα σε μία λέξη.
παίρνει ορίσματα από τη γραμμή εντολών"""

import sys

def index_of_caps(str_arg):
    indexList = []
    for i in range(len(str_arg)):
        if str_arg[i].isupper():
            indexList.append(i)
    
    return indexList

arguments = len(sys.argv) - 1


position = 1
while (position <= arguments):
    
    txt = index_of_caps(sys.argv[position])
    print(txt)
    position = position + 1

