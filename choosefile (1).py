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


    def getShortestPaths(self, graph, size, src_node, hospitals, k):
        pred = [-1] * size
        nearest_hospitals = self.BFS(graph, size, src_node, hospitals, pred, k)
        paths = []
        for current_hospital in nearest_hospitals:
            crawl = current_hospital
            path = [crawl]
            while pred[crawl] != -1:
                path.append(pred[crawl])
                crawl = pred[crawl]
            paths.append(path.copy())
        return paths


    def BFS(self, graph, size, src_node, hospitals, pred, k):
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

        ans = open("ANSWER2.txt", 'w')

        for node in sorted(g.keys()):
            paths = self.getShortestPaths(g, size, node, hospitals, k)
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