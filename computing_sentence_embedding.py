"""
Basic example of loading a pre trained model 
for generating sentence embedding for a given list of sentences.
"""

from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import logging

### Just some code to print debug information to stdout
np.set_printoptions(threshold=100)

logging.basicConfig(format='%(asctime)s - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S',
	level=logging.INFO,
	handlers=[LoggingHandler()])
###

# load pre trained model based on DistilBERT
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Embed a list of sentences
sentences = ['This framework generates embeddings for each input sentence',
             'Sentences are passed as a list of string.',
             'The quick brown fox jumps over the lazy dog.']
sentence_embeddings = model.encode(sentences)

# The result is a list of sentence embeddings as numpy arrays
for sentence, embedding in zip(sentences, sentence_embeddings):
	print(f"Sentence: {sentence}")
	print(f"Embedding: {embedding}")
	print("")
