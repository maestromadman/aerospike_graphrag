from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import IO
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from clean import clean_grem

# def graph_output():
#     final_grem = clean_grem()
#     if __name__ == '__main__':
#         # Create GraphTraversalSource to remote server.                                                                                                
#         g = traversal().with_remote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))
#         # Read back the new vertex.                                                                                                                    
#         result = g.V().has('company','aerospike').element_map().to_list()
#         print(result)

def match_grem():
    initial = clean_grem()

    from llama_cpp import Llama
    model_path = "./mistral-7b-instruct-v0.1.Q5_K_S.gguf"
    llm = Llama(
            model_path=model_path,
            n_ctx=0,  # Context length to use
            n_threads=16,  # Number of CPU threads to use
            n_gpu_layers=33,  # Number of model layers to offload to GPU
            chat_format="",
            verbose=False
        )
    
    # Set the generation parameters
    generation_kwargs = {
            "max_tokens":400,
            "stop":["</s>"],
            "echo":False,  # Echo the prompt in the output
            "top_k":1  # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
        }

    # Specify the prompt
    sample_queries = "Find the number of airports in this graph: g.V().has('code','DFW')\n Find the number of flights going out of the airport SFO: g.V().hasLabel('airport').count()\n Get all cities with flights that are >4000 miles: g.V().has('code','SFO').outE().count()\n Find all the airports in the USA you can fly to from London Heathrow (LHR): g.V().has('dist', P.gt(4000L)).inV().values('city').dedup()\n g.V().has('code','LHR').out('route').has('country','US').values('code')\n Find all the unique locations in the world and in the US that I can get to from SFO through a 2 hop flight: g.V().has('code', 'SFO').out().out().dedup().fold().project('totalAirportCountFromSFO', 'USAirportCountFromSFO').by(__.unfold().count()).by(__.unfold().has('country', 'US').count())"

    prompt = f"Print just the Gremlin query from this text: {initial} and make sure it is similar to one of these sample queries: {sample_queries}."

    # Generate the text
    res3 = llm(prompt, **generation_kwargs)  # Res is a dictionary

    # Print the generated text
    #return res2["choices"][0]["text"]  # res is short for result
    
    output = res3["choices"][0]["text"] 
    start = output.find(".V")
    end = output.rfind(")") + 1
    matched_gremlin_query = output[start:end]
    return matched_gremlin_query



