# CopyCAT
Raspberry Pi Portable File Copier

==== 3.5 SPI Touch Screen =====

This project uses 3.5 inch 320×480 resolution SPI touch screen, which is relatively inexpensive but has limitations on touch accuracy and display colours/angles.
More information on the display found on https://www.lcdwiki.com/3.5inch_RPi_Display.
Run the following code to get the Pi to use the attached display,

Connect the Pi to the same local network and enable SSH with a password when installing the Pi OS
Open the Windows Terminal with admin access,

1. ssh username@pi or find the pi IP address from the WIFI router and use username@192.168.1.1 - replace with your IP address

After you have the SSH access, run the following code

1. git clone https://github.com/goodtft/LCD-show.git
2. chmod -R 755 LCD-show
3. cd LCD-show/
4. sudo ./LCD35-show

==== Autostart the app on startup ====

This will make the app autostart on the Pi boot, and this will remove the difficult navigation with 3.5 screen
1. cd .config
2. mkdir autostart
3. cd autostart
4. nano copycat.desktop
5. Enter the following code
   [Desktop Entry]
   Exce=bash -c "sleep 10 && python3 /home/pi/Desktop/main.py"   --- Replace the pi with your device name
6. Copy the code file copycat.pi to your desktop



   
