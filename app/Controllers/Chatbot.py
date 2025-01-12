
# from datetime import time
# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import h5py
# from flask import Flask, request, jsonify

# def load_model_from_h5(model, file_path):
#     with h5py.File(file_path, 'r') as h5_file:
#         state_dict = {key: torch.tensor(value[:]) for key, value in h5_file.items()}
#     model.load_state_dict(state_dict)

# def generate_response(prompt, model, tokenizer, max_length=60, temperature=0.8, top_k=50, top_p=0.95):
#     model.eval()  # Mengatur model ke mode evaluasi
#     inputs = tokenizer.encode(prompt, return_tensors="pt") 
#     outputs = model.generate(
#         inputs,
#         max_length=max_length,
#         temperature=temperature,  # Mengontrol keacakan generasi teks
#         top_k=top_k,              # Membatasi pemilihan token ke k teratas
#         top_p=top_p,              # Membatasi pemilihan token ke p teratas (nucleus sampling)
#         pad_token_id=tokenizer.eos_token_id,
#     )
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)


# try:
#     tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#     tokenizer.pad_token = tokenizer.eos_token  # Set pad token
#     model = GPT2LMHeadModel.from_pretrained("gpt2")

#     # Path ke file H5
#     h5_model_path = "./app/Controllers/model.h5"  # Ganti path dengan lokasi model Anda
#     load_model_from_h5(model, h5_model_path)
#     print("Model berhasil dimuat dari file .h5")
# except Exception as e:
#     print(f"Error loading model: {e}")
#     model, tokenizer = None, None


# def chatbot():
#     if model is None or tokenizer is None:
#         return jsonify({'error': 'Model or tokenizer not initialized'}), 500

#     data = request.json
#     if not data or 'message' not in data:
#         return jsonify({'error': 'Message is required'}), 400

#     prompt = data['message']
#     try:
#         response = generate_response(prompt, model, tokenizer)
#         return jsonify({'response': response})
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return jsonify({'error': 'Failed to generate response'}), 500

# # respon_terakhir = None
# # def chatbotMobile():
   
# #     if model is None or tokenizer is None:
# #         return jsonify({'error': 'Model or tokenizer not initialized'}), 500

# #     data = request.json
# #     if not data or 'message' not in data:
# #         return jsonify({'error': 'Message is required'}), 400

# #     prompt = data['message']
# #     try:
# #         response = generate_response(prompt, model, tokenizer)
# #         return jsonify({'response': response})
# #     except Exception as e:
# #         print(f"Error generating response: {e}")
# #         return jsonify({'error': 'Failed to generate response'}), 500
    


from flask import Flask, request, jsonify
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    ServiceContext,
    load_index_from_storage
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
GROQ_API_KEY = "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"

# Define the embedding and LLM models
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L12-v2")
llm = Groq(model="llama-3.2-90b-vision-preview", api_key=GROQ_API_KEY)

# Configure Service Context
service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)

# Define Storage Context
storage_context = StorageContext.from_defaults(persist_dir="C:\storage_mini")

# Load Index
index = load_index_from_storage(storage_context, service_context=service_context)

# Query Engine
query_engine = index.as_query_engine(service_context=service_context)


def chat():
    try:
        # Get user input from request
        user_input = request.json.get('message', '').strip()
        if not user_input:
            return jsonify({'response': 'Pesan kosong, silakan masukkan pesan valid.'}), 400
        
        # Query the LLM
        response = query_engine.query(user_input)
        
        # Return the response
        return jsonify({'response': response.response})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e), 'response': 'Terjadi kesalahan. Silakan coba lagi nanti.'}), 500
