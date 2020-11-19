import tello_controller
from tello_control_panel_ui import TelloUI

"""Coded by Group Dylan"""
def main():

    drone = tello_controller.TelloController('', 8889)  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
