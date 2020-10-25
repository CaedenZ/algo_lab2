from queue import Queue
from _collections import defaultdict

#-------- To obtain shortest path --------#


def getResult(graph, size, src_node, hospitals, k):
    parent = [-1] * size  # Init the path tracing array
    nearest_hospitals = BFS(graph, size, src_node,
                            hospitals, parent, k)    # to call the BFS
    # create an array for the shortest path
    paths = []

    for current_hospital in nearest_hospitals:
        current = current_hospital
        path = [current]
        # When parent[current] not equals to -1, it have not reach the src node
        while parent[current] != -1:
            # The parent will be added to the path
            path.append(parent[current])
            # The parent will now become the current node
            current = parent[current]
        # Append the path into paths
        paths.append(path.copy())
    return paths

#------------ BFS code -------------#


def BFS(graph, size, src_node, hospitals, parent, k):
    # Start a queue
    queue = Queue()
    # Set every single node to not visited
    visited = [False] * size
    # Number of hospitals found
    tmp_k = 0
    # Create a list for hospitals
    hospitalList = []
    # Set starting node as visited
    visited[src_node] = True
    # Add starting node to the queue
    queue.EnQueue(src_node)

    # If starting node is a hospital,
    if str(src_node) in hospitals:
        # Add 1 to hospitals found
        tmp_k += 1
        # Add source node to hospital list
        hospitalList.append(src_node)

    # parent = [-1, 2 ,0 ,1]
    # if current = hopital_node  = 1
    # parent[current] = 2
    # path.append(2)
    # current = parent[current] = 2
    # parent[current] = 0
    # path.append(0)
    # current = parent[current] = 0
    # parent[current] = -1
    # path = [2, 0]
    # path to hospital 1 from node 0 is [0, 2, 1]

    # When there is something in the queue and number of hospitals found is less than k,
    while not queue.isEmpty() and tmp_k < k:
        # Get current node from the queue
        current_node = queue.DeQueue()
        # Get the next node base on the graph
        for nextNode in graph[current_node]:
            # Checks if the node is visited before or not, if not visited,
            if not visited[nextNode]:
                # Next node will be marked as visited
                visited[nextNode] = True
                # Set the neighbour as the current node
                parent[nextNode] = current_node
                # Add next node to the queue
                queue.EnQueue(nextNode)
                # if next node is a hospital,
                if str(nextNode) in hospitals:
                    tmp_k += 1                                              # Add 1 to hospitals found
                    # Add source node to hospital list
                    hospitalList.append(nextNode)
                    if tmp_k >= k:                                          # Check if number of hospitals is more than k
                        break
    return hospitalList


if __name__ == '__main__':

    # create a dictionary list for our graph
    g = defaultdict(list)
#-------- Prepare the data --------#
    edgeFile = "graphs.txt"
    hospitalFile = "hospital2.txt"
    edgeFileOpen = open(edgeFile, "r")
    clearStr = edgeFileOpen.readline()
    # Remove strings before the data
    while clearStr[0] == '#':
        clearStr = edgeFileOpen.readline()
    str1 = clearStr + edgeFileOpen.read()
    edgeFileOpen.close()
    arr1 = str1.split("\n")

    size = 0

    # Input our data into our graph in a matrix format
    for i in arr1[0:-1]:
        a = i.split("\t")
        g[int(a[0])].append(int(a[1]))
        if int(a[0]) > size:
            size = int(a[0])
        if int(a[1]) > size:
            size = int(a[1])

    size += 1

#------- Prepare the hospital data -------#
    hospitalFileOpen = open(hospitalFile, "r")
    nu = hospitalFileOpen.readline()
    str2 = hospitalFileOpen.read()
    hospitals = str2.split("\n")
    hospitalFileOpen.close()

    # Get input k from user (top-k hospital)
    k = int(input("Enter value for k (top-k hospital): "))

#------- To retrieve the result --------#
    result = open("result.txt", 'w')

    for node in sorted(g.keys()):
        # Call the shortest path function
        paths = getResult(g, size, node, hospitals, k)
        result.write('source node  :' + str(node) + ':  ')
        # Output every path into the text file
        for path in paths:
            result.write(', distance: ' + str(len(path) - 1) + ',  path: [')
            # Reverse the path to ensure result starts from the source node and ends at hospital
            string = ', '.join(str(x) for x in path[::-1])
            result.write(string + ' ]')

        result.write('\n')
    result.close()
