# import tensorflow as tf
# import numpy as np
# import json
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from sklearn.preprocessing import LabelEncoder
# import sys

# # Load the intents JSON file
# with open('/home/vivek/Desktop/bot_back/intents.json') as file:
#     data = json.load(file)

# # Extract data from JSON
# training_sentences = []
# training_labels = []
# labels = []
# responses = []

# for intent in data['intents']:
#     for pattern in intent['patterns']:
#         training_sentences.append(pattern.lower())  # Convert to lowercase for consistency
#         training_labels.append(intent['tag'])
#     responses.append(intent['responses'])

#     if intent['tag'] not in labels:
#         labels.append(intent['tag'])

# # Tokenize the training sentences
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(training_sentences)
# vocab_size = len(tokenizer.word_index) + 1

# # Create sequences and pad them
# sequences = tokenizer.texts_to_sequences(training_sentences)
# max_sequence_length = max([len(x) for x in sequences])
# sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# # Create training data
# training_data = np.array(sequences)
# training_labels = np.array(training_labels)

# # Encode the training labels
# label_encoder = LabelEncoder()
# training_labels_encoded = label_encoder.fit_transform(training_labels)

# # Load the saved model
# model = tf.keras.models.load_model("/home/vivek/Desktop/bot_back/chatbot_model.h5")

# # Function to predict response
# def predict_response(text):
#     sequence = tokenizer.texts_to_sequences([text.lower()])  # Convert input to lowercase for consistency
#     padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
#     prediction = model.predict(padded_sequence)
#     predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
    
#     for intent in data['intents']:
#         if intent['tag'] == predicted_label:
#             return np.random.choice(intent['responses'])

# # Get user input from command line arguments
# if __name__ == "__main__":
#     user_input = " ".join(sys.argv[1:])  # Combine command line arguments into a single string
#     response = predict_response(user_input)
#     print(response)


import os
import sys
import json
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


sys.stdout = open(os.devnull, 'w')


with open('intents.json') as file:
    data = json.load(file)


training_sentences = []
training_labels = []
labels = []
responses = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern.lower())  
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])


tokenizer = Tokenizer()
tokenizer.fit_on_texts(training_sentences)
vocab_size = len(tokenizer.word_index) + 1


sequences = tokenizer.texts_to_sequences(training_sentences)
max_sequence_length = max([len(x) for x in sequences])
sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')


training_data = np.array(sequences)
training_labels = np.array(training_labels)


label_encoder = LabelEncoder()
training_labels_encoded = label_encoder.fit_transform(training_labels)

model = tf.keras.models.load_model("chatbot_model.h5")


sys.stdout = sys.__stdout__


def predict_response(text):
    sequence = tokenizer.texts_to_sequences([text.lower()]) 
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict(padded_sequence)
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
    
    for intent in data['intents']:
        if intent['tag'] == predicted_label:
            return np.random.choice(intent['responses'])  


if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])  
    response = predict_response(user_input)
    print(response)  
