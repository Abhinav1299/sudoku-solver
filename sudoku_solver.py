import time

# board=[
#     [0,0,0,2,6,0,7,0,1],
#     [6,8,0,0,7,0,0,9,0],
#     [1,9,0,0,0,4,5,0,0],
#     [8,2,0,1,0,0,0,4,0],
#     [0,0,4,6,0,2,9,0,0],
#     [0,5,0,0,0,3,0,2,8],
#     [0,0,9,3,0,0,0,7,4],
#     [0,4,0,0,5,0,0,3,6],
#     [7,0,3,0,1,8,0,0,0]
# ]

# board=[
#     [5,0,8,4,0,0,3,0,1],
#     [0,9,0,0,6,0,0,8,0],
#     [0,0,0,0,0,0,0,0,0],
#     [6,0,0,0,0,0,1,0,0],
#     [0,2,0,0,8,0,0,3,0],
#     [0,0,9,0,0,0,0,0,5],
#     [0,0,0,0,0,0,0,0,0],
#     [0,6,0,0,3,0,0,4,0],
#     [8,0,7,0,0,1,5,0,9]
# ]

board=[
    [0,9,0,0,0,5,0,0,0],
    [0,5,0,0,2,0,0,9,6],
    [0,0,4,0,1,0,3,0,0],
    [4,0,0,0,0,0,0,0,0],
    [0,7,3,0,8,0,2,6,0],
    [0,0,0,0,0,0,0,0,7],
    [0,0,8,0,7,0,1,0,0],
    [1,4,0,0,3,0,0,2,0],
    [0,0,0,6,0,0,0,8,0]
]

count=0

def print_board(brd):
    print()
    for i in range(len(brd)):
        print("  ",end="  ")
        if(i%3==0 and i!=0):
            print("- - - - - - - - - - - - - - - - - - ")
            print("  ",end="  ")
        for j in range(len(brd[0])):
            if(j%3==0 and j!=0):
                print(" | ",end="")
            if(j==8):
                print(" "+str(brd[i][j]))
            else:
                print(" "+str(brd[i][j]),end=" ")

    print()


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if(brd[i][j]==0):
                return (i,j)
    return False


def valid(brd,num,pos):
    for i in range(len(brd)):   # row column
        if brd[i][pos[1]]==num and i!=pos[0]:
            return False
    
    for i in range(len(brd[0])):    # check row
        if brd[pos[0]][i]==num and i!=pos[1]:
            return False
    
    # check box
    box_x=pos[0]//3
    box_y=pos[1]//3
    for i in range(box_x*3,(box_x*3)+3):
        for j in range(box_y*3,(box_y*3)+3):
            if brd[i][j]==num and (i,j)!=pos:
                return False
    return True

count=0
def solve(brd):
    global count
    find=find_empty(brd)
    if find==False:         # base case of recursion
        return True
    else:
        row,col=find

    for i in range(1,10):
        v=valid(brd,i,find)
        if(v==True):
            brd[row][col]=i

            if(solve(brd)==True):
                return True

            brd[row][col]=0
            count+=1
    return False


print_board(board)
start=time.time()
solve(board)
end=time.time()
print_board(board)
print("total changes in our assumption =  "+str(count))
print("total time to solve the sudoku =  "+str(end-start)+" sec")