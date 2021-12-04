


def show_Date(self, date):  # 显示日期
    self.show_msg("日期:" + date.toString("yyyy-MM-dd"))
    # return date.toString("yyyy-MM-dd")


# 时间改变时显示信息
def onTimeChanged(self, time):
    self.time = time.toString('hh:mm')
    self.show_msg(time.toString('hh:mm'))


# 日期改变时显示信息
def onDateChanged(self, date):
    # 年:月:日 [星期]
    self.date = date.toString('yyyy/MM/dd')
    self.show_msg(self.date)
    self.show_msg(date.toString('yyyy/MM/dd [ddd]'))


# 时间日期改变时显示信息
def onDateTimeChanged(self, dateTime):
    self.datetime = dateTime.toString('yyyy/MM/dd, hh:mm:ss')
    self.show_msg(dateTime.toString('yyyy:MM:dd [ddd] hh:mm:ss'))
































def clearAllInfo(self):
    # 清除窗口
    self.DOI_1.setPlainText('')
    self.title_1.setPlainText('')
    self.Presenter_1.setPlainText('')
    self.URL_link_1.setPlainText('')
    self.PDF_link_1.setPlainText('')
    self.text_JC_Browser_1.setPlainText('')
    self.text_paper_Browser_1.setPlainText('')

    self.DOI_2.setPlainText('')
    self.title_2.setPlainText('')
    self.Presenter_2.setPlainText('')
    self.URL_link_2.setPlainText('')
    self.PDF_link_2.setPlainText('')
    self.text_JC_Browser_2.setPlainText('')
    self.text_paper_Browser_2.setPlainText('')

    self.workreport_3.setPlainText('')
    self.Presenter_3.setPlainText('')
    self.text_paper_Browser_3.setPlainText('')