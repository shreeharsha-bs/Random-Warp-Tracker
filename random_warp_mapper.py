# Using graph data structures to act as a random warp zone tracker in Pokemon warp games
# With this tracker, keep track of Gyms, elite 4 memebers, warp zones and also get a printed path to anywhere you want to go
# I want to write this so that adding new nodes/vertices (which act as names to locations). There's no inherent edge cost that I want to deal with. I also won't use adjaceny matrices since the matrix will be largely sparse and adding new rows and columns is generally a pain point with matrices in python.
import pdb

class random_warp_Graph:
	def __init__(self):
		self.graph = dict() # The mapper will be a dictionary

	def addPath(self, node1, node2, directions): # You should add a path based on your source, target and the path you took and the place you reached
		if node1 not in self.graph:		# Example: You can say add path: Floraroma_town oldale_town Left_building_3-->5th_building_right
		    self.graph[node1] = []		# That means if you are in oldale town then you can get to floraroma town 5th right building from the 3rd left 
		if node2 not in self.graph:		# building in oldale town and viceversa. If it is a one way please specify so.
		    self.graph[node2] = []

		self.graph[node2].append((node1,directions))
		self.graph[node1].append((node2,"Follow in REVERSE!:: "+directions))

	def printGraph(self):
		for source, destination in self.graph.items():
		    print(f"{source}-->{destination}")


def build_graph():
	g = random_warp_Graph()
	mode = 0
	print("Please enter directions like: Target Source PATH_YOU_TOOK_AND_WHERE_IT_LED")
	print("Enter '2' if you feel you have traversed enough or if you want to Find a path")
	while(mode==0):
#		pdb.set_trace()
		user_input = input()	
		if(user_input=='2'):
			mode = 1
		else:
			node1, node2, directions = user_input.split(' ')
			g.addPath(node1, node2, directions)
		
	g.printGraph()
	return g

def PathFinder(target,source,g):
	#Convention is PathFinder(destination, source, Map so far)
	map1 = g.graph
	#pdb.set_trace()
	path_success = 0
	path = [target]
	if target in map1:
		print("This is a valid destination, finding path...")
		nested_neigh = map1[source]
		#pdb.set_trace()
		path_taken = []
		while(path_success==0):
			for neigh_loc in nested_neigh:
				if(target in [i[0] for i in nested_neigh]):
					print(source + " --> " + neigh_loc[1] + " --> " + neigh_loc[0])
					path_success = 1
					break
			else:					
				#print("level count")
				nested_neigh = map1[neigh_loc[0]]
				source = neigh_loc[0]
				#tracer = ([i[0] for i in nested_neigh].index(target))
				path+=[nested_neigh]
	
		print(path)
	else:
		print("Invalid destination, check spellings etc.")
		return 0
	

