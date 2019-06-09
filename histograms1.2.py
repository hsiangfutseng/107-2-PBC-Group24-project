import matplotlib.pyplot as pyplot
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
import os

class barchart(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.btnLoad = tk.Button(self, text = "直方圖出來吧", height = 1, width = 5, 
		command = self.clickBtnLoad)
		self.cvsMain = tk.Canvas(self, width = 800, height = 800, bg = "white")

		self.btnLoad.grid(row = 0, column = 0, rowspan = 1, sticky = tk.NE + tk.SW)
		self.cvsMain.grid(row = 1, column = 0, rowspan = 5, sticky = tk.NE + tk.SW)

	def clickBtnLoad(self):
		self.makeBarchart()

		self.imageMain = ImageTk.PhotoImage(file = locationForBarchart)
		self.cvsMain.create_image(100, 100, image = self.imageMain, anchor = tk.NW) # anchor 設定顯示位置
		os.remove(locationForBarchart)

	def makeBarchart(self):
		pyplot.title("Scores of 3 Indicator")
		pyplot.xlabel("Scores")
		indicator = ("Indicator1", "Indicator2", "Indicator3")
		width = 0.2

		pyplot.barh(indicator, scrList, align = "center")

		# pyplot.show()
		pyplot.savefig(locationForBarchart, dpi = 100) # dpi太多會爆

scrList = [30, 40, 20]  # 這邊輸入分數

locationForBarchart = "D:\\商管程式設計\\期末project\\temp.png"
B1 = barchart()
B1.master.title("Barchart")
B1.mainloop()

