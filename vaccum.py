def vaccum(A, B, vac_locat):
    A_st=A
    B_st=B
    vac_locat=vac_locat
    action_list=[]
    sum=0
    print('%s, %s, %s'%(A, B, vac_locat))
    for i in range (0,1000):
        sum+=performance(A_st, B_st)
        slist= percept(A_st, B_st, vac_locat)
        A_st=slist[0]
        B_st=slist[1]
        vac_locat=slist[2]
        action=slist[3]
        
        action_list.append(action)
    
    #print(action_list)
    print(sum)
    

def percept(A,B,vac_locat):
    if vac_locat=='A':
        if A=='clean':
            vac_locat='B'
            return (A,B,vac_locat,'right')
        elif A=='dirty':
            A='clean'
            return (A,B,vac_locat,'suck')
        
    elif vac_locat=='B':
        if B=='clean':
            vac_locat='A'
            return (A,B,vac_locat,'left')
        elif B=='dirty':
            B='clean'
            return (A,B,vac_locat,'suck')
    
    

def performance(A,B):
    score=0
    if A=='clean':
        score+=1
    if B=='clean':
        score+=1
    return score


vaccum('clean','clean','A')
vaccum('clean','dirty','A')
vaccum('dirty','clean','A')
vaccum('dirty','dirty','A')
vaccum('clean','clean','B')
vaccum('clean','dirty','B')
vaccum('dirty','clean','B')
vaccum('dirty','dirty','B')