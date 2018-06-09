# Semantic Soft Segmentation
http://people.inf.ethz.ch/aksoyy/sss/


## What do I need:
- Image input&output (with opacity)
- deep neural network
- eigen vector
- minimize an energy function
- SLIC for generating 'superpixels'


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





