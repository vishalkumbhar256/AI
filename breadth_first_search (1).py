tree = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':['f'],
    'f':[]
}

start=input("ENTER THE START STATE: ")

def bfs_traversal(tree,start):
    close=[]
    open=[start]
    while open:
        node=open.pop(0)
        if node not in close:
            close.append(node)
            neighbour=tree[node]
            for i in neighbour:
                open.append(i)
    return close
print("Traveral is: ",bfs_traversal(tree,start))
    


