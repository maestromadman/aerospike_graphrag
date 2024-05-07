from llama_cpp import Llama
from graph_context import schema_context

# Specify the path to your local model file
model_path = "/Users/amallya/gremlin_fun/llama-2-7b-chat.Q4_0.gguf"

# Initialize the Llama model
llm = Llama(
    model_path=model_path,
    n_ctx=200,  # Context length to use
    n_threads=32,  # Number of CPU threads to use
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
question = print("Please ask a question about air routes you are interested in.")
user_query = input()
prompt = user_query + schema_context

# Generate the text
res = llm(prompt, **generation_kwargs)  # Res is a dictionary

# Print the generated text
print(res["choices"][0]["text"])  # res is short for result

