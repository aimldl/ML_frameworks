* Draft: 2021-05-27 (Thu)

# Appendix. Full Output Messages

## 1-basic_image_classification-fashion_mnist_mlp-edited
```bash
$ python 1-basic_image_classification-fashion_mnist_mlp-edited.py 
2.4.1
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
32768/29515 [=================================] - 0s 1us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
26427392/26421880 [==============================] - 1s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
8192/5148 [===============================================] - 0s 0us/step
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
4423680/4422102 [==============================] - 0s 0us/step
Epoch 1/10
1875/1875 [==============================] - 5s 2ms/step - loss: 0.6280 - accuracy: 0.7795
Epoch 2/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.3808 - accuracy: 0.8617
Epoch 3/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.3357 - accuracy: 0.8772
Epoch 4/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.3206 - accuracy: 0.8829
Epoch 5/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2908 - accuracy: 0.8925
Epoch 6/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2775 - accuracy: 0.8977
Epoch 7/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2645 - accuracy: 0.9013
Epoch 8/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2502 - accuracy: 0.9062
Epoch 9/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2444 - accuracy: 0.9098
Epoch 10/10
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2369 - accuracy: 0.9102
313/313 - 0s - loss: 0.3437 - accuracy: 0.8839

Test accuracy: 0.883899986743927
(28, 28)
(1, 28, 28)
[[3.0471241e-05 1.8900351e-14 9.9957675e-01 4.4207897e-12 3.8082965e-04
  6.4259729e-07 1.1316726e-05 1.3496255e-16 1.4000721e-10 1.9950882e-17]]
$
```

