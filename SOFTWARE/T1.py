#Mohamed Ameen Omar
#u16055323
#EAI 320 - Practical 2
#2018
import math
#represents each postion in the maze
class node:
    def __init__(self,position = [0,0], currentPath = [[0,0]], cost = 0, pathCost = 0):
        self.position = position
        self.currentPath = currentPath
        self.cost = cost
        self.pathCost = pathCost
    
    def addPath(self,path = []):
        self.currentPath = []
        if(len(path) == 0):
            self.currentPath = []            
        else:
            for x in range(0, len(path)):
                self.currentPath.append(path[x])
            
    def isGoal(self):
        if(self.position[0] == 9):
            if(self.position[1] == 9):
                return True        
        return False
    #returns a list with the co ordinates of all neighbours 
    def getNeighboursPosition(self):
        neighbours = self.getStraightNeighboursPosition()
        neighbours.extend(self.getDiagonalNeighboursPosition())        
        return neighbours
    
    def getStraightNeighboursPosition(self):    
        temp1 = self.position[0]
        temp2 = self.position[1]        
        myList = []
        if( ( (temp1-1) >=0) and ((temp1-1) <12)):
            tempList = [temp1-1,temp2]
            myList.append(tempList)            
        if( ( (temp1+1) >=0) and ((temp1+1) <12)):
            tempList = [temp1+1,temp2]
            myList.append(tempList)            
        if( ( (temp2-1) >=0) and ((temp2-1) <12)):
            tempList = [temp1,temp2-1]
            myList.append(tempList)            
        if( ( (temp2+1) >=0) and ((temp2+1) <12)):
            tempList = [temp1,temp2+1]
            myList.append(tempList)       
        return myList        
        
    def getDiagonalNeighboursPosition(self):
        temp1 = self.position[0]
        temp2 = self.position[1]        
        myList = []
        if( ( (temp1-1) >=0) and ((temp2-1) >=0)):
            tempList = [temp1-1,temp2-1]
            myList.append(tempList)            
        if( ( (temp2+1) <12) and ((temp1+1) <12)):
            tempList = [temp1+1,temp2+1]
            myList.append(tempList)            
        if( ( (temp2-1) >=0) and ((temp1+1) <12)):
            tempList = [temp1+1,temp2-1]
            myList.append(tempList)            
        if( ( (temp1-1) >=0) and ((temp2+1) <12)):
            tempList = [temp1-1,temp2+1]
            myList.append(tempList)        
        return myList
    
