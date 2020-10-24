from queue import Queue
from _collections import defaultdict


def getShortestPaths(graph, size, src_node, hospitals, k):
    pred = [-1] * size
    nearest_hospitals = BFS(graph, size, src_node, hospitals, pred, k)
    paths = []
    for current_hospital in nearest_hospitals:
        crawl = current_hospital
        path = [crawl]
        while pred[crawl] != -1:
            path.append(pred[crawl])
            crawl = pred[crawl]
        paths.append(path.copy())
    return paths


def BFS(graph, size, src_node, hospitals, pred, k):
    queue = Queue()
    visited = [False] * size
    hospitals_found = 0
    hospital_list = []  # stores all the hospitals found
    visited[src_node] = True
    queue.EnQueue(src_node)

    if str(src_node) in hospitals:
        hospitals_found += 1
        hospital_list.append(src_node)

    while not queue.isEmpty() and hospitals_found < k:
        current_node = queue.DeQueue()
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                pred[neighbor] = current_node
                queue.EnQueue(neighbor)
                if str(neighbor) in hospitals:
                    hospitals_found += 1
                    hospital_list.append(neighbor)
                    if hospitals_found >= k:
                        break
    return hospital_list


def BFS2(graph, paths, hospital, k):
    # TODO
    pass


if __name__ == '__main__':

    g = defaultdict(list)

    file1 = "roadNet-CA.txt"
    file2 = "hospital2.txt"
    f1 = open(file1, "r")   # file 1 contains the network data
    clearStr = f1.readline()
    # while loop to clear the first few lines of the file which describes the data
    while clearStr[0] == '#':
        clearStr = f1.readline()
    str1 = clearStr + f1.read()
    f1.close()
    arr1 = str1.split("\n")

    size = 0
    # for loop to create the adjacency list and store it into the 'graph' variable
    for i in arr1[0:-1]:
        a = i.split("\t")
        g[int(a[0])].append(int(a[1]))
        if int(a[0]) > size:
            size = int(a[0])
        if int(a[1]) > size:
            size = int(a[1])

    size += 1

    f2 = open(file2, "r")
    nu = f2.readline()
    str2 = f2.read()
    hospitals = str2.split("\n")
    f2.close()

    k = int(input("Enter value for k: "))

    paths = {}

    for node in g:
        paths[node] = {}

    for hospital in hospitals:
        BFS2(g, paths, hospital, k)

    ans = open("ANSWER.txt", 'w')

    for node in sorted(g.keys()):
        paths = getShortestPaths(g, size, node, hospitals, k)
        ans.write('source node  :' + str(node) + ':  ')
        for path in paths:
            ans.write(', distance: ' + str(len(path) - 1) + ',  path: [')
            string = ', '.join(str(x) for x in path[::-1])
            ans.write(string + ' ]')

        ans.write('\n')
    ans.close()
