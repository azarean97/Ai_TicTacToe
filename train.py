### TicTacToe with MiniMax algorithm
worldSize = 3
world = {
    0: [2, 1, 2], 1: [0 ,2, 0], 2: [1, 0, 0]
}

####
'''

in our matrix 0 is empty room
1 is coumputer move
2 is human move

'''
####
def check(lst):
    print(lst)
    for i in range(8):
        if lst[i][0] == lst[i][1] == lst[i][2] == 1:
            return (True , 'Computer')

        if lst[i][0] == lst[i][1] == lst[i][2] == 2:
            return (True , 'Human')

    return (-1 , -1 )



def winAll(localWorld) :
    win , who = True , ' '
    totalcheckList = []
    ## 
    ###########
    ##
    
    for i in range(3):
        checkList = []
        for j in range(3):
            checkList.append( localWorld[i][j] )
#        print(checkList)
        totalcheckList.append(checkList)

    ##  #
    ##  #
    ##  #
    
    for i in range(3):
        checkList = []
        for j in range(3):
            checkList.append ( localWorld[j][i] )
        totalcheckList.append(checkList)

    ##  #
    ##   #
    ##    #
    
    for i in range(2):
        checkList = []
        for j in range(3):
            checkList.append( localWorld[j][abs(j-(i*2))] )        
        totalcheckList.append(checkList)

    win , who = check(totalcheckList)
    
    if (win , who) == (-1,-1):
        return (False , 'No One')
    else:
        return (win , who)







a , b = winAll(world)
print(a,b)