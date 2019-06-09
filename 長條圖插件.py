

        self.makeBarchart(self)
        
        self.imageMain = ImageTk.PhotoImage(file = locationForBarchart)
        self.bar_chart.create_image(50, 100, image = self.imageMain, anchor = tk.W) # anchor 設定顯示位置
        os.remove(locationForBarchart)

    @staticmethod
    def makeBarchart(self):
        pyplot.title("Scores of 3 Indicator")
        pyplot.xlabel("Scores")
        indicator = ("Indicator 1", "Indicator 2", "Indicator 3")
        width = 0.35

        pyplot.barh(indicator, scrList, align = "center")
        pyplot.savefig(locationForBarchart, dpi = 40) # dpi太多會爆

locationForBarchart = "D:\\商管程式設計\\期末project\\temp.png"
scrList = [30, 40, 20]  # 這邊輸入分數

