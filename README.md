# Object-distance-Estimation-and-Collision-warning
A project which uses deep learning to detect and estimate the distance of the detected objects from the monocular camera. An alarm is raised the detected object is in a distance range considered as dangerous.

In this poject we used the TensorFlow implementation of Yolov3 architecture from [pythonlesson](https://github.com/pythonlessons/YOLOv3-object-detection-tutorial/tree/master/YOLOv3-custom-training). We trained our model on the [Kitti](http://www.cvlibs.net/datasets/kitti/) dataset for this model to be detect the road object. This dataset has 9 classes which are 'car', 'Van', 'Truck','person', 'Person_sitting', 'Cyclist', 'Tram', 'Misc' and 'DontCare'
