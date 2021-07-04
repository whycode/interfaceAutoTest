import json
import xlrd


class Excels(object):
    """构造Excel工具类"""

    def readExcelData(self, rowx):
        """读取rowx行数"""
        book = xlrd.open_workbook(r'。。\Data\data.xlsx')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readUrl(self, rowx):
        """读取接口地址"""
        return self.readExcelData(rowx)[0]

    def readData(self, rowx):
        """读取请求参数"""
        return json.loads(self.readExcelData(rowx)[1])

    def readToken(self, rowx):
        """读取Token"""
        return json.loads(self.readExcelData(rowx)[2])
