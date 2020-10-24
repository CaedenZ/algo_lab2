from queue import Queue
from _collections import defaultdict


def getResult(graph, size, src_node, hospitals, k):
    parent = [-1] * size
    nearest_hospitals = BFS(graph, size, src_node, hospitals, parent, k)
    paths = []
    for current_hospital in nearest_hospitals:
        current = current_hospital
        path = [current]
        while parent[current] != -1:
            path.append(parent[current])
            current = parent[current]
        paths.append(path.copy())
    return paths


def BFS(graph, size, src_node, hospitals, parent, k):
    queue = Queue()
    visited = [False] * size
    tmp_k = 0
    hospitalList = []
    visited[src_node] = True
    queue.EnQueue(src_node)

    if str(src_node) in hospitals:
        tmp_k += 1
        hospitalList.append(src_node)

    while not queue.isEmpty() and tmp_k < k:
        current_node = queue.DeQueue()
        for nextNode in graph[current_node]:
            if not visited[nextNode]:
                visited[nextNode] = True
                parent[nextNode] = current_node
                queue.EnQueue(nextNode)
                if str(nextNode) in hospitals:
                    tmp_k += 1
                    hospitalList.append(nextNode)
                    if tmp_k >= k:
                        break
    return hospitalList


if __name__ == '__main__':

    g = defaultdict(list)

    edgeFile = "roadNet-CA.txt"
    hospitalFile = "hospital2.txt"
    edgeFileOpen = open(edgeFile, "r")
    clearStr = edgeFileOpen.readline()
    while clearStr[0] == '#':
        clearStr = edgeFileOpen.readline()
    str1 = clearStr + edgeFileOpen.read()
    edgeFileOpen.close()
    arr1 = str1.split("\n")

    size = 0

    for i in arr1[0:-1]:
        a = i.split("\t")
        g[int(a[0])].append(int(a[1]))
        if int(a[0]) > size:
            size = int(a[0])
        if int(a[1]) > size:
            size = int(a[1])

    size += 1

    hospitalFileOpen = open(hospitalFile, "r")
    nu = hospitalFileOpen.readline()
    str2 = hospitalFileOpen.read()
    hospitals = str2.split("\n")
    hospitalFileOpen.close()

    k = int(input("Enter value for k: "))

    result = open("result.txt", 'w')

    for node in sorted(g.keys()):
        paths = getResult(g, size, node, hospitals, k)
        result.write('source node  :' + str(node) + ':  ')
        for path in paths:
            result.write(', distance: ' + str(len(path) - 1) + ',  path: [')
            string = ', '.join(str(x) for x in path[::-1])
            result.write(string + ' ]')

        result.write('\n')
    result.close()
