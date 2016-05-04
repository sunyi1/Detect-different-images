we need to download opencv for this program first 
After we download opencv package, we can import cv2 in python

opencv and data in the document

we install opencv by using these three comment lines in order to install and set environment 

conda create -n opencv numpy scipy scikit-learn matplotlib python=3

source activate opencv

conda install -c https://conda.binstar.org/menpo opencv3

each time I run program, we need to use "source activate opencv" to set environment, before we run the command line.

For example:

1. source activate opencv

2. python proj3.py Data/02/06.jpg(which is the path of the test image)

3. we can set our trainning set after the first for loop.


