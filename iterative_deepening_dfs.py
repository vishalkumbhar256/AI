tree = {'A':['B','C'],'B':['D','E','F'],'C':['G','H'],'D':[],'E':[],'F':[],'G':[],'H':[]}
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
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

max=100
def iterateddfs(start,goal,tree,max):
    for i in range(max):
        print("Iteration: ",i+1)
        path=[]
        if dfs(start,goal,tree,level,path,i):
            print("path to goal node available")
            print("path: ",path)
            return True
    return False
iterateddfs(start,goal,tree,max)
        
    
    


