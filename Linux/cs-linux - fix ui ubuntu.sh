
#problem with wifi

sudo apt-get update
sudo apt-get install linux-headers-generic build-essential dkms
sudo apt-get install broadcom-sta-dkms
sudo modprobe wl #boot mode secure must be disabled
sudo reboot


#problem with UI
#https://medium.com/@sundharwinston/ubuntu-graphical-user-interface-gui-not-working-e7ea95f2b24a#:~:text=Sometimes%2C%20the%20graphical%20user%20interface,system%20updates%20or%20package%20installations.
sudo apt-get update
sudo apt-get upgrade

sudo apt install software-properties-common

sudo add-apt-repository universe
sudo add-apt-repository multiverse

sudo apt install tasksel

sudo tasksel #choose debian

sudo reboot

#




