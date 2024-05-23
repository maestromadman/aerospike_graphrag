# from gremlin_python.process.anonymous_traversal import traversal
# from gremlin_python.process.traversal import IO
# from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.driver.client import Client
from clean import clean_grem

final_grem = clean_grem()
# print(final_grem)

def graph_output():
    
    if __name__ == '__main__':
                                                                                                   
        client = Client('ws://localhost:8182/gremlin', 'g')
        try:
            result = client.submit(final_grem).all().result()
        finally:
            client.close()
        return result

out = graph_output()
print(out)
        


