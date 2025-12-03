# https://docs.ollama.com/capabilities/embeddings

import ollama

single = ollama.embed(
  model='nomic-embed-text',
  input='The quick brown fox jumps over the lazy dog.'
)
print(type(single['embeddings'][0][0])) # float
print(len(single['embeddings'][0])) # 768

batch = ollama.embed(
  model='nomic-embed-text',
  input=[
    'The quick brown fox jumps over the lazy dog.',
    'The five boxing wizards jump quickly.',
    'Jackdaws love my big sphinx of quartz.',
  ]
)
print(type(batch['embeddings'][0][0])) # float
print(len(batch['embeddings']))  # 3