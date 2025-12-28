# CopyCAT
Raspberry Pi Portable File Copier

==== 3.5 SPI Touch Screen =====
This project uses 3.5 inch 320×480 resolution SPI touch screen, which is relatively inexpensive but has limitations on touch accuracy and display colours/angles.
More information on the display found on https://www.lcdwiki.com/3.5inch_RPi_Display.
Run the following code to get the Pi to use the attached display,

git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show

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



   
