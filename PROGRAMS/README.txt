Jonathan Young jyoun127
Heyun Wang hwang257@jhu.edu

Source Files: 
driver.py: main file of this application, run with command line arguments such as listed below

frame.py: representation of a frame, or transformation matrix from one frame to another. Contains functionality to also manipulate that point cloud.

pivotCalibration.py: methods to perform a pivot calibration when given point clouds

pointCloud.py: representation of a point cloud, and contains methods to perform actions to manipulate point cloud or for registration. 

q4.py: driver for question four, computes the expected values of Contains

q5.py: driver for question five, calibrates the EM marker in a pivot calibration manner relative to the dimple

q6.py driver for question six, performs pivot calibration in EM tracker coordinates for optical tracker pivot

Running parameters: 
Testing: python driver.py tolerance(as float)
Normal input: 
python driver.py xx-calbody.txt xx-calreadings.txt xx-empivot.txt xx-optpivot.txt
