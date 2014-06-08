bypasser
========

Python program that uses a webcam to check for people passing by and triggers behaviours and events

extracting information from the motion detector
--------
the motion detector has two methods that return information about the detected motion:
 - dump(): returns the raw detection data, a vector of times and a vector of positions. It is used in the graphing tool.
 - data(): returns the vector of data regarding the last detection: slope, intercept, y_dev, std_dev

adding new behaviours
--------
Behaviours should comply with the template:
 - init(self,display): constructor for the class
 - push(self,data): method to pass information to he behaviour from the main thread
 - condition(self): check if the specific condition has been met to trigger the behaviour
 - show(self): display the behaviour

