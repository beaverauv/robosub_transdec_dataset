# Robosub Transdec Dataset
Labeled dataset of obstacles in the RoboSub competition. 

## Data
Each buoy color has its own class, and the gate is detected as two individual posts. The majority of the images are labeled. Most of the labels are of the gate, buoys, channel and some markers, and a network trained with py-faster-rcnn using VGG-16 performs well on these objects.

## Format
The data is in the sloth XML container format, the same format used in the Imagenet dataset. The genDataset.py can be used to generate a randomized set of training and testing data. 

## Usage
The data is freely available to use, but it would be appreciated if teams who use it contribute back to it, to help create a more complete dataset of the obstacles in the robosub competition

## Thanks to
* Montana State University (RoboCatz) for providing the initial data and labels along with their modified version of py-faster-rcnn
* Amador Valley Robotics Club (AVBotz) for providing video and images from transdec

