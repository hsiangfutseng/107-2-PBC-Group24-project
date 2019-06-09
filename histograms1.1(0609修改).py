import matplotlib.pyplot as pyplot
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
import os

class Histogram(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.btnLoad = tk.Button(self, text = "直方圖出來吧", height = 1, width = 5, 
		command = self.clickBtnLoad)
		self.cvsMain = tk.Canvas(self, width = 1920, height = 1080, bg = "white")

		self.btnLoad.grid(row = 0, column = 0, rowspan = 1, sticky = tk.NE + tk.SW)
		self.cvsMain.grid(row = 1, column = 0, rowspan = 5, sticky = tk.NE + tk.SW)

	def clickBtnLoad(self):
		self.makeHistogram()

		self.imageMain = ImageTk.PhotoImage(file = "D:\\商管程式設計\\期末project\\temp.png")
		self.cvsMain.create_image(200, 300, image = self.imageMain, 
		anchor = tk.CENTER) # anchor 設定顯示位置
		os.remove("D:\\商管程式設計\\期末project\\temp.png")

	def makeHistogram(self):
		pyplot.title("Scores of 3 Indicator")
		pyplot.xlabel("Scores")
		indicator = ("Indicator 1", "Indicator 2", "Indicator 3")
		width = 0.35

		pyplot.barh(indicator, scrList, align = "center")

		# pyplot.show()
		pyplot.savefig("D:\\商管程式設計\\期末project\\temp.png", dpi = 100) # dpi太多會爆

scrList = [30, 40, 20]  # 這邊輸入分數

H1 = Histogram()
H1.master.title("Histogram")
H1.mainloop()

