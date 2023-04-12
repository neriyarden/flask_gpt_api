import os
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

def ask_gpt(api_key, prompt):
	os.environ['OPENAI_API_KEY'] = api_key

	# Load you data into 'Documents' a custom type by LlamaIndex
	documents = SimpleDirectoryReader('./data').load_data()

	# Create an index of your documents
	index = GPTSimpleVectorIndex.from_documents(documents)


	# Query your index!
	response = index.query(prompt)

	return str(response)