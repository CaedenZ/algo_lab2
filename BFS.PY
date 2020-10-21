# # Python3 Program to print BFS traversal 
# # from a given source vertex. BFS(int s) 
# # traverses vertices reachable from s. 

# file1 = "roadNet-CA.txt"
# file2 = "answer.txt"
# k = int(input("Enter value for k: "))

# #--------- editing the file ---------#
# editfile1 = open(file1, "r")   # file 1 contains the network data
# clearStrings = editfile1.readline() 
# while clearStrings[0] == '#':   # while loop to clear the first few lines of the file which describes the data
#         clearStrings = editfile1.readline()
#     str1 = clearStrings + editfile1.read()
#     editfile1.close()




# editfile2 = open(file2, "r")   # file 2 contains the hospitals
#     size = editfile2.readline()
#     str2 = editfile2.read()
#     hospital_list = list(map(int, str2.split()))


def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

graph = {}  # stores the graph into an adjacency list -> { node: [ neighbors ] }

# file1 = "roadNet-PA.txt"
# file2 = "hospitals_roadNet-PA.txt"
file1 = "small road.txt"
file2 = "hospital2.txt"
#k = int(input("Enter value for k: "))
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
print(hospital_list[0])
#print(graph)
k = int(input("Enter value for k: "))
i= 0
while(k>0):
    while(i<k):
        print(bfs(graph, 0, hospital_list[i]))
        i = i+1
    k = k-1