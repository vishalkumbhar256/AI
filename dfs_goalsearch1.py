"""ABSOLUTE"""
tree = {'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
close=[]
def dfs(tree,start):
    if start not in close:
        print(start)
        close.append(start)
        neighbour=tree[start]
        for i in neighbour:
            if goal in close:
                break
            else:
                dfs(tree,i)
dfs(tree,start)
