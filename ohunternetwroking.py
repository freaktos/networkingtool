# octet hunter wifi penetration hub >_<
import os
import time
import datetime
print(r"""
           ,--,
     _ ___/ /\|
 ,;'( )__, )  ~
//  //   '--; 
'   \     | ^
     ^    ^
""")


selection = input("Welcome to Octethunter Networking Tool! \n Select scenario for wifi's nearby. \n L - Lazy mode do it everything for me >o< \n M - Just take my NIC into monitor mode for me i'll do it other stuffs.\n"
" E - Exit and Take your NIC back to Managed mode.\n").lower()

outputFolder ="OctetHunterNetworkHub"

current_time = datetime.datetime.now().strftime("%Y%m%d_&H&M")
outputFile = f"Scan_{current_time}"

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)
    print(f"'{outputFolder}' Klasörü oluşturuldu.")






if selection == "l":
    os.system("sudo systemctl stop NetworkManager && sudo ifconfig wlan1 down && sudo iwconfig wlan1 mode Monitor && sudo ifconfig wlan1 up && sudo systemctl restart NetworkManager")
    print("Your NIC is now in Monitor mode. Scan is starting in 3 sec.")
    time.sleep(3)
    os.system(f"sudo airodump-ng wlan1 -w {outputFolder}/{outputFile}")
elif selection == "e":
    os.system("sudo systemctl stop NetworkManager && sudo ifconfig wlan1 down && sudo iwconfig wlan1 mode Managed && sudo ifconfig wlan1 up && sudo systemctl restart NetworkManager")
    print("NIC has been successfully turned back to Managed mode. byee!")
elif selection =="m":
    os.system("sudo systemctl stop NetworkManager && sudo ifconfig wlan1 down && sudo iwconfig wlan1 mode Monitor && sudo ifconfig wlan1 up && sudo systemctl start NetworkManager")
    print("Your NIC is now under Monitor mode hence you are the wizard who make magic from now...")
else:
    print("Wrong input, try again.")