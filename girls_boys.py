
# coding: utf-8

# In[23]:


import pandas as pd
import string
#opening both the files and
def number_g_b():
    with open("./namesGirls.txt") as f:
        lines_g=f.read().splitlines()
    with open("./namesBoys.txt") as f:
        lines_b=f.read().splitlines()
    #print(lines_g)
    #print(lines_b)
    df=pd.DataFrame({"End Letter": list(string.ascii_lowercase),"Number_of_Girls":0,"Number_of_Boys":0})
    #print(df)
    #to check the ascii value of the first letter
    #print("The ASCII value of 'a' is",ord("a"))
    for g in lines_g:
        #taking the last character and assigning it to charg
        charg=g[-1]
        index=ord(charg)-97
        df.loc[index,'Number_of_Girls']=df.loc[index,'Number_of_Girls']+1
    for b in lines_b:
        #taking the last character and assigning it to charg
        charb=b[-1]
        index=ord(charb)-97
        df.loc[index,"Number_of_Boys"]=df.loc[index,"Number_of_Boys"]+1
    print(df)
        
number_g_b()

