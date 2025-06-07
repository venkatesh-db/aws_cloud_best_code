
'''
# variable 
smiles =50 

# Scripting 

# variables 
joy="happy"

# conditions 
if joy == "happy":
    print("i might win ")

# loops 
for i in range(3): # index 0 ..2 
    print(i)

# DSA 

tuples = ( "processor","8 gb") 
lists=["server1","16 gb"]
lists.append("server2")
dicts={"mumbai":"server1","bangalore": "server2"}
print(dicts )

'''

# Automotion - AWS 

def Resuable():
    # problem in this code  data is hardcoded 
    
    # variables 
    joy="happy"

    # conditions 
    if joy == "happy":
            print("i might win ")

    # loops 
    for i in range(3): # index 0 ..2 
     print(i)

    # DSA 

    tuples = ( "processor","8 gb") 
    lists=["server1","16 gb"]
    lists.append("server2")
    dicts={"mumbai":"server1","bangalore": "server2"}
    print(dicts )


def  Automoation(joy ,loop, tups,lists,dicts):
# based on data code automotion works
    
         # conditions 
         if joy == "happy":
            print("i might win ")
         elif joy !="happy":
             raise Exception("invalid data")
         
         # loops 
         for i in range(loop): # index 0 ..2 
            print(i)
        
         for i in lists:
             print(i)
            
'''    
tuples = ( "processor","8 gb") 
lists=["server1","16 gb"]
lists.append("server2")
dicts={"mumbai":"server1","bangalore": "server2"}
Automoation("happy" ,3,tuples,lists,dicts)     
'''

def ECtwoinstance(serverconfig):
    sconfig={}
    
    if serverconfig == "Linux":
         sconfig.update({serverconfig:"corei5 16gb ram"})
        
    elif serverconfig == "redhat":
        sconfig.update({serverconfig:"corei7 8gb ram"})
        
    elif serverconfig == "rtlinux":
         sconfig.update({serverconfig:"corei6 8gb ram"})
         
    return sconfig
  
    
serverconfig=ECtwoinstance("redhat")
print(serverconfig)           