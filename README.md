PositionRanker

The package is composed of a "final" folder which contains the final program and its different files. 

And a "guide" folder which contains different guides to better understand the code.

In this version, the program will first retrieve the first nb of search results for the keywords contained on a google sheet page. Then, it will extract from these queries the lines containing the desired domain names (names of the sheets in the google sheet file). This data is then sent to the google sheet. And will then be filtered on the page corresponding to the appropriate domain name.

To run the program, just go to the "final" directory and enter the command in the terminal: python3 positionRanker.py (or use a python compiler, e.g. Thonny). Once the program is launched, it will ask you to enter the id of the workbook you want to work on.

/!\The workbook must be similar to the one used as an example /!\

Make sure that the user you want to connect with has the rights. For this part, look at the file guidePython~GoogleSheets.txt in the guide folder.

