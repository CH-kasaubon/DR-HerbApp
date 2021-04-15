# DR-HerbApp
A python app to organise herbs for an RPG

main.py         - this is the GUI code
params.py       - a parameter file
data_handler.py - this reads the herb CSV file and handles that data
herb.py         - the Herb class file, deals with herb specific stuff
pouch.py        - the Pouch class file, for the herbs you've got to hand
herb.csv        - CSV file full of herb data from Roll20 site
hstock.csv      - currently on stock at the apothecary. this is unlikely to be up to date.

saving the current herb pouch will create a 'pouch_save.csv' file
the app creates a 'herbs_mod.csv' file that tidies up the herb.csv file a bit, because the table on Roll20 has some spelling inconsistencies. There's still an issue with some of the poison names

Built in Python 3.9.  Needs pandas and tkinter.
