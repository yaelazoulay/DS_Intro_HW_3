# -*- coding: utf-8 -*-

###YAEL A ######
def read_line(n,file) :
    
        try:
            filename = open(file)
        except :
               return "FILE NOT FOUND"
      
        lines = filename.readlines() 
        
        if type(n) == int :
            count = 0
            for i in lines :
                count+=1
            if n>count :   
                return "LINE" ,n, "DOES NOT EXIST"

        else:
            return "INVALID INPUT DETECTED"

        return lines[n-1]
       
             
print(read_line(8,"Desktop\ex3_text.txt"))
                          
  

#%%
#B

L = list()
L2 =list()
L3 = list()
def longest_words(file):
    try:
        filename = open(file)
    except :
           return "file not found"

    for i in filename:
        words = i.split()
        for word in words:
            if word.startswith('-')==False:
                L.append(word)
    for i in L:
         i = i.split(".")
         for word in i:
             word=word.rstrip(',')
             L2.append(word)            
    x= sorted(L2,key = len,reverse=True)       
    L3 = x[:5]   
    return(L3)



print(longest_words("Desktop\ex3_text.txt"))






