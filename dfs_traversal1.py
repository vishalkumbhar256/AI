tree = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]
}

start=input("ENTER THE START STATE: ")

def dfs(tree):
    close=[]
    open=[start]
    while open:
        node=open.pop()
        if node not in close:
            close.append(node)
            neighbour=tree[node]
            for i in neighbour:
                open.append(i)
    return close
print("DFS traversal is: ",dfs(tree))
                



