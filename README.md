# Aerospike Graph Rag (in progress...)
This demo uses Aerospike's Graph Database for RAG with an LLM. 
As of **May 15, 2024**, this project is incomplete, but Gremlin queries can be generated using the air-routes-latest.graphml dataset and a Mistral LLM model. I will first get this set up as a chat bot and then swap out this dataset with a more meaningful, large-scale graph used by Aerospike's Graph team. I am also currently exploring the use of LangChain.

## Clone this Repo
To clone this repo, open up your command line and use `git clone` followed by this repository's URL (found by clicking the green <> Code button and copying the HTML link). Select a folder where you want this repo to exist on your local machine and make this your current directory with `cd [/path/to/your/folder]`

## Download an LLM from HuggingFace
For this demo, I chose the quantized Q5_K version of the [TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) model. TheBloke's Hugging Face page offers quantized versions of various LLM models for folks who have less RAM but want to run models locally. I used the Q5_K version because I was running the model on a 24 GB Macbook Air (M3); it generated solid Gremlin queries to the vast majority of my prompts.

Again, make sure you're in the right folder where you want to download the model. 
In your CLI, run the following: 
```
pip install huggingface_hub
hf user login #you may need to use an authentication token from your HuggingFace profile
hf hub download --model TheBloke/llama-2-7b-chat.Q4_0.gguf
```
The model is now downloaded in this repo's local folder on your machine!

## Aerospike Graph Setup 
Follow the steps on [Aerospike.com](https://aerospike.com/docs/graph/getting-started/installation) for Aerospike Graph installation. You will run it with Docker. When you get to the Configuration step, I have provided a simple configuration file called 'aerospike-graph.properties' within the repo. 

## Virtual Environment & Download Requirements
Make sure you are still in this repo directory/folder. Create a virtual environment and use a valid Python version. 
I like to use 3.11. There is a requirements.txt file in this folder. To make sure you have all your dependencies installed in your virtual environment (.venv), run:
```
pip install -r requirements.txt

```

## Running
Navigate to the `llamacpp_gremgen.py` and run the file. You should see some LLM configuration text pop up, in addition to a prompt. Try asking something like "Find all outbound flights from Austin." You should get a Gremlin query in response. Once this demo is fully developed, this will be fed to Aerospike Graph to get a result, and this in turn will be sent back to the LLM to generate a natural language response.









