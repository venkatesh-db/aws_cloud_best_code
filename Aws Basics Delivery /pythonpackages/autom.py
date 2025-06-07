
def ECtwoinstance(serverconfig):
    sconfig={}
    
    if serverconfig == "Linux":
         sconfig.update({serverconfig:"corei5 16gb ram"})
        
    elif serverconfig == "redhat":
        sconfig.update({serverconfig:"corei7 8gb ram"})
        
    elif serverconfig == "rtlinux":
         sconfig.update({serverconfig:"corei6 8gb ram"})
         
    return sconfig