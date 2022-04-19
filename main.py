class Pagination:
    def __init__(self, items=[], pageSize = 10, flag=0):
        self.items = items
        self.pageSize = pageSize
        self.flag = flag

    def GetVisibleItems(self):
        a = self.items[self.flag * pageSize: self.flag * self.pageSize + self.pageSize]
        return a

    def NextPage(self):
        self.flag += 1
        return self

    def PrevPage(self):
        self.flag -= 1
        return self

    def GotoPage(self):
        print("Input")
        w = float(input())
        count = int(w)
        if count > len(self.items) / self.pageSize:
            self.LastPage(_lst, self.pageSize)
        else:
            self.flag = self.pageSize * (count - 1)


        return self

    def FirstPage(self):
        self.flag = 0
        return self

    def LastPage(self, items, pageSize):
        self.flag = int(len(self.items) / pageSize)
        if self.flag * pageSize == len(self.items):
            self.flag -= 1
        return self

print("Input pagesize")
q = float(input())
pageSize = int(q)
print(pageSize)

alphabetList = "abcdefghijklmnopqrstuvwxyz"
_lst = list(alphabetList)
print(_lst)
p = Pagination(alphabetList, pageSize, 0)

data_output = p.GetVisibleItems()

print(data_output)
p.NextPage()
print(p.GetVisibleItems())
p.GotoPage()
print(p.GetVisibleItems())
