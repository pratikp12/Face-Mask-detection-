# Face-Mask-detection-

### Table of content

1. [Description](#description)
2. [Requirements](#requirements)
3. [Library](#library)
4. [Steps](#steps)
5. [Conclusion](#conclusion)



<a name="description"></a>
## Description
This is a simple facemask Detection python program.This is based on OpenCV library which is used for image processing.I have worked on 2 approch.
1. Face Detection
2. Nose Detection

### Haar Cascade Classifier

It is a machine learning based approach where a cascade function is trained from a lot of positive (images with face) and negative images (images without face). The algorithm is proposed by Paul Viola and Michael Jones.

The algorithm has four stages:

1. **Haar Feature Selection:** Haar features are calculated in the subsections of the input image. The difference between the sum of pixel intensities of adjacent rectangular regions is calculated to differentiate the subsections of the image. A large number of haar-like features are required for getting facial features.
2. **Creating an Integral Image:** Too much computation will be done when operations are performed on all pixels, so an integral image is used that reduce the computation to only four pixels. This makes the algorithm quite fast.
3. **Adaboost:** All the computed features are not relevant for the classification purpose. `Adaboost` is used to classify the relevant features.
4. **Cascading Classifiers:** Now we can use the relevant features to classify a face from a non-face but algorithm provides another improvement using the concept of `cascades of classifiers`. Every region of the image is not a facial region so it is not useful to apply all the features on all the regions of the image. Instead of using all the features at a time, group the features into different stages of the classifier.Apply each stage one-by-one to find a facial region. If on any stage the classifier fails, that region will be discarded from further iterations. Only the facial region will pass all the stages of the classifier.  

<a name="requirements"></a>
## Requirements

<a name="library"></a>
## Library

<a name="steps"></a>
## Steps


<a name="conclusion"></a>
## Conclusion

