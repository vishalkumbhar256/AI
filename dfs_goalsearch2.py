"""RELATIVE"""
tree = {'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
def dfs_search(tree,start):
    close=[]
    open=[[start]]
    if start==goal:
        print("start is a goal node")
    while open:
        path=open.pop()
        node=path[-1]
        if node not in close:
            close.append(node)
        neighbour=tree[node]
        for i in neighbour:
            new_path=list(path)
            new_path.append(i)
            open.append(new_path)
            if i==goal:
                return new_path
print("path is: ",dfs_search(tree, start))
    

