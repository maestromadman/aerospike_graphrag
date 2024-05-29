from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import IO
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection                                                                                             
from gremlin_python.driver.aiohttp.transport import AiohttpTransport

def schem_summ(q):
    # Create GraphTraversalSource to remote server.     
    connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g', transport_factory=lambda:AiohttpTransport(call_from_event_loop=True))                                                                                       
    g = traversal().with_remote(connection)


    # Sample queries with the air-routes data set. To use these queries, download
            # the data set and load it with the following:
    # g.with_("evaluationTimeout", 24 * 60 * 60 * 1000).\
    # io("/opt/air-routes/air-routes-latest.graphml").\
    # with_(IO.reader, IO.graphml).\
    # read().iterate()                                                                                            

# RAG

    summary = g.call("summary").next()

    edges = {k: v for k, v in summary.items() if k in {'Edge properties by label'}} # <type 'dict'>
    edge_props = edges.get('Edge properties by label', {}).get('route', {})
    edge_props_str = " \n".join(edge_props)

    vertex_props = summary.get('Vertex properties by label', {}).get('airport', {}) # <type 'dict'>
    vertex_props_str = " ".join(vertex_props)
            
    sample_queries = '''How many airports are there in this graph? : g.V().hasLabel('airport').count()\n 
    How many flights are flying out of SFO? : g.V().has('code','SFO').outE().count()\n 
    Find me all cities with flights that are greater than 4000 miles: g.V().has('dist', P.gt(4000L)).inV().values('city').dedup()\n 
    Find all the airports in the USA you can fly to from London Heathrow airport (LHR): g.V().has('code','LHR').out('route').has('country','US').values('code')\n 
    Find all the unique locations in the world and in the US that I can get to from SFO through a 2 hop flight: g.V().has('code', 'SFO').out().out().dedup().fold().project('totalAirportCountFromSFO', 'USAirportCountFromSFO').by(__.unfold().count()).by(__.unfold().has('country', 'US').count())"
    '''
    schema_context = '''\
                Here are some example questions and Gremlin queries that traverse a graph to find their answers: {sample_queries}.
                
                Insert ONLY THESE edge properties ({edge_props}) and THESE vertex properties ({vertex_props}) into a Gremlin query help find the answer to my question.
                
                Question: {question}
                '''


    from llama_cpp import Llama

    # Specify the path to your local model file
    model_path = "./mistral-7b-instruct-v0.1.Q5_K_S.gguf"
    # Initialize the Llama model
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
            "max_tokens":375, #prev 350
            "stop":["</s>"],
            "echo":False,  # Echo the prompt in the output
            "top_k":1  # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
        }

    # Specify the prompt
    # print("\nAsk me a question about air routes!")
    # user_query = input()
    prompt = schema_context.format(edge_props=edge_props_str, vertex_props=vertex_props_str, sample_queries=sample_queries, question=q)

    # Generate the text
    res1 = llm(prompt, **generation_kwargs)  # Res is a dictionary

    # Print the generated text
    return res1["choices"][0]["text"]  # res is short for result

