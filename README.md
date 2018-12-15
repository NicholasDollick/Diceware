## Diceware 

⚠ Python3 is currently required.

#### Description
A python implementation of diceware. 

Uses a series of simulated dice rolls in order to generate a truly random combination of words, for use as a secure passphrase. 

For more information, visit: www.diceware.com

#### Usage
```
usage: python3 diceware.py -l <password_length> [options]
options:
-l --length           - length of generated password (Default: 5)
-s --secure           - inserts a random character for extra entropy

Examples: 
python3 diceware.py 
python3 diceware.py -l 8
python3 diceware.py -l 6 -s

Output:
tu pam sob ke umbra 
harem lazy moore elsie vivian ogre goal bony 
sal sixty ship force tend uk rite si;x 
```
