#python language
import time
a={} 
def create(key,value,timeout=0):
    if key in a:
        print("ERROR:Key already exists")
    else:
        if(key.isalpha()):
            if len(a)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    a[key]=l
            else:
                print("ERROR: Memory limit exceeded ")
        else:
            print("ERROR: Invalind keyname. keyname must contain only alphabets and no special characters or numbers")
def read(key):
    if key not in a:
        print("ERROR: Given key does not exist in data. Please enter a valid key") 
    else:
        b=a[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("ERROR: Time-to-live of key has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return str
def delete(key):
    if key not in a:
        print("ERROR: Given key does not exist in data. Please enter a valid key") 
    else:
        b=a[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del a[key]
                print("key is successfully deleted")
            else:
                print("ERROR: Time-to-live of key has expired") 
        else:
            del a[key]
            print("Key successfully deleted")
def modify(key,value):
    b=a[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in a:
                print("ERROR: Given key does not exist in data. Please enter a valid key") #ERROR message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                a[key]=l
        else:
            print("ERROR: Time-to-live of key has expired") 
    else:
        if key not in a:
            print("ERROR: Given key does not exist in data. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            a[key]=l
            
create("hrc",3)
create("src",70,3600) 
read("sastra")
read("hrc")
create("sastra",350)
modify("sastra",255) 
delete("sastra")
