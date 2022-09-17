# Game_Highlighter

a highlight extractor that extracts special moments from a video game video (or stream).

you can feed your video or stream to the system and it will summarize the given video to a smaller one with the best moments and actions.

it is very useful for the streamers who have a lot of long videos as the system can provide them an automatic summary instead of extracting the best moments manually (using video editors or something similar).

The system can extract special moments from any kind of games but it is more accurate for the third person shooter games.

# The solution provided

## extract features from video frames

like: the number of characters, the health bar, the amount of motion etc...

using different computer vision algorithms.

## extract features from audio

like: the loudness and the different amplitudes of the sound etc...

## apply unsupervised machine learning algorithm

apply one-class svm algorithm to assign an outlier score for each frame and sort the frames from the most outliers to the least.

then pick from the sorted list of the frames as many frames as you need.

# Results 

our system score 7.35 out of 10 depending on users ratings.