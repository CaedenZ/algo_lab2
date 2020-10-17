class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:    # Queue is used for BFS
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Method to add an item to the queue
    def EnQueue(self, val):
        newNode = ListNode(val)

        if self.tail is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

        # Method to remove an item from queue

    def DeQueue(self):

        if self.isEmpty():
            return None
        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.tail = None

        return temp.val


def BFS(graph, paths, queues, src_node, k):
    queue = queues[src_node]
    if not queue.isEmpty():
        current_node = queue.DeQueue()
        if current_node in graph:
            for neighbor in graph[current_node]:
                if src_node not in paths[neighbor] and len(paths[neighbor]) < k:
                    queue.EnQueue(neighbor)
                    paths[neighbor][src_node] = current_node

        return True
    else:
        return False


def tracePath(paths, node, shortestPaths):
    for source_hospital in paths[node]:
        back_tracing_path = []
        back_trace_to_hospital(paths, node, source_hospital, back_tracing_path)
        shortestPaths.append(back_tracing_path.copy())


def back_trace_to_hospital(paths, node, source_hospital, back_tracing_path):
    if node == source_hospital:
        back_tracing_path.append(source_hospital)
    else:
        back_tracing_path.append(node)
        back_trace_to_hospital(paths, paths[node][source_hospital], source_hospital, back_tracing_path)


if __name__ == '__main__':
    #############################################
    #     Preparation of data from the 2 files  #
    #############################################
    graph = {}  # stores the graph into an adjacency list -> { node: [ neighbors ] }

    # file1 = "roadNet-PA.txt"
    # file2 = "hospitals_roadNet-PA.txt"
    file1 = "105_random_nodes.txt"
    file2 = "hospitals_105_nodes.txt"
    k = int(input("Enter value for k: "))
    f1 = open(file1, "r")   # file 1 contains the network data
    clearStr = f1.readline()
    while clearStr[0] == '#':   # while loop to clear the first few lines of the file which describes the data
        clearStr = f1.readline()
    str1 = clearStr + f1.read()
    f1.close()
    arr1 = str1.split("\n")

    for i in arr1[0:-1]:    # for loop to create the adjacency list and store it into the 'graph' variable
        a = i.split("\t")
        if int(a[0]) not in graph:
            graph[int(a[0])] = [int(a[1])]
        else:
            graph[int(a[0])].append(int(a[1]))

    f2 = open(file2, "r")   # file 2 contains the hospitals
    size = f2.readline()
    str2 = f2.read()
    hospital_list = list(map(int, str2.split()))

#############################################
#        finished preparation of data       #
#############################################

    # This part is important,
    # paths variable stores all the paths to k nearest hospitals for each node
    paths = {}

    for node in graph:     # initiate all the paths
        paths[node] = {}    # each node will have their own dictionary/hashmap to store the paths to the source hospital
                            # in the form { source_hospital: predecessor}
#   for example:
#
#           0           k = 2
#            \          hospitals: 1, 6
#         4   1
#        / \ / \
#       5   3   2
#          / \
#         6   8
#          \
#           7
#
#    **** The reason there are 2 sets of {source_hospital: predecessor} in the dictionary is because k = 2
#    **** so the 2 are the nearest hospital and the path connecting the node to the hospital.
#    **** To trace the path back to that hospital, you just follow keep tracing the predecessor until you reach.
#
#       node number -> {source_hospital: predecessor, source_hospital: predecessor}
#     paths = { node 0 -> { 1: 1, 6: 1 },
#               node 1 -> { 1: 1, 6: 3 },
#               node 2 -> { 1: 1, 6: 1 },
#               node 3 -> { 1: 1, 6: 6 },
#               node 4 -> { 6: 3, 1: 3 },
#               node 5 -> { 6: 4, 1: 4 },
#               node 6 -> { 6: 6, 1: 3 },
#               node 7 -> { 6: 6, 1: 6 },
#               node 8 -> { 6: 3, 1: 3 }
#               }
#       So the 2 nearest hospitals for node 0 are 1 and 6. To get to hospital 1, you have to follow the
#       predecessor using the key of the source_hospital (which is 1 in this case). To reach node 1, the key will be 1.
#       key 1 for node 0 points to node 1, and that's the path to hospital 1. The second nearest hospital is hospital 6.
#       To reach hospital 6, the key used will be 6.
#       key 6 for node 0 points to node 1
#       key 6 for node 1 points to node 3
#       key 6 for node 3 points to node 6
#       And you have traced the path back to hospital 6.
#       Try applying this to the other nodes and see how each of them trace back to the respective hospitals.

    queues = {}  # This dictionary stores the state of each queue, which is required to implement BFS for each hospital

    for hospital in hospital_list:    # For each hospital, their first nearest hospital is themself.
        newQueue = Queue()            # So lets say node 7 is a hospital. node 7 -> { 7: 7 }
        newQueue.EnQueue(hospital)    # This means the path to hospital 7 is 7, in this case, the distance will be 0.
        queues[hospital] = newQueue
        if hospital in paths:
            paths[hospital][hospital] = hospital

    stillHave = True    # basically to check when to stop, stillHave will be set to false when none of the hospitals
                        # can BFS any further.

    while stillHave:    # this while loop does 1 iteration of BFS for each hospital
        stillHave = False
        for hospital in hospital_list:
            if BFS(graph, paths, queues, hospital, k):
                stillHave = True

    #####################################
    #   Saving the answer into a file   #
    #####################################

    ans = open("ANSWER_BFS_Hospitals.txt", 'w')

    for node in sorted(paths.keys()):
        shortest_paths = []
        if len(paths[node]) > 0:
            ans.write(str(node) + ':  ')
            tracePath(paths, node, shortest_paths)      # TracePath will trace the path from the node to the k
                                                        # nearest hospitals, using a recursive function called
                                                        # back_trace_to_hospital.
            for path in shortest_paths:
                ans.write('    dist: ' + str(len(path)-1) + '  path: ')
                string = ', '.join(str(x) for x in path)
                ans.write(string)
            ans.write('\n')
    ans.close()
