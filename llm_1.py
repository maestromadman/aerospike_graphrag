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

#--------------------------------------------------------------------------------

from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained("llama-2-7b-chat.Q4_0.gguf")
model = AutoModelForCausalLM.from_pretrained("llama-2-7b-chat.Q4_0.gguf")

#Prompt creation
prompt = print("Please ask a question about air routes you are interested in.")
user_query = input()
input_text = user_query + schema_summary #ADD USER INPUT HERE

input_ids = tokenizer.encode(input_text, return_tensors='pt')
output = model.generate(input_ids, max_length=350, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
print(response)
