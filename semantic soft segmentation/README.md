# Semantic Soft Segmentation
http://people.inf.ethz.ch/aksoyy/sss/


## What do I need:
- Image input&output (with opacity)
  - using pillow
- deep neural network 
- eigen vector
- minimize an energy function
- SLIC for generating 'superpixels'
  - this is a reference to another paper


## Method(from description):
- define opacity on pixels
- construct Laplacian matrix (representing probability each pair of pixels is in the same layer)
- create layers from eigenvectors of L (using "sparsification")


## Method (from Fig 2.):
- Read image
- image => semantic features
- image => matting affinity
- image => colour affinity
- image (+ semantic features ?) => semantic affinity
- 3 affinities => Laplacian matrix
- Laplacian => eigenvectors
- eigenvectors => initial segments
- initial segments => grouped segments
- grouped segments => final segments
- write (or use) layers

## OK, so step 1 is to implement this other paper (paper or recipe?)... with differences
Canonical link:
- http://liangchiehchen.com/projects/DeepLabv2_resnet.html
- requires 'caffe/kaffe'.. what it is?

TensorFlow reimplementation:
- https://github.com/zhengyang-wang/Deeplab-v2--ResNet-101--Tensorflow
- lists Tensorflow 1.3.0+ as needed (anaconda windows only has 1.1.0)
- TensorFlow on windows seems to be too much trouble.  I guess it's time to resurrect my dual-boot to Linux.

Hello from the linux side. Let me tell you a little story about nvidia-driver... no, it's actually beside the point.

Caffe is a simple apt-get install. But. I can't seem to make the deeplabv2 model work. The internets suggest that caffe models often require a specific version of caffe (sometimes uniquely modified by the model makers). I can't find any suggestion which version the models were made with.

Next stop, TensorFlow...

ok, apparently TensorFlow isn't supported on Debian. I now have Ubuntu up and running happily(ish) and I can even import tensorflow successfully! I suspect none of the cuda libraries are actually set up.. there's talk on the internet about different path env variables.

TensorFlow can now run on my GPU!!!!  All it took was:
- finding CUDA 9.0 from nvidia's website (ubuntu's cuda 9.1 package is too good for TF)
- finding cudnn on nvidia's website (i'm sure i've done this part before but I couldn't find my account info of course)
- compiling tensorflow master branch from source. (something something compute capability 3.0).

