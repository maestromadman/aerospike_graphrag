from transformers import AutoTokenizer, AutoModelForCausalLM
from graph_context import schema_context
# Initialize the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

prompt = print("Please ask a question about air routes you are interested in.")
user_query = input()

# Let's say we have the following input text
input_text = user_query, schema_context                     #ADD USER INPUT HERE

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate a response
output = model.generate(input_ids, max_length=350, temperature=0.7, pad_token_id=tokenizer.eos_token_id)

# Decode the response
response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

print(response)
