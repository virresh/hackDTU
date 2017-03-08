#HackDTU

CardioSol 
(A project built by Team CodeChamps for HackDTU)


CardioSol is one of the most efficient and easy ways of detecting the possible occurence of Tachycardia. Capable of detecting your heartbeat rate from the webcam, CardioSol is a must have for one's well - being, as it carries out easy checkups at home. CardioSol does not need Internet connectivity and thus, comes to the rescue of people living in remote areas with poor internet connectivity, connecting them with suitable doctors in their city, in case they are detected with the possible occurence of the disease.

It calculates the patients' heartbeat rate by using the laptop's webcam based on an algorithm. In case, the user shows the symptoms of Tachycardia, it prompts the user to answer a questionnaire, based on which, it suggests the user, suitable remedies or the contact details of suitable doctors.

Requirements:
---------------

- [Python v2.7+](http://python.org/)
- [OpenCV v2.4+](http://opencv.org/), with the cv2 python bindings
- Numpy 

```
sudo apt-get update
sudo apt-get install python-numpy
```
or
```
pip install numpy
```
- Scipy

```
sudo apt-get install python-scipy
```
or
```
pip install scipy
```

- Tkinter

```
sudo apt-get install python-tk
```


Quickstart:
------------

- run pulse.sh to start the application

```
./pulse.sh
```