#######################myMaze##################    
class myMaze:
    def __init__(self):
        self.maze = [[0,0,0,0,0,0,0,0,0,0,0,0], 
                     [0,0,0,0,0,1,1,1,0,1,1,0], 
                     [0,1,0,0,0,0,1,1,0,1,1,0], 
                     [0,1,1,0,0,0,0,0,0,1,1,0], 
                     [0,1,1,1,0,0,0,0,0,1,1,0], 
                     [0,1,1,1,1,0,0,0,0,1,1,0], 
                     [0,1,1,1,1,1,1,1,1,1,1,0], 
                     [1,1,1,1,1,1,1,1,1,1,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,1,0],
                     [0,0,1,1,1,1,1,1,1,1,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,0,0]]
        self.maze[7][0] = 0
        # 0 is free
        # 1 is a wall        
        # 2 is expanded
        # 3 is viewed or touched
        # 9 is the path
    
    #returns only free Nodes
    def validateFreeNeighbours(self,neighbours):
        remove = []
        for n in neighbours:            
            temp1 = n[0]
            temp2 = n[1] 
            if(self.maze[temp1][temp2] != 0):
                remove.append(n)
        for x in remove:
            neighbours.remove(x)
        return neighbours
    #if a NODE passed in is already expanded
    def isExpanded(self,temp):
        x = temp.position[0]
        y = temp.position[1]
        if( self.maze[x][y] == 2):
            return True
        return False
        
    #returns only free or viewed
    def validateFreeOrViewed(self,neighbours):
        remove = []
        for n in neighbours:
            temp1 = n[0]
            temp2 = n[1]
            if( (self.maze[temp1][temp2] == 1) or (self.maze[temp1][temp2] == 2)):
                remove.append(n)   
        for x in remove:
             neighbours.remove(x)
        return neighbours
    
    #returns all except a Wall
    def validateNotWall(self,neighbours):
        remove = []
        for n in neighbours:
            temp1 = n[0]
            temp2 = n[1]
            if( (self.maze[temp1][temp2] == 1)):
                remove.append(n)   
        for x in remove:
            neighbours.remove(x)
        return neighbours
    
    def resetMaze(self):
        self.maze = [[0,0,0,0,0,0,0,0,0,0,0,0], 
                     [0,0,0,0,0,1,1,1,0,1,1,0], 
                     [0,1,0,0,0,0,1,1,0,1,1,0], 
                     [0,1,1,0,0,0,0,0,0,1,1,0], 
                     [0,1,1,1,0,0,0,0,0,1,1,0], 
                     [0,1,1,1,1,0,0,0,0,1,1,0], 
                     [0,1,1,1,1,1,1,1,1,1,1,0], 
                     [1,1,1,1,1,1,1,1,1,1,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,1,0],
                     [0,0,1,1,1,1,1,1,1,1,1,0], 
                     [0,0,0,0,0,0,0,0,0,0,0,0]]          
        self.maze[7][0] = 0
        
    def toggleNodeExpanded(self,tempNode):
        self.maze[tempNode.position[0]][tempNode.position[1]] = 2
    
    def toggleNodeViewed(self,tempNode):
        self.maze[tempNode.position[0]][tempNode.position[1]] = 3
        
    def makeWall(self):
        self.maze[7][0] = 1
    #used to format the maze so that the output is more clear(walls,path,etc)     
    #path passed in as an arguement 
    def formatMaze(self,temp):
        for location in temp:
            self.maze[location[0]][location[1]] = "~" #node in the path
        self.maze[0][0] = "S" #start
        self.maze[9][9] = "E" #end
        for x in range(0,len(self.maze)):
            for y in range(0,len(self.maze[x])):
                if(self.maze[x][y] == 0):#a free node
                    self.maze[x][y] = "#" 
            
    def printMaze(self):
        for x in range(0,len(self.maze[0])-1):
            print("________", end = '')
        print('')
        for r in range(0,len(self.maze)):
            print("|", end = '')
            for x in range(0,len(self.maze[r])):
                print(self.maze[r][x], end = '')
                if(x == len(self.maze[r]) -1):
                    print("|", end = '')
                print("\t", end = '')
            print()
        for x in range(0,len(self.maze[0])-1):
            print("________", end = '')
        print()
        print("Legend")
        print("# is free - not expanded or visited\n1 is a wall\n2 is expanded\n3 is viewed or touched\n~ is the path")
        print("S is the start\nE is the end")
        