## 2-basic_text_classification-imdb_embedding_mlp 
```bash
$ python 2-basic_text_classification-imdb_embedding_mlp-edited.py 
2.4.1
Saving the downloaded dataset to ./downloads/aclImdb...
Rachel Griffiths writes and directs this award winning short film. A heartwarming story about coping with grief and cherishing the memory of those we've loved and lost. Although, only 15 minutes long, Griffiths manages to capture so much emotion and truth onto film in the short space of time. Bud Tingwell gives a touching performance as Will, a widower struggling to cope with his wife's death. Will is confronted by the harsh reality of loneliness and helplessness as he proceeds to take care of Ruth's pet cow, Tulip. The film displays the grief and responsibility one feels for those they have loved and lost. Good cinematography, great direction, and superbly acted. It will bring tears to all those who have lost a loved one, and survived.
Found 25000 files belonging to 2 classes.
Using 20000 files for training.
Review b'"Pandemonium" is a horror movie spoof that comes off more stupid than funny. Believe me when I tell you, I love comedies. Especially comedy spoofs. "Airplane", "The Naked Gun" trilogy, "Blazing Saddles", "High Anxiety", and "Spaceballs" are some of my favorite comedies that spoof a particular genre. "Pandemonium" is not up there with those films. Most of the scenes in this movie had me sitting there in stunned silence because the movie wasn\'t all that funny. There are a few laughs in the film, but when you watch a comedy, you expect to laugh a lot more than a few times and that\'s all this film has going for it. Geez, "Scream" had more laughs than this film and that was more of a horror film. How bizarre is that?<br /><br />*1/2 (out of four)'
Label 0
Review b"David Mamet is a very interesting and a very un-equal director. His first movie 'House of Games' was the one I liked best, and it set a series of films with characters whose perspective of life changes as they get into complicated situations, and so does the perspective of the viewer.<br /><br />So is 'Homicide' which from the title tries to set the mind of the viewer to the usual crime drama. The principal characters are two cops, one Jewish and one Irish who deal with a racially charged area. The murder of an old Jewish shop owner who proves to be an ancient veteran of the Israeli Independence war triggers the Jewish identity in the mind and heart of the Jewish detective.<br /><br />This is were the flaws of the film are the more obvious. The process of awakening is theatrical and hard to believe, the group of Jewish militants is operatic, and the way the detective eventually walks to the final violent confrontation is pathetic. The end of the film itself is Mamet-like smart, but disappoints from a human emotional perspective.<br /><br />Joe Mantegna and William Macy give strong performances, but the flaws of the story are too evident to be easily compensated."
Label 0
Review b'Great documentary about the lives of NY firefighters during the worst terrorist attack of all time.. That reason alone is why this should be a must see collectors item.. What shocked me was not only the attacks, but the"High Fat Diet" and physical appearance of some of these firefighters. I think a lot of Doctors would agree with me that,in the physical shape they were in, some of these firefighters would NOT of made it to the 79th floor carrying over 60 lbs of gear. Having said that i now have a greater respect for firefighters and i realize becoming a firefighter is a life altering job. The French have a history of making great documentary\'s and that is what this is, a Great Documentary.....'
Label 1
Label 0 corresponds to neg
Label 1 corresponds to pos
Found 25000 files belonging to 2 classes.
Using 5000 files for validation.
Found 25000 files belonging to 2 classes.
Review tf.Tensor(b'Silent Night, Deadly Night 5 is the very last of the series, and like part 4, it\'s unrelated to the first three except by title and the fact that it\'s a Christmas-themed horror flick.<br /><br />Except to the oblivious, there\'s some obvious things going on here...Mickey Rooney plays a toymaker named Joe Petto and his creepy son\'s name is Pino. Ring a bell, anyone? Now, a little boy named Derek heard a knock at the door one evening, and opened it to find a present on the doorstep for him. Even though it said "don\'t open till Christmas", he begins to open it anyway but is stopped by his dad, who scolds him and sends him to bed, and opens the gift himself. Inside is a little red ball that sprouts Santa arms and a head, and proceeds to kill dad. Oops, maybe he should have left well-enough alone. Of course Derek is then traumatized by the incident since he watched it from the stairs, but he doesn\'t grow up to be some killer Santa, he just stops talking.<br /><br />There\'s a mysterious stranger lurking around, who seems very interested in the toys that Joe Petto makes. We even see him buying a bunch when Derek\'s mom takes him to the store to find a gift for him to bring him out of his trauma. And what exactly is this guy doing? Well, we\'re not sure but he does seem to be taking these toys apart to see what makes them tick. He does keep his landlord from evicting him by promising him to pay him in cash the next day and presents him with a "Larry the Larvae" toy for his kid, but of course "Larry" is not a good toy and gets out of the box in the car and of course, well, things aren\'t pretty.<br /><br />Anyway, eventually what\'s going on with Joe Petto and Pino is of course revealed, and as with the old story, Pino is not a "real boy". Pino is probably even more agitated and naughty because he suffers from "Kenitalia" (a smooth plastic crotch) so that could account for his evil ways. And the identity of the lurking stranger is revealed too, and there\'s even kind of a happy ending of sorts. Whee.<br /><br />A step up from part 4, but not much of one. Again, Brian Yuzna is involved, and Screaming Mad George, so some decent special effects, but not enough to make this great. A few leftovers from part 4 are hanging around too, like Clint Howard and Neith Hunter, but that doesn\'t really make any difference. Anyway, I now have seeing the whole series out of my system. Now if I could get some of it out of my brain. 4 out of 5.', shape=(), dtype=string)
Label neg
Vectorized review (<tf.Tensor: shape=(1, 250), dtype=int64, numpy=
array([[1287,  313, 2380,  313,  661,    7,    2,   52,  229,    5,    2,
         200,    3,   38,  170,  669,   29, 5492,    6,    2,   83,  297,
         549,   32,  410,    3,    2,  186,   12,   29,    4,    1,  191,
         510,  549,    6,    2, 8229,  212,   46,  576,  175,  168,   20,
           1, 5361,  290,    4,    1,  761,  969,    1,    3,   24,  935,
        2271,  393,    7,    1, 1675,    4, 3747,  250,  148,    4,  112,
         436,  761, 3529,  548,    4, 3633,   31,    2, 1331,   28, 2096,
           3, 2912,    9,    6,  163,    4, 1006,   20,    2,    1,   15,
          85,   53,  147,    9,  292,   89,  959, 2314,  984,   27,  762,
           6,  959,    9,  564,   18,    7, 2140,   32,   24, 1254,   36,
           1,   85,    3, 3298,   85,    6, 1410,    3, 1936,    2, 3408,
         301,  965,    7,    4,  112,  740, 1977,   12,    1, 2014, 2772,
           3,    4,  428,    3, 5177,    6,  512, 1254,    1,  278,   27,
         139,   25,  308,    1,  579,    5,  259, 3529,    7,   92, 8981,
          32,    2, 3842,  230,   27,  289,    9,   35,    2, 5712,   18,
          27,  144, 2166,   56,    6,   26,   46,  466, 2014,   27,   40,
        2745,  657,  212,    4, 1376, 3002, 7080,  183,   36,  180,   52,
         920,    8,    2, 4028,   12,  969,    1,  158,   71,   53,   67,
          85, 2754,    4,  734,   51,    1, 1611,  294,   85,    6,    2,
        1164,    6,  163,    4, 3408,   15,   85,    6,  717,   85,   44,
           5,   24, 7158,    3,   48,  604,    7,   11,  225,  384,   73,
          65,   21,  242,   18,   27,  120,  295,    6,   26,  667,  129,
        4028,  948,    6,   67,   48,  158,   93,    1]])>, <tf.Tensor: shape=(), dtype=int32, numpy=0>)
1287 --->  silent
 313 --->  night
Vocabulary size: 10000
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, None, 16)          160016    
_________________________________________________________________
dropout (Dropout)            (None, None, 16)          0         
_________________________________________________________________
global_average_pooling1d (Gl (None, 16)                0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16)                0         
_________________________________________________________________
dense (Dense)                (None, 1)                 17        
=================================================================
Total params: 160,033
Trainable params: 160,033
Non-trainable params: 0
_________________________________________________________________
Epoch 1/10
625/625 [==============================] - 5s 7ms/step - loss: 0.6827 - binary_accuracy: 0.6064 - val_loss: 0.6147 - val_binary_accuracy: 0.7712
Epoch 2/10
625/625 [==============================] - 3s 5ms/step - loss: 0.5800 - binary_accuracy: 0.7806 - val_loss: 0.4975 - val_binary_accuracy: 0.8224
Epoch 3/10
625/625 [==============================] - 3s 5ms/step - loss: 0.4654 - binary_accuracy: 0.8359 - val_loss: 0.4193 - val_binary_accuracy: 0.8474
Epoch 4/10
625/625 [==============================] - 3s 5ms/step - loss: 0.3905 - binary_accuracy: 0.8615 - val_loss: 0.3734 - val_binary_accuracy: 0.8616
Epoch 5/10
625/625 [==============================] - 3s 5ms/step - loss: 0.3434 - binary_accuracy: 0.8742 - val_loss: 0.3447 - val_binary_accuracy: 0.8678
Epoch 6/10
625/625 [==============================] - 3s 5ms/step - loss: 0.3109 - binary_accuracy: 0.8881 - val_loss: 0.3256 - val_binary_accuracy: 0.8720
Epoch 7/10
625/625 [==============================] - 3s 5ms/step - loss: 0.2864 - binary_accuracy: 0.8960 - val_loss: 0.3125 - val_binary_accuracy: 0.8738
Epoch 8/10
625/625 [==============================] - 3s 5ms/step - loss: 0.2662 - binary_accuracy: 0.9025 - val_loss: 0.3029 - val_binary_accuracy: 0.8752
Epoch 9/10
625/625 [==============================] - 3s 5ms/step - loss: 0.2484 - binary_accuracy: 0.9117 - val_loss: 0.2965 - val_binary_accuracy: 0.8776
Epoch 10/10
625/625 [==============================] - 3s 5ms/step - loss: 0.2329 - binary_accuracy: 0.9148 - val_loss: 0.2921 - val_binary_accuracy: 0.8786
782/782 [==============================] - 4s 5ms/step - loss: 0.3100 - binary_accuracy: 0.8736
Loss:  0.31001201272010803
Accuracy:  0.8736000061035156
782/782 [==============================] - 6s 7ms/step - loss: 0.3059 - accuracy: 0.8725
0.8736000061035156
$
```

