from gremgen import schem_summ

def clean_grem():
    initial = schem_summ()

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
            "max_tokens":300,
            "stop":["</s>"],
            "echo":False,  # Echo the prompt in the output
            "top_k":1  # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
        }

    # Specify the prompt
    prompt = f"Print just the Gremlin query from this text: {initial}."

    # Generate the text
    res2 = llm(prompt, **generation_kwargs)  # Res is a dictionary

    # Print the generated text
    #return res2["choices"][0]["text"]  # res is short for result
    
    output = res2["choices"][0]["text"] 
    start = output.find(".V")
    end = output.rfind(")") + 1
    gremlin_query = output[start:end]
    return gremlin_query

out = clean_grem()
print(out)







