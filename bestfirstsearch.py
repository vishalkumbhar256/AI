tree={'A':[('B',12),('C',4)],'B':[('D',7),('E',3)],'C':[('F',8),('G',2)],'D':[],'E':[('H',0)],'F':[('H',0)],'G':[('H',0)],'H':[]}
"""print(tree['A'])
node=tree['A']
print(node)
print(node[0])
print(node[1])"""
open=[]
close=[]
start=input("Enter the start node: ")
goal=input("Enter the goal node: ")
def best_fs(start,goal,tree,open,close):
    if start not in close:
        print(start)
        close.append(start)
        neighbour=tree[start]
        for i in neighbour:
            if i[0] not in open:
                open.append(i)
        open.sort(key=lambda i:i[1])
        if open[0][0]==goal:
            print(open[0][0])
        else:
            node=open[0]
            open.remove(node)
            best_fs(node[0],goal,tree,open,close)
print("Path is:")
best_fs(start,goal,tree,open,close)