## keras/python 2_mnist-simple-cnn-keras-edited.py
```bash
$ python 2_mnist-simple-cnn-keras-edited.py
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11493376/11490434 [==============================] - 1s 0us/step
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
Epoch 1/20
1500/1500 [==============================] - 14s 4ms/step - loss: 0.5093 - accuracy: 0.8395 - val_loss: 0.0748 - val_accuracy: 0.9778
Epoch 2/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0921 - accuracy: 0.9715 - val_loss: 0.0526 - val_accuracy: 0.9854
Epoch 3/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0644 - accuracy: 0.9797 - val_loss: 0.0455 - val_accuracy: 0.9873
Epoch 4/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0546 - accuracy: 0.9823 - val_loss: 0.0445 - val_accuracy: 0.9867
Epoch 5/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0479 - accuracy: 0.9856 - val_loss: 0.0352 - val_accuracy: 0.9899
Epoch 6/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0456 - accuracy: 0.9856 - val_loss: 0.0373 - val_accuracy: 0.9895
Epoch 7/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0406 - accuracy: 0.9870 - val_loss: 0.0369 - val_accuracy: 0.9893
Epoch 8/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0365 - accuracy: 0.9883 - val_loss: 0.0382 - val_accuracy: 0.9888
Epoch 9/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0361 - accuracy: 0.9888 - val_loss: 0.0373 - val_accuracy: 0.9896
Epoch 10/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0351 - accuracy: 0.9888 - val_loss: 0.0320 - val_accuracy: 0.9908
Epoch 11/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0325 - accuracy: 0.9890 - val_loss: 0.0337 - val_accuracy: 0.9911
Epoch 12/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0303 - accuracy: 0.9899 - val_loss: 0.0340 - val_accuracy: 0.9905
Epoch 13/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0285 - accuracy: 0.9898 - val_loss: 0.0332 - val_accuracy: 0.9910
Epoch 14/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0264 - accuracy: 0.9908 - val_loss: 0.0325 - val_accuracy: 0.9909
Epoch 15/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0245 - accuracy: 0.9920 - val_loss: 0.0319 - val_accuracy: 0.9916
Epoch 16/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0248 - accuracy: 0.9919 - val_loss: 0.0306 - val_accuracy: 0.9926
Epoch 17/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0210 - accuracy: 0.9926 - val_loss: 0.0312 - val_accuracy: 0.9919
Epoch 18/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0249 - accuracy: 0.9919 - val_loss: 0.0337 - val_accuracy: 0.9909
Epoch 19/20
1500/1500 [==============================] - 6s 4ms/step - loss: 0.0233 - accuracy: 0.9923 - val_loss: 0.0293 - val_accuracy: 0.9930
Epoch 20/20
1500/1500 [==============================] - 5s 4ms/step - loss: 0.0200 - accuracy: 0.9934 - val_loss: 0.0324 - val_accuracy: 0.9923
313/313 [==============================] - 1s 3ms/step - loss: 0.0279 - accuracy: 0.9923
$
```
