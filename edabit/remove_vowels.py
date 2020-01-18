def remove_vowels():
    
    table = str.maketrans(dict.fromkeys("aeiou"))
    new_string = '123hello.jpg'.translate(table)
    
    print (new_string)
    #for i in range(len(str)):
     #   if str[i] in "aeiou"


remove_vowels()