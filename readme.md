# Pottermore Spell caster

**This project is deprecated** because Pottermore removed all their game like features :(

In pottermore there was a spell casting minigame thast required a coordinated keyboard presses to cast a certain spell correctly, i thought of a way to automate the keyboard presses so i get consistely accurate spell casts.

I have implemented 3 spells (Locomotor Wibbly, Mimble Wimble, Petrificus Totalus).

The script is written in python and uses [uinput](https://pypi.python.org/pypi/python-uinput) to simulate keyboard presses. 

**Note**: This is inspired by: http://www.hashbangcode.com/blog/using-python-beat-2012-olympic-google-doodles-669.html


## Known issues
- I suspect that the timing will require some tuning for other comupters, but i never tried it.
- I wasn't able to get the accuracy above 143, and sometimes it misses up so the accuracy is between 139 -143 and on most cases it scores 142.
- There is no cli interface, i have to manually comment/uncomment the required spell before running the spell caster.

## Using it
* You need to comment\uncomment the spell you wanna use. 
* Run the script `sudo python spellcaster.py`, It will count 3 seconds then fire up. That gives you time to select the pottermore window and keep it on focus.
* The script needs root access to run, because it has to simulate a keyboard.
