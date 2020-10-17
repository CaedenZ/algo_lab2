from _collections import defaultdict
#
#
# def hash1(key, size):
#     return key % size
#
#
# def hash2(key):
#     return 11 - (key % 7)
#
#
# def insertHash(key, hashTable):
#     size = len(hashTable)
#     index = hash1(key, size)
#     initial_index = index
#     if hashTable[index] is not None:
#         index2 = hash2(key)
#         i = 1
#         while True:
#             newIndex = (index + i * index2) % size
#             if initial_index == newIndex:
#                 index = (initial_index + 1) % size
#                 while hashTable[index] is not None:
#                     index = (index + 1) % size
#                 hashTable[index] = key
#                 break
#             if hashTable[newIndex] is None:
#                 hashTable[newIndex] = key
#                 break
#             i += 1
#
#     else:
#         hashTable[index] = key
#
#
# def searchHash(key, hashTable):
#     size = len(hashTable)
#     index1 = hash1(key, size)
#     index2 = hash2(key)
#     i = 0
#     first_key = hashTable[(index1 + i * index2) % size]
#     while hashTable[(index1 + i * index2) % size] != key:
#         if hashTable[(index1 + i * index2) % size] is None or hashTable[(index1 + i * index2) % size] == first_key:
#             return False
#         i += 1
#     return True


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
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

    if is_hospital[src_node]:
        hospitals_found += 1
        hospital_list.append(src_node)

    while not queue.isEmpty() and hospitals_found < k:
        current_node = queue.DeQueue()
        for neighbor in graph[current_node]:
            # print(neighbor, len(graph))
            if not visited[neighbor]:
                visited[neighbor] = True
                pred[neighbor] = current_node
                queue.EnQueue(neighbor)

                # if found hospital, increment hospitals_found
                if is_hospital[neighbor]:
                    hospitals_found += 1
                    hospital_list.append(neighbor)
                    if hospitals_found >= k:
                        break
    return hospital_list


if __name__ == '__main__':
    graph = defaultdict(list)
    # file1 = "roadNet-PA.txt"
    # file2 = "hospitals_roadNet-PA.txt"
    file1 = "105_random_nodes.txt"
    file2 = "hospitals_105_nodes.txt"
    k = int(input("Enter value for k: "))
    f1 = open(file1, "r")

    clearStr = f1.readline()
    while clearStr[0] == '#':
        clearStr = f1.readline()
    str1 = clearStr + f1.read()
    f1.close()
    arr1 = str1.split("\n")
    total_nodes = 0
    for i in arr1[0:-1]:
        a = i.split("\t")
        graph[int(a[0])].append(int(a[1]))
        if int(a[0]) > total_nodes:
            total_nodes = int(a[0])

    total_nodes += 1

    f2 = open(file2, "r")
    size = f2.readline()
    size = int(size.split(" ")[1])
    size *= 1.5
    size = int(size)
    str2 = f2.read()
    arr2 = str2.split("\n")
    is_hospital = total_nodes * [False]
    f2.close()
    for i in arr2:
        is_hospital[int(i)] = True

    # for i in arr2:
    #     insertHash(int(i), hospitals_hashTable)

    ans = open("ANSWER.txt", 'w')

    for node in sorted(graph.keys()):
        paths = getShortestPaths(graph, total_nodes, node, is_hospital, k)
        print(paths)
        ans.write(str(node) + ':  ')
        for path in paths:
            ans.write(' dist: ' + str(len(path) - 1) + '  path: ')
            string = ', '.join(str(x) for x in path)
            ans.write(string)

        ans.write('\n')
    ans.close()
