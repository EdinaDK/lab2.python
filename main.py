class Pagination:

    def __init__(self, items=[], pageSize = 0, tag = 0):
        self.items = items
        self.pageSize = pageSize
        self.tag = tag

    # Предыдущая страница
    def PrevPage(self):
        self.tag -= 1
        return self

    # Следующая страница
    def NextPage(self):
        self.tag += 1
        return self

    # Первая страница
    def FirstPage(self):
        self.tag = 0
        return self

    # Последняя страница
    def LastPage(self, items, pageSize):
        self.tag = int(len(self.items) / pageSize)
        if self.tag * pageSize == len(self.items):
            self.tag -= 1
        return self

    # Переход на страницу
    def GoToPage(self):
        print("Enter number: ")
        a = input()
        count = int(a)
        if count > len(self.items) / self.pageSize: # если введенный номер страницы больше максимальной
            self.LastPage(_lst, self.pageSize)      # выводим последнюю страницу
        else:
            self.tag = self.pageSize * (count - 1)
        return self

    # Получить видимые элементы
    def GetVisibleItems(self):
        n = self.items[self.tag * pageSize: self.tag * self.pageSize + self.pageSize]
        return n


m = float(input())
pageSize = int(m)
print("pageSize = ", pageSize)

alphabetList = "abcdefghijklmnopqrstuvwxyz"
p = Pagination(alphabetList, pageSize)
print("alphabet = ", alphabetList)
_lst = list(alphabetList)

print("first page = ", p.GetVisibleItems())

p.NextPage()
print("next page = ", p.GetVisibleItems())

p.LastPage(alphabetList, pageSize)
print("last page = ", p.GetVisibleItems())

p.GoToPage()
print("go to page = ", p.GetVisibleItems())