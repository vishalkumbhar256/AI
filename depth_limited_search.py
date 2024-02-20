"""depth limited search"""

tree = {'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
max_d=int(input("Enter depth limit: "))
path=[]
level=0
def dfs(start,goal,tree,level,path,max_d):
    print("Current level is: ",level)
    path.append(start)
    if start==goal:
        print("Goal Found")
        return path
    if level==max_d:
        return False
    print("Expanding the node ",start)
    neighbour=tree[start]
    for i in neighbour:
        if dfs(i,goal,tree,level+1,path,max_d):
            return path
        path.pop()
    return False
if dfs(start,goal,tree,level,path,max_d):
    print("Goal is present")
    print(path)
else:
    print("Goal is not found")
    



