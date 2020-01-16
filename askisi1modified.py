#στο πρόγραμμα υποθέτουμε ότι οι αριθμοί που θα δοθούν από το 
#χρήστη είναι διαφορετικοί ανά δύο μεταξύ τους

#με τις τροποποιήσεις για την άσκηση 2

#πλήθος αριθμών
number = input("Δώσε το πλήθος των αριθμών:")

numberList = []
for i in range(int(number)):
    txt = "Δώσε {} αριθμό:"
    num = input(txt.format(i+1))
    numberList.append(int(num))

firstInList = numberList[0]
    
max1 = max(numberList)
max1Index = numberList.index(max1)
txt = "Ο μέγιστος αριθμός της λίστας είναι {} στη θέση {}"
print(txt.format(max1, max1Index + 1))
numberList.pop(max1Index)

max2 = max(numberList)
max2Index = numberList.index(max2)
txt = "Ο δεύτερος μέγιστος αριθμός της λίστας είναι {} στη θέση {}"
print(txt.format(max2, max2Index + 1))

txt = "Ο πρώτος αριθμός που κατεχωρήθη είναι {}"
print(txt.format(firstInList))