######################################game###############################
class game:
    def __init__(self):
        self.start = node() #starting node        
        self.uniformSearchMaze = myMaze() #Maze for current instance
        self.uniformNodesExpanded = 0 #number of nodes expanded
        self.uniformNodesViewed = 0 #number of nodes viewed
        self.uniformMaxFrontierQueue = 0; #num of nodes in frontier queue 
        self.uniformPath = []        
        self.greedySearchMaze = myMaze() #Maze for current instance
        self.greedyNodesExpanded = 0 #number of nodes expanded
        self.greedyNodesViewed = 0 #number of nodes viewed
        self.greedyMaxFrontierQueue = 0;   
        self.greedyPath = []
        self.starSearchMaze = myMaze() #Maze for current instance
        self.starNodesExpanded = 0 #number of nodes expanded
        self.starNodesViewed = 0 #number of nodes viewed
        self.starMaxFrontierQueue = 0;  
        self.starPath = []
        self.frontier = [] #current nodes that may be expanded
        
    #resets the game
    def reset(self):
        self.start = node() #starting node        
        self.uniformSearchMaze = myMaze() #Maze for current instance
        self.uniformNodesExpanded = 0 #number of nodes expanded
        self.uniformNodesViewed = 0 #number of nodes viewed
        self.uniformMaxFrontierQueue = 0; #num of nodes in frontier queue 
        self.uniformPath = []        
        self.greedySearchMaze = myMaze() #Maze for current instance
        self.greedyNodesExpanded = 0 #number of nodes expanded
        self.greedyNodesViewed = 0 #number of nodes viewed
        self.greedyMaxFrontierQueue = 0;   
        self.greedyPath = []
        self.starSearchMaze = None 
        self.starSearchMaze = myMaze() #Maze for current instance
        self.starNodesExpanded = 0 #number of nodes expanded
        self.starNodesViewed = 0 #number of nodes viewed
        self.starMaxFrontierQueue = 0;  
        self.starPath = []
        self.frontier = [] #current nodes that may be expanded

    def uniformSearch(self):
        self.reset()
        self.frontier = []
        self.frontier.append(self.start)
        temp = None
        self.uniformNodesViewed = 1
        print("Conducting a Uniform Cost Search")
        while(self.frontier != []):
            if(len(self.frontier) > self.uniformMaxFrontierQueue): #to get the largest size of queue
                self.uniformMaxFrontierQueue = len(self.frontier)
            temp = self.getUniExpansionNode()#get lowest path cost node 
            if(temp.isGoal() == True):
                self.uniformPath = temp.currentPath
                self.uniformSearchMaze.formatMaze(self.uniformPath)
                break
            self.uniformSearchMaze.toggleNodeExpanded(temp) 
            self.uniformNodesExpanded += 1 
            self.uniformExpand(temp) #expand this node
        print("Search Complete")
        print("Uniform Search Path Found:")
        print(self.uniformPath)
        print("Number of nodes in path", len(self.uniformPath))
        print("Total path cost", temp.pathCost)
        print("Number of nodes expanded ", self.uniformNodesExpanded)
        print("Number of nodes viewed ", self.uniformNodesViewed)
        print("Maximum number of nodes in search queue: ", self.uniformMaxFrontierQueue)
        print("Here is the final Maze:")        
        self.uniformSearchMaze.printMaze() #print the final maze
        print()
        print()
        
    #expands the current state      
    def uniformExpand(self,tempNode):
        if(tempNode == None):
            return 
        neighbours = tempNode.getNeighboursPosition()#get all neighbours     
        neighbours = self.uniformSearchMaze.validateFreeOrViewed(neighbours)#remove all walls and expanded nodes
        for x in neighbours:
            newNode = node()
            newNode.position = [x[0],x[1]]
            newNode.cost = self.getNeighbourCost(tempNode, newNode.position)#from current node to new node
            newNode.pathCost = tempNode.pathCost + newNode.cost# entire path cost g(n)
            newNode.addPath(tempNode.currentPath)
            newNode.currentPath.append(newNode.position)
            self.uniformNodesViewed += 1
            self.uniformSearchMaze.toggleNodeViewed(newNode)
            if(self.isInFrontier(x) == True):
                self.uniformSearchMaze.toggleNodeViewed(newNode)
                for x in range(0,len(self.frontier)):
                    if(self.frontier[x].position == newNode.position):
                        if(self.frontier[x].pathCost > newNode.pathCost):
                            self.frontier[x] = newNode                       
                continue            
            self.frontier.append(newNode)
        
    def isInFrontier(self,position):
        for x in self.frontier:
            if(x.position == position):
                return True
        return False
        
    #uniform search cost from current node to nextNode   
    def getNeighbourCost(self,myNode, nextPostion):
        distance = 0
        if(nextPostion[0] >= myNode.position[0]):
            temp = nextPostion[0] - myNode.position[0]
            distance += (temp*temp)
        else:
            temp = myNode.position[0] - nextPostion[0]
            distance += (temp*temp)
        
        if(nextPostion[1] >= myNode.position[1]):
            temp = nextPostion[1] - myNode.position[1]
            distance += (temp*temp)
        else:
            temp = myNode.position[1] - nextPostion[1]
            distance += (temp*temp)        
        return ( math.sqrt(distance) )
    
    #returns the node we are going to expand, returns node with smallest cost   
    def getUniExpansionNode(self):        
        tempNode = None        
        for x in range(0, len(self.frontier)):
            if(tempNode == None):
                tempNode = self.frontier[x]
            else:
                if(tempNode.pathCost > self.frontier[x].pathCost):
                    tempNode = self.frontier[x]        
        self.frontier.remove(tempNode)                    
        return tempNode
    
    def greedyBestFirstSearch(self):
        self.reset()
        print("Conducting a Greedy Best First Search:")
        self.frontier = []
        self.head = node()
        self.frontier.append(self.start)
        alreadyExpanded = []        
        temp = None
        x = 0
        loop = False
        self.greedyNodesViewed = 1
        while(self.frontier != []):
            if(len(self.frontier) > self.greedyMaxFrontierQueue): #to get the largest size of queue
                self.greedyMaxFrontierQueue = len(self.frontier)
            temp = self.getGreedyExpansionNode()  
            for y in alreadyExpanded:
                if(y.position == temp.position):
                    x+=1
            if(temp.isGoal() == True):  
                self.greedyPath = temp.currentPath
                self.greedySearchMaze.formatMaze(self.greedyPath)
                break
            self.greedySearchMaze.toggleNodeExpanded(temp)            
            self.greedyExpand(temp)            
            self.greedyNodesExpanded += 1
            if(self.greedySearchMaze.isExpanded(temp) == True):
                alreadyExpanded.append(temp)
            if(x >1):#infinite loop detected
                loop = True
                self.greedyPath = temp.currentPath
                break            
        if(loop == True):
            self.greedySearchMaze.formatMaze(self.greedyPath)
            print("Search Complete")
            print("The Search resulted in an infinite loop and thus did not find a solution")
            print("Greedy Best First Search Followed the following path:")
            print(self.greedyPath)
            print("Number of nodes in path:", len(self.greedyPath))
            print("Number of total path cost:", temp.pathCost)
            print("Number of nodes expanded: ", self.greedyNodesExpanded)
            print("Number of nodes viewed: ", self.greedyNodesViewed)
            print("Maximum number of nodes in search queue: ", self.greedyMaxFrontierQueue)
            print("Here is the final Maze:")        
            self.greedySearchMaze.printMaze() #print the final maze
            print()
            print()
            return        
        self.greedySearchMaze.formatMaze(self.greedyPath)
        print("Search Complete")
        print("Greedy Best First Search Path Found:")
        print(self.greedyPath)
        print("Number of nodes in path:", len(self.greedyPath))
        print("Number of total path cost:", temp.pathCost)
        print("Number of nodes expanded: ", self.greedyNodesExpanded)
        print("Number of nodes viewed: ", self.greedyNodesViewed)
        print("Maximum number of nodes in search queue: ", self.greedyMaxFrontierQueue)
        print("Here is the final Maze:")        
        self.greedySearchMaze.printMaze() #print the final maze
        print()
        print()
        
    #expands the current state      
    def greedyExpand(self,tempNode):
        if(tempNode == None):
            return 
        neighbours = tempNode.getNeighboursPosition()
        neighbours = self.greedySearchMaze.validateNotWall(neighbours)
        self.frontier = []
        for x in neighbours:
            newNode = node()
            newNode.position = [x[0],x[1]]
            newNode.cost = self.getGreedyCost(newNode.position)
            newNode.pathCost = tempNode.pathCost + self.getNeighbourCost(tempNode,newNode.position)
            newNode.addPath(tempNode.currentPath)
            newNode.currentPath.append(newNode.position)
            self.greedyNodesViewed += 1
            if(self.isInFrontier(x) == True):
                for x in range(0,len(self.frontier)):
                    if(self.frontier[x].position == newNode.position):
                        if(self.frontier[x].cost > newNode.cost):
                            self.frontier[x] = newNode                       
                continue
            self.greedySearchMaze.toggleNodeViewed(newNode)
            self.frontier.append(newNode)
            
    def getGreedyExpansionNode(self):
        tempNode = None        
        for x in range(0, len(self.frontier)):
            if(tempNode == None):
                tempNode = self.frontier[x]
            else:
                if(tempNode.cost > self.frontier[x].cost):
                    tempNode = self.frontier[x]        
        self.frontier.remove(tempNode)                    
        return tempNode
     
    # h(n) from current to 9,9
    def getGreedyCost(self,myNode):
        d1 = 9 - myNode[0]
        d2 = 9 - myNode[1]        
        d1 = d1*d1
        d2 = d2*d2
        return math.sqrt(d1+d2)      
    
    def aStarSearch(self):
        self.reset()
        print("Conducting an A* Search")
        self.frontier = []
        self.start = node()
        self.frontier.append(self.start)
        temp = None
        self.starNodesViewed = 1
        while(self.frontier != []):
            if(len(self.frontier) > self.starMaxFrontierQueue):
                self.starMaxFrontierQueue = len(self.frontier)
            temp = self.getStarExpansionNode()
            if(temp.isGoal() == True):
                self.starPath = temp.currentPath
                self.starSearchMaze.formatMaze(self.starPath)
                break
            self.starSearchMaze.toggleNodeExpanded(temp)            
            self.starExpand(temp)            
            self.starNodesExpanded += 1             
        print("Search Complete")
        print("A Star Search Path Found:")
        print(self.starPath)
        print("Number of nodes in path:", len(self.starPath))
        print("Number of total path cost:", temp.pathCost)
        print("Number of nodes expanded: ", self.starNodesExpanded)
        print("Number of nodes viewed: ", self.starNodesViewed)
        print("Maximum number of nodes in search queue: ", self.starMaxFrontierQueue)
        print("Here is the final Maze:")        
        self.starSearchMaze.printMaze() #print the final maze
        print()
        print()
        
    #expands the current state      
    def starExpand(self,tempNode):
        if(tempNode == None):
            return 
        neighbours = tempNode.getNeighboursPosition()
        neighbours = self.starSearchMaze.validateFreeOrViewed(neighbours)
        for x in neighbours:
            newNode = node()        
            newNode.position = [x[0],x[1]]
            newNode.pathCost = tempNode.pathCost + self.getNeighbourCost(tempNode,newNode.position)
            newNode.cost = self.getGreedyCost(newNode.position) + newNode.pathCost #g+h           
            newNode.addPath(tempNode.currentPath)
            newNode.currentPath.append(newNode.position)
            self.starNodesViewed += 1
            if(self.isInFrontier(x) == True):
                for x in range(0,len(self.frontier)):
                    if(self.frontier[x].position == newNode.position):
                        if(self.frontier[x].cost > newNode.cost):
                           self.frontier[x] = newNode                       
                continue            
            self.starSearchMaze.toggleNodeViewed(newNode)
            self.frontier.append(newNode)
    
    #return next node from list for A * Search       
    def getStarExpansionNode(self):
        tempNode = None        
        for x in range(0, len(self.frontier)):
            if(tempNode == None):
                tempNode = self.frontier[x]
            else:
                if(tempNode.cost > self.frontier[x].cost):#g+h
                    tempNode = self.frontier[x]       
                    
        returnNode = tempNode
        self.frontier.remove(tempNode)  
        return returnNode
    
    def wallUniform(self):
        self.reset()
        print("Block(7,0) is not passable")
        self.uniformSearchMaze.makeWall()        
        self.uniformSearch()
    
    def wallGreedy(self):
        self.reset()
        print("Block(7,0) is not passable")
        self.greedySearchMaze.makeWall()
        self.greedyBestFirstSearch()
        
    def wallStar(self):
        self.reset()
        print("Block(7,0) is not passable")
        self.starSearchMaze.makeWall()
        self.aStarSearch()
        
newGame = game()
newGame.uniformSearch()
newGame.greedyBestFirstSearch()
newGame.aStarSearch()
newGame.wallUniform()
newGame.wallGreedy()
newGame.wallStar()