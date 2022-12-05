def Biconexo(p,v,graph,pre,cpre,low,pA,pM):
    cpre += 1
    pre[v] = cpre
    low[v] = cpre
    print ("Entrando em ", v+1, " -> pre:", pre, "low:", low)
    for i in range(0,len(graph[v])):
        if graph[v][i] == 1:
            aresta = ["{}-{}".format(min(i+1,v+1),max(i+1,v+1))]
            if aresta not in pA and aresta not in pM:
                pM.append(aresta)
                pA.append(aresta)
            if pre[i] == 0:
                pre, cpre, low, pA, pM = Biconexo(v,i,graph,pre,cpre,low,pA,pM)
                if pre[v] <= low[i]:
                    print ("Componente Biconexo: ",end="")
                    while pA[len(pA)-1] != aresta:
                        print(pA.pop(),end="")
                    print(pA.pop())
                low[v] = min(low[v], low[i])
            elif i != p:
	            low[v] = min(low[v], pre[i])
    print ("Saindo de ", v+1, "   -> pre:", pre, "low:", low)
    return pre, cpre, low, pA, pM
    
    
graph = [[0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0]]

cpre = 0
pre = [0 for i in graph] 
low = [0 for i in graph] 
pA, pM = [], []

priorityList = list(range(4,len(graph))) + list(range(0,4))

for v in priorityList:
    if pre[v] == 0:
        pre, cpre, low, pA, pM = Biconexo(v,v,graph,pre,cpre,low,pA,pM)
    
