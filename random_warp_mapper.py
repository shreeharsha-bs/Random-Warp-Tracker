# Using graph data structures to act as a random warp zone tracker in Pokemon warp games
# With this tracker, keep track of Gyms, elite 4 memebers, warp zones and also get a printed path to anywhere you want to go
# I want to write this so that adding new nodes/vertices (which act as names to locations) is easy. There's no inherent edge cost that I want to deal with. I also won't use adjaceny matrices since the matrix will be largely sparse and adding new rows and columns is generally a pain point with matrices in python.

#import pdb
from itertools import chain

class random_warp_Graph:
	def __init__(self):
		self.graph = dict() # The mapper will be a dictionary

	def addPath(self, node1, node2, directions): # You should add a path based on your source, target and the path you took and the place you reached
		if node1 not in self.graph:		# Example: You can say add path: Floraroma_town oldale_town Left_building_3-->5th_building_right
		    self.graph[node1] = []		# That means if you are in oldale town then you can get to floraroma town 5th right building from the 3rd left
		if node2 not in self.graph:		# building in oldale town and viceversa. If it is a one way please specify so.
		    self.graph[node2] = []

		self.graph[node2].append((node1,directions))
		self.graph[node1].append((node2,"Follow in REVERSE!: "+directions))

	def printGraph(self):
		for source, destination in self.graph.items():
		    print(f"{source}-->{destination}")


def build_graph():
	g = random_warp_Graph()
	mode = 0
	print("Please enter directions like: Source Target PATH_YOU_TOOK_AND_WHERE_IT_LED")
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

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

def flatten(l):
    return [item for sublist in l for item in sublist]

def PathFinder(source,target,g):
	#Convention is PathFinder(source, destination, Map object so far)
	map1 = g.graph
	path_success = 0
	if target in map1:
		print(target + " is a valid destination, finding path...")
		source_init=source
		source = [source]
		old_source = []
		nb = []
		#prev = ['Dummy variable with long name, so it\'s never confused']
		#print(source_init)
		while(path_success==0):
			for y in source:
				neighbours = flatten(map1[y])[::2] # Cleaning up the format of the neighbours, I hate doing stuff like this. Learn to use queues..nooooo

				for neigh_loc in neighbours:
					#print(neigh_loc)
					if([neigh_loc] in old_source or neigh_loc in old_source):
						continue # Won't visit neighbours if he's already been visited once before
					else:
						if(target in neigh_loc):
								path_success = 1
								prev = y
								parent = target
									# No back traces again because there might be one ways, we'll have to rely on old_source
								break

			else:
				#pdb.set_trace()
				n_old = neighbours
				neighbours = flatten([map1[temp] for temp in source])
				#pdb.set_trace()
				neighbours = list(chain.from_iterable(neighbours))[::2]
				neighbours = list(set(neighbours))
				#nb += [neighbours]

				if(source_init in source and len(source)!=1):
					source.remove(source_init)

				old_source.append(source)

				if(path_success == 1):
						old_source_bt = old_source[::-1]
						old_source_bt[0]= [prev]
						for index in range(0,len(old_source_bt)):
							if(len(old_source_bt[index])==1):
								continue
							#pdb.set_trace()
							#print(index)
							old_source_bt[index] = common_elements(list(chain.from_iterable(map1[old_source_bt[index-1][0]]))[::2],old_source_bt[index])
							if(len(old_source_bt[index])!=1):
								old_source_bt[index] = [old_source_bt[index][0]]


				source = neighbours
		#print(target)
		old_source_bt.insert(0,[target])
		output = old_source_bt[::-1]
		return output

#In [39]: PathFinder('T7','S',map1)
#S is a valid destination, finding path...
#Out[39]: [[['T7'], ['T6'], ['T2', 'T5']], 'S']

	else:
		print("Invalid destination, check spellings etc.")
		return 0


if __name__ == "__main__":
	map1 = build_graph()
	output = PathFinder('S','T6',map1)
	print(output)

'''
Use case:
S T1 L1
S T2 L2
T1 T3 L13
T1 T4 L14
T2 T5 L25
T2 T6 L26
T5 T6 L56
T5 T7 L57
T6 T7 L67
2
'''
