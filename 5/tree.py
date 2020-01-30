
with open('tree/rosalind_tree.txt') as input_data:
	edges = input_data.read().strip().split('\n')
	n = int(edges.pop(0))
	edges = [list(map(int,edge.split())) for edge in edges]
	

connNodes =list()
for i in range(1,n+1):
	connNodes.append({i})

for edge in edges:
	temp_nodes = set()
	nodesToBeDel = []
	for nodes in connNodes:

		if (edge[0] in nodes) and (edge[1] in nodes):
			break

		elif (edge[0] in nodes) or (edge[1] in nodes):
			temp_nodes.update(nodes)
			nodesToBeDel.append(nodes)
			if len(nodesToBeDel) == 2:
				break

	if len(nodesToBeDel) != 0:
		temp_nodes.add(edge[0])
		temp_nodes.add(edge[1])
		for nodes in nodesToBeDel:
			connNodes.remove(nodes)
		connNodes.append(temp_nodes)

print(len(connNodes)-1)