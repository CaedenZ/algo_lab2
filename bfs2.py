from queue import Queue
from _collections import defaultdict

#-------- To obtain shortest path --------#
def getResult(graph, size, src_node, hospitals, k):
    parent = [-1] * size                                                    #Set the starting node size
    nearest_hospitals = BFS(graph, size, src_node, hospitals, parent, k)    # to call the BFS 
    paths = []                                                              # create an array for the shortest path
    
    for current_hospital in nearest_hospitals:                              
        current = current_hospital
        path = [current]
        while parent[current] != -1:                                        # When parent[current] not equals to -1, there is a neighbour present
            path.append(parent[current])                                    # The neighbour will be added to the path
            current = parent[current]                                       # The neighbour will now become the current node
        paths.append(path.copy())                                           # Update the path into paths
    return paths

#------------ BFS code -------------#
def BFS(graph, size, src_node, hospitals, parent, k):
    queue = Queue()                                                         # Start a queue
    visited = [False] * size                                                # Set every single node to not visited
    tmp_k = 0                                                               # Number of hospitals found
    hospitalList = []                                                       # Create a list for hospitals
    visited[src_node] = True                                                # Set starting node as visited
    queue.EnQueue(src_node)                                                 # Add starting node to the queue

    if str(src_node) in hospitals:                                          # If starting node is a hospital, 
        tmp_k += 1                                                          # Add 1 to hospitals found
        hospitalList.append(src_node)                                       # Add source node to hospital list


    # parent = [-1,-1,-1]
    # if current = 3
    # parent[current] = 1
    # path.append(1)
    # current = parent[current] = 1
    # updated path: [-1, 0, 0, 1]  
    # -1: Not Visited 
    # 0: Neighbour
    # 1: Visted
    # parent = [-1,-1,1]

    while not queue.isEmpty() and tmp_k < k:                                # When there is something in the queue and number of hospitals found is less than k,
        current_node = queue.DeQueue()                                      # Get current node from the queue
        for nextNode in graph[current_node]:                                # Get the next node base on the graph
            if not visited[nextNode]:                                       # Checks if the node is visited before or not, if not visited,
                visited[nextNode] = True                                    # Next node will be marked as visited
                parent[nextNode] = current_node                             # Set the neighbour as the current node
                queue.EnQueue(nextNode)                                     # Add next node to the queue
                if str(nextNode) in hospitals:                              # if next node is a hospital,
                    tmp_k += 1                                              # Add 1 to hospitals found
                    hospitalList.append(nextNode)                           # Add source node to hospital list
                    if tmp_k >= k:                                          # Check if number of hospitals is more than k 
                        break                                               
    return hospitalList


if __name__ == '__main__':

    g = defaultdict(list)                                                   # create a dictionary list for our graph
#-------- Prepare the data --------#
    edgeFile = "roadNet-CA.txt"
    hospitalFile = "hospital2.txt"
    edgeFileOpen = open(edgeFile, "r")
    clearStr = edgeFileOpen.readline()                                      
    while clearStr[0] == '#':                                               # Remove strings before the data
        clearStr = edgeFileOpen.readline()
    str1 = clearStr + edgeFileOpen.read()                                   
    edgeFileOpen.close()
    arr1 = str1.split("\n")

    size = 0

    for i in arr1[0:-1]:                                                    # Input our data into our graph in a matrix format
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

    k = int(input("Enter value for k (top-k hospital): "))                                   # Get input k from user (top-k hospital)

#------- To retrieve the result --------#
    result = open("result.txt", 'w')

    for node in sorted(g.keys()):
        paths = getResult(g, size, node, hospitals, k)                                       # Call the shortest path function
        result.write('source node  :' + str(node) + ':  ')                                    
        for path in paths:                                                                   # Output every path into the text file
            result.write(', distance: ' + str(len(path) - 1) + ',  path: [')
            string = ', '.join(str(x) for x in path[::-1])
            result.write(string + ' ]')

        result.write('\n')
    result.close()
