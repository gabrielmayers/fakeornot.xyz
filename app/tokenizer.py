from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

vocab_size = 5000
embedding_dim = 16
max_length = 500
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<OOV>'

def lets_token(sentence):
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(sentence)
    word_index = tokenizer.word_index

    sequences = tokenizer.texts_to_sequences(sentence) # TOKENIZE
    sequences_padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type) # PAD

    return sequences_padded