from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import IO
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from clean import clean_grem

def graph_output():
    final_grem = clean_grem()
    if __name__ == '__main__':
        # Create GraphTraversalSource to remote server.                                                                                                
        g = traversal().with_remote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))
        # Read back the new vertex.                                                                                                                    
        result = g.V().has('company','aerospike').element_map().to_list()
        print(result)




