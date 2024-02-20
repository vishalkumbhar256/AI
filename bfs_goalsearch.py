tree = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]
}

goal=input("ENTER THE GOAL STATE: ")
start=input("ENTER THE START STATE: ")

def bfs(tree):
    close=[]
    open=[start]
    if start==goal:
        print(start,"start is a goal")
    else:
        close.append(start)
        while open:
            node=open.pop(0)
            neighbour=tree[node]
            for i in neighbour:
                open.append(i)
                close.append(i)
                if i==goal:
                    return close
        print("goal does not exist")
print("BFS search is ",bfs(tree))
                

