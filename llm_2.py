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
    
    # def iterate_nested_dict(dictionary):
    #     for key, value in dictionary.items():
    #         if isinstance(value, dict):
    #             iterate_nested_dict(value)
    #         else:
    #             print(key, value)
    
    # schema_summary = iterate_nested_dict(summary)

    def iterate_nested_dict(dictionary):
        result = ""
        for key, value in dictionary.items():
            if isinstance(value, dict):
                result += iterate_nested_dict(value)
            else:
                result += f"{key} {value}\n"
        return result

schema_summary = iterate_nested_dict(summary)
print(schema_summary)



from llama_cpp import Llama

# Specify the path to your local model file
model_path = "./llama-2-7b-chat.Q4_0.gguf"

# Initialize the Llama model
llm = Llama(
    model_path=model_path,
    n_ctx=0,  # Context length to use
    n_threads=16,  # Number of CPU threads to use
    n_gpu_layers=0  # Number of model layers to offload to GPU
)

# Set the generation parameters
generation_kwargs = {
    "max_tokens":100,
    "stop":["</s>"],
    "echo":False,  # Echo the prompt in the output
    "top_k":1  # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

# Specify the prompt
question = print("Ask for a gremlin query to traverse the air-routes graph.")
user_query = input()
prompt = user_query + schema_summary

# Generate the text
res = llm(prompt, **generation_kwargs)  # Res is a dictionary

# Print the generated text
print(res["choices"][0]["text"])  # res is short for result
