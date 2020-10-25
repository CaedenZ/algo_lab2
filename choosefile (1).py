from PyQt5 import QtWidgets, QtCore, QtGui
from queue import Queue
from _collections import defaultdict

import bfsui
import sys
class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = bfsui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.uploadEdgeBtn.clicked.connect(self.getedgefiles)
        self.ui.uploadHospitalBtn.clicked.connect(self.gethospitalfiles)
        self.ui.submitBtn.clicked.connect(self.displayOutput)

    #-------- To obtain shortest path --------#


    def getResult(self, graph, size, src_node, hospitals, k):
        parent = [-1] * size  # Init the path tracing array
        nearest_hospitals = self.BFS(graph, size, src_node,
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


    def BFS(self, graph, size, src_node, hospitals, parent, k):
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


    def getedgefiles(self):
        global my_file_name1
        fileEdgeName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        self.ui.edgeTxt.setText(fileEdgeName)
        my_file_name1 = str(self.ui.edgeTxt.text())
        

    def gethospitalfiles(self):
        global my_file_name2
        fileHospitalName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        self.ui.hosTxt.setText(fileHospitalName)
        my_file_name2 = str(self.ui.hosTxt.text())

    def displayOutput(self):

        g = defaultdict(list)

        file1 = my_file_name1
        file2 = my_file_name2
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

        k = int(self.ui.textEdit.toPlainText())

        ans = open("result.txt", 'w')

        for node in sorted(g.keys()):
            paths = self.getResult(g, size, node, hospitals, k)
            ans.write('source node  :' + str(node) + ':  ')
            for path in paths:
                ans.write(', distance: ' + str(len(path) - 1) + ',  path: [')
                string = ', '.join(str(x) for x in path[::-1])
                ans.write(string + ' ]')

            ans.write('\n')
        ans.close()
        
   
if __name__ == '__main__':
    
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
