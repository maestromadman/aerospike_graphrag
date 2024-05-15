from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import IO
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection



if __name__ == '__main__':
    # Create GraphTraversalSource to remote server.                                                                                                
    g = traversal().with_remote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))

 # Sample queries with the air-routes data set. To use these queries, download
    # the data set and load it with the following:
    # g.with_("evaluationTimeout", 24 * 60 * 60 * 1000).\
    #   io("/opt/aerospike-graph/data/air-routes-small.graphml").\
    #   with_(IO.reader, IO.graphml).\
    #   read().iterate()                                                                                              

    summary = g.call("summary").next()  
    
    def iterate_nested_dict(dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                iterate_nested_dict(value)
            else:
                print(key, value)
    


   



                                    
                   
