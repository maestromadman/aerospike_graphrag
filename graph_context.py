# from pygraphml import GraphMLParser

# # read .graphml file, (ASSUMING HOMOGENOUS PROPERTIES FOR ALL NODES & EDGES)
# parser = GraphMLParser()
# my_graph = "air-routes-small.graphml"
# graph = parser.parse(my_graph)   #not reasonable at scale 
#                                         # use Graph summary api instead of graphml
#                                         # try more complex llm queries
#                                         # print Gremlin query to troubleshoot if inaccurate

# # NODE PROPERTIES
# node_schema = []
# nodes = graph.nodes()
# node = nodes[1]
# node_properties = node.attributes()
# node_keys = node_properties.keys()
# for key in node_keys:
#     node_schema.append(key)
# # print(node_schema)

# # EDGE PROPERTIES
# edge_schema = []
# edges = graph.edges()
# edge = edges[1]
# edge_properties = edge.attributes()
# edge_keys = edge_properties.keys()
# for key in edge_keys:
#     edge_schema.append(key)
# # print(edge_schema)

# # SCHEMA CONTEXT
# node_schema_str = " ".join(node_schema)
# edge_schema_str = " ".join(edge_schema)
# schema_context = "For Gremlin queries, use these node properties: \n" + node_schema_str + "\nand these edge properties: \n" + edge_schema_str


# ----------------------------------------------------------------------------------------------------------------

#GRAPH SUMMARY




