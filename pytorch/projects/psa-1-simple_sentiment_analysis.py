#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
psa-1-simple_sentiment_analysis.py
PyTorch Sentiment Analysis > Tutorials > 1. Simple Sentiment Analysis
[PyTorch Sentiment Analysis](https://github.com/bentrevett/pytorch-sentiment-analysis)

This tutorial covers the workflow of a PyTorch with TorchText project.
We'll learn how to:
    load data,
    create train/test/validation splits, 
    build a vocabulary,
    create data iterators,
    define a model
    and implement the train/evaluate/test loop.
The model will be simple and achieve poor performance, 
  but this will be improved in the subsequent tutorials.

Google search: sentiment analysis pytorch
"""

import torch
from torchtext import data

SEED = 1234

torch.manual_seed( SEED )
torch.backends.cudnn.deterministic = True

TEXT  = data.Field( tokenize = 'spacy' )
LABEL = data.LabelField( dtype = torch.float )

from torchtext import datasets

train_data, test_data = datasets.IMDB.splits( TEXT, LABEL )

print(f'Number of training examples: {len( train_data)}')
#Number of training examples: 25000
print(f'Number of testing examples: {len( test_data)}')
#Number of testing examples: 25000

print( vars(train_data.examples) )  # TODO
# TypeError: vars() argument must have __dict__ attribute

import random

train_data, valid_data = train_data.split( random_state = random.seed(SEED) )

print(f'Number of training examples: {len( train_data)}')
#Number of training examples: 17500
print(f'Number of validation examples: {len( valid_data)}')
#Number of validation examples: 7500
print(f'Number of testing examples: {len( test_data)}')
#Number of testing examples: 25000

MAX_VOCAB_SIZE = 25_000

TEXT.build_vocab( train_data, max_size = MAX_VOCAB_SIZE )
LABEL.build_vocab( train_data )

print( f"Unique tokens in TEXT vocaburary: {len(TEXT.vocab)}" )
#Unique tokens in TEXT vocaburary: 25002
# <unk> & <pad> tokens means vocaburary size +2.
print( f"Unique tokens in LABEL vocaburary: {len(LABEL.vocab)}" )
#Unique tokens in LABEL vocaburary: 2

# numericalizing
# token -> indexes

print( TEXT.vocab.freqs.most_common(20) )
#[('the', 203887), (',', 193799), ('.', 166116), ('and', 110300), ('a', 109699), ('of', 101118), ('to', 94499), ('is', 76858), ('in', 61492), ('I', 54611), ('it', 53479), ('that', 49460), ('"', 44492), ("'s", 43762), ('this', 42258), ('-', 37422), ('/><br', 35781), ('was', 34893), ('as', 30581), ('with', 30119)]
print( TEXT.vocab.itos[:10] )
#['<unk>', '<pad>', 'the', ',', '.', 'and', 'a', 'of', 'to', 'is']

# string-to-integer for LABEL, either 0 or 1
print( LABEL.vocab.stoi[:10] )  # TODO
#TypeError: unhashable type: 'slice'

# GPU
BATCH_SIZE = 64
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
train_iterator, valid_iterator, test_iterator = data.BucketIterator.splits( (train_data, valid_data, test_data),
                            batch_size = BATCH_SIZE,
                            device = device)

# Build the model
import torch.nn as nn

class RNN( nn.Module ):
    def __init__( self, input_dim, embedding_dim, hidden_dim, output_dim ):
        super().__init__()
        self.embedding = nn.Embedding( input_dim, embedding_dim )
        self.rnn       = nn.RNN( embedding_dim, hidden_dim )
        self.fc        = nn.Linear( hidden_dim, output_dim )

    def forward(self, text):
        # text = [ sent len, batch size]
        
        embedded = self.embedding( text )
        # embedded = [sent len, batch size, emb dim]
        # emb dim is usually 50~250 depending on the vocabulary size.
        
        output, hidden = self.rnn( embedded )
        # output = [sent len, batch size, hid dim]
        # hidden = [1, batch size, hid dim]
        # hid dim is usually 100-500 depending on
        #   the vocalulary size,
        #   the dense vector size,
        #   complexity of the task, and so on.
        
        assert torch.equal( output[-1,:,:], hidden.squeeze(0) )
        return self.fc( hidden.squeeze(0) )
    
# The output dimension is usually the number of classes.
# The output value is between 0 and 1. So 1-d.

INPUT_DIM     = len( TEXT.vocab )
EMBEDDING_DIM = 100
HIDDEN_DIM    = 256
OUTPUT_DIM    = 1

model = RNN( INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM )

def count_parameters( model ):
    return sum( p.numel() for p in model.parameters() if p.requires_grad )

print( f'The model has { count_parameters(model):,} trainable parameters' )

# Train the model
import torch.optim as optim

optimizer = optim.SGD( model.parameters(), lr=1e-3 )

# The loss function is binary cross entropy with logits

criterion = nn.BCEWithLogitsLoss()

model     = model.to( device )

# The criterion function calculate the loss.
criterion = criterion.to( device )

# Write the function to calculate the accuracy.

def binary_accuracy( preds, y ):
    """
    returns accuracy per batch.
    If 8/10 is right, 0.8 is returned, not 8.
    """
    # Round predictions to the closest integer
    rounded_preds = torch.round( torch.sigmoid(preds) )
    correct = ( rounded_preds == y ).float()
    acc = correct.sum() / len( correct )
    
    return acc

# Train function iterates over all examples, one batch at a time.
def train( model, iterator, optimizer, criterion):
    epoch_loss      = 0
    epoch_accuracy  = 0
    
    model.train()
    
    for batch in iterator:
        optimizer.zero_grad()
        predictions = model( batch.text ).squeeze(1)
        loss        = criterion( predictions, batch.label )
        accuracy    = binary_accuracy( predictions, batch.label )
        loss.backward()
        optimizer.step()
        
        epoch_loss      += loss.item()
        epoch_accuracy  += accuracy.item()

    return epoch_loss / len(iterator), epoch_accuracy / len(iterator)

def evaluate( model, iterator, criterion ):
    epoch_loss      = 0
    epoch_accuracy  = 0
    model.eval()  # This turns off dropout & batch normalization
    
    with torch.no_grad():  # To speed up computation with less memory
        for batch in iterator:
            predictions = model( batch.text ).squeeze(1)
            loss        = criterion( predictions, batch.label )
            accuracy    = binary_accuracy( predictions, batch.label )
            
            epoch_loss     += loss.item()
            epoch_accuracy += accuracy.item()


import time

def epoch_time( start_time, end_time ):
    ''''
    returns elapsed_mins, elapsed_secs to compare training times between models
    '''
    elapsed_time = end_time - start_time
    elapsed_mins = int( elapsed_time / 60 )
    elapsed_secs = int( elapsed_time - (elapsed_mins*60))  # TODO: check this out. (elapsed_mins*60)
    
    return elapsed_mins, elapsed_secs

N_EPOCHS = 5

best_valid_loss = float('inf')

for epoch in range( N_EPOCHS ):
    start_time = time.time()
    
    train_loss, train_accuracy = train( model, train_iterator, optimizer, criterion )
    valid_loss, valid_accuracy = evaluate( model, valid_iterator, criterion )

    end_time = time.time()
    
    epoch_mins, epoch_secs = epoch_time( start_time, end_time )
    
    if valid_loss < best_valid_loss:
        best_valid_loss = valid_loss  # Minimum so far
        torch.save( model.state_dict(), 'tut1-model.pt')
    
    print(f'Epoch: {epoch+1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
    print(f'\tTrain Loss: {train_loss:.3f} | Train Accuracy: {train_accuracy*100:.2f}%')
    print(f'\tValidation Loss: {valid_loss:.3f} | Validation Accuracy: {valid_acc*100:.2f}%')

# The accuracy is poor and the loss doesn't decrease much.
# This is due to several issues with the model.

model.load_state_dict( torch.load('tut1-model.pt') )
test_loss, test_accuracy = evaluate( model, test_iterator, criterion )

print(f'Test Loss: {test_loss:.3f} | Test Accuracy: {test_accuracy*100:.2f}%')
