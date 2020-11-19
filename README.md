# Drone Controller Application for Tello Edu By Group Dylan
## Dependencies
- Python 3
- tkinter
- cv2
- numpy
- Pillow

## Steps to install the dependencies
<b>Use Linux or Windows Subsystems if you don't want to waste time on installation</b>
### Linux : (Much more easier to setup compared to Windows)
`

    sudo apt-get install python3.6 python-pip -y
    sudo pip install --upgrade pip

    sudo apt-get install libboost-all-dev -y
    sudo apt-get install libavcodec-dev -y
    sudo apt-get install libswscale-dev -y
    sudo apt-get install python-numpy -y
    sudo apt-get install python-matplotlib -y
    sudo pip install opencv-python
    sudo apt-get install python-imaging-tk
`

### Windows : 
- Go find online one by one on the internet to download the installation files. 

## Steps to run the application:
- Step 1 - Install the dependencies
- Step 2 - python main.py

FAQ:
1. Error running the app.
   Ans: Check python version via python --version. If you have installed python3 and the python --version gives u the python2 version. Try use python3 instead. Eg. python3 main.py
   If it still does not work go to your environmental variables, find the python3 path, move the python3 path to the top.