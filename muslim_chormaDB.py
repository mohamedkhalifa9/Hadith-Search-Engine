import chromadb;

import torch;

# #testing chroma
# chroma_client = chromadb.Client();

# collection = chroma_client.create_collection(name="my_collection")
# collection.add(
#     documents=[
#         "Hassan the king ruled over Aachen city.",
#         "Aachen is a small city filled with big dreams."
#     ],
#     ids=["id1", "id2"]
# )

# results = collection.query(
#     query_texts=["Who's Hassan?"], # Chroma will embed this for you
#     n_results=2 # how many results to return
# )
# print(results)

# #testing transformers
# import pandas as pd
# import glob
# import os

# # Path to your CSV files
import pandas as pd
import glob
import os

# # Path to your CSV files - add /*.csv to get all CSV files in the directory
# path = '/Users/khalifa/Downloads/LK-Hadith-Corpus-master/Muslim/*.csv'  # Note the /*.csv at the end

# # Get all CSV files in the directory
# all_files = glob.glob(path)

# # List to store all dataframes
# dfs = []

# # Read each CSV file and append to list
# for file in all_files:
#     print(f"Reading file: {file}")  # This helps you see which files are being processed
#     df = pd.read_csv(file)
#     dfs.append(df)
    

# # Combine all dataframes
# combined_df = pd.concat(dfs, ignore_index=True)

# # Save to new CSV file
# combined_df.to_csv('/Users/khalifa/Downloads/LK-Hadith-Corpus-master/Muslim/combined_output.csv', index=False)
# print(f"Combined {len(all_files)} files into combined_output.csv")
# print(f"Total rows: {len(combined_df)}")


# tokenizer= AutoTokenizer.from_pretrained("xlm-roberta-large-finetuned-conll03-english");
# model= AutoModel.from_pretrained('xlm-roberta-large-finetuned-conll03-english');

# array=["Hassan the king ruled over Aachen city.",  "Aachen is a small city filled with big dreams."];
# for i in array:
#     token= tokenizer(i, padding=True, return_tensors='pt')
#     outputs= model(**token)
#     embeddings = outputs.last_hidden_state.mean(dim=1) ;

# print(embeddings);

#decided to use normal chroma embbder: Allmini


# df_done = pd.read_csv('/Users/khalifa/Downloads/LK-Hadith-Corpus-master/Muslim/combined_output.csv')

# client = chromadb.PersistentClient(path="/Users/khalifa/Desktop/DBo")
# collection = client.create_collection(name="muslim_hadiths")

# # Generate ids
# ids = [str(i) for i in range(len(df_done))]  # Convert to strings as Chroma requires string ids

# # Convert the pandas series to a list
# documents = df_done['English_Hadith'].tolist()

# collection.add(
#     documents=documents,
#     ids=ids
# )

# print(f"Added {len(ids)} documents to collection")

# import chromadb
# from transformers import MarianMTModel, MarianTokenizer

# # Initialize ChromaDB
# client = chromadb.PersistentClient(path="/Users/khalifa/Desktop/DBo")
# collection = client.get_collection(name="muslim_hadiths")

# # Load Arabic to English translation model
# model_name = "Helsinki-NLP/opus-mt-ar-en"
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# model = MarianMTModel.from_pretrained(model_name)

# # Get user input
# input_text = input('Enter your Hadith Query in Arabic: ')

# # Translate to English
# encoded = tokenizer(input_text, return_tensors="pt", padding=True)
# translated = model.generate(**encoded)
# english_query = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

# # Query the collection
# results = collection.query(
#     query_texts=[english_query],
#     n_results=3
# )
# print(results)

# import chromadb
# from transformers import MBartTokenizer, MBartForConditionalGeneration, AutoModel, AutoTokenizer  # Changed imports

# First install required package
# !pip install tiktoken

# # Initialize ChromaDB
# client = chromadb.PersistentClient(path="/Users/khalifa/Desktop/DBo")
# collection = client.get_collection(name="muslim_hadiths")
# #print(collection.peek())
# tokenizer= AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt");
# model= AutoModel.from_pretrained('facebook/mbart-large-50-many-to-many-mmt');
# input= input('Enter your Hadith Query in Arabic:')

# tokenizer.src_lang = "ar_AR"
# encoded_ar = tokenizer(input, return_tensors="pt")
# generated_tokens = model.generate(
# **encoded_ar,
# forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
# )
# english_query=tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

# results = collection.query(
# query_texts=[english_query],
# n_results=3
# )
# print(results)

