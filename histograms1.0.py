import matplotlib.pyplot as py
import csv

"""
def findScores(fileName)
	fh = open(fileName, "r")
	csvFile = csv.DictReader(fh)
	
	scores = dict()
	scrList = []
	
	for row in csvFile:
		scrList = int(row["   "])

	fh.close()
"""

scrList = [30, 40, 20]

indicator = ("Indicator 1", "Indicator 2", "Indicator 3")
width = 0.35

py.barh(indicator, scrList, align = "center")
py.title("Scores of 3 Indicator")
py.xlabel("Scores")

py.show()




