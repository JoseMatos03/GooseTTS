import xgboost as xgb
import numpy as np
import pandas as pd
from app.nlp.tokenizer import Tokenizer  # Import the Tokenizer class

# Load the saved model
model_path = r'/Users/josematos/Dev/Projects/GooseTTS/models/normalization/xgb_model'
model = xgb.Booster()
model.load_model(model_path)

# Define the same parameters used during training
max_num_features = 10
pad_size = 1
boundary_letter = -1
space_letter = 0

# Define the class labels (as used during training)
labels = np.array(['PLAIN', 'PUNCT', 'DATE', 'LETTERS', 'CARDINAL', 'VERBATIM', 'DECIMAL',
                   'MEASURE', 'MONEY', 'ORDINAL', 'TIME', 'ELECTRONIC', 'DIGIT',
                   'FRACTION', 'TELEPHONE', 'ADDRESS'])

# Initialize the tokenizer
tokenizer = Tokenizer()


def preprocess_token(token):
    """Preprocess a token in the same way as the training data."""
    x_row = np.ones(max_num_features, dtype=int) * space_letter
    for xi, i in zip(list(str(token)), np.arange(max_num_features)):
        x_row[i] = ord(xi)
    return x_row


def context_window_transform(data, pad_size):
    """Apply the same context window transformation as during training."""
    pre = np.zeros(max_num_features)
    pre = [pre for _ in np.arange(pad_size)]
    data = pre + data + pre
    neo_data = []
    for i in np.arange(len(data) - pad_size * 2):
        row = []
        for x in data[i: i + pad_size * 2 + 1]:
            row.append([boundary_letter])
            row.append(x)
        row.append([boundary_letter])
        neo_data.append([int(x) for y in row for x in y])
    return neo_data


def predict_sentence(sentence, model, labels):
    """Predict the class for each token in the sentence using the improved tokenizer."""
    tokens = tokenizer.tokenize(sentence)  # Use the Tokenizer class
    x_data = [preprocess_token(token) for token in tokens]
    x_data = context_window_transform(x_data, pad_size)
    x_data = np.array(x_data)

    dmatrix = xgb.DMatrix(x_data)
    predictions = model.predict(dmatrix)

    # Map numerical predictions to class labels
    predicted_labels = [labels[int(x)] for x in predictions]

    return tokens, predicted_labels


def save_predictions_to_csv(tokens, predicted_labels, output_path):
    """Save the predictions to a CSV file."""
    df = pd.DataFrame({
        'token': tokens,
        'predicted_class': predicted_labels
    })
    df.to_csv(output_path, index=False)
