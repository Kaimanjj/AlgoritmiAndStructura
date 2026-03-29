#создадим словарь, где ключ - название остановки, значение - список с координатами и временем до следующей остановки 
# stopover_dict = {"Остановка 1": ["Адрес 1",15],
#                  "Остановка 2": ["Адрес 2",13],
#                  "Остановка 3": ["Адрес 3",9],
#                  "Остановка 4": ["Адрес 4",23],
#                  "Остановка 5": ["Адрес 5",5],
#                  "Остановка 6": ["Адрес 6",8]}

#Класс для нахождения индекса выбранной остановки в списке
class IndexOstanovki:
    @staticmethod
    def OpredOstanovki(stopover_list,current_stopover):
        k=0
        for i in range(len(stopover_list)-1):
            if stopover_list[i][0]==current_stopover:
                return k
            k+=1
        return k


#добавление остановки 
class Add_Stopover:
    def __init__(self,stopover_list,name_stopover , address_stopover , time_stopover):
        self.stopover_list = stopover_list
        self.name_stopover = name_stopover
        self.address_stopover = address_stopover
        self.time_stopover = time_stopover
    def AppendInList(self):
        time_stopover_int = int(self.time_stopover)
        self.stopover_list.append([self.name_stopover,self.address_stopover,time_stopover_int])
    def __str__(self):
        return f'Конечный список маршрута автобуса:{self.stopover_list}'
        

#расчет общего времени маршрута
class AllTime:
    def __init__(self,stopover_list):
        self.stopover_list = stopover_list
        self.time_way = 0
    def RaschetTime(self):
        for i in self.stopover_list:
            self.time_way += i[2]
    def __str__(self):
        return f'Общее время маршрута:{self.time_way}'

#Определение, где будет автобус через N остановок
class DeltaStopover:
    def __init__(self,stopover_list, dop_class_index):
        self.stopover_list = stopover_list
        self.dop_class_index = dop_class_index
        self.kolichestvo = 0
        self.count_stopover = 0
    def OpredelenieStopover(self):
        current_stopover_1 = input('Напишите название остановки, на которой сейчас находится автобус:\n')
        self.count_stopover = int(input("Напишите количество остановок, которые должен проехать автобус:\n"))

        self.kolichestvo = self.dop_class_index.OpredOstanovki(self.stopover_list,current_stopover_1)
    def __str__(self):
        return f'Через {self.count_stopover} остановок автобус будет на остновке под названием:{self.stopover_list[self.count_stopover+self.kolichestvo][0]}'

#построение обратного маршрута 
class ReturnRoute():
    def __init__(self, stopover_list, dop_class_index):
        self.stopover_list = stopover_list
        self.dop_class_index = dop_class_index #полезная штука вызова метода из одного класса в другой, запомнить и не забыть вновь
        self.novai_stopover_list = []
        self.novai_name_stopover = []
    def FindRoute(self):
        current_stopover_2 = input('Напишите название остановки, на которой сейчас находится автобус:\n')
        tekush_ost = self.dop_class_index.OpredOstanovki(self.stopover_list,current_stopover_2) #использование
        for i in range(tekush_ost-1,-1,-1):
            self.novai_stopover_list.append(self.stopover_list[i])
        self.novai_name_stopover = [self.novai_stopover_list[i][0] for i in range (tekush_ost)]
    def __str__(self):
        return f'Обратный маршрут выглядит так:\n{self.novai_name_stopover}'

#Класс для вывода маршрута в формате таблицы
class Spreadsheet:
    def __init__(self,massiv):
        self.name_massiv = [massiv[i][0] for i in range(len(massiv))]
        self.headers = ["№", "Остановка"]
    def FormatTabl(self):
        col_widths = [
        max(len(str(len(self.name_massiv))), len(self.name_massiv[0])),  # ширина для номера
        max(max(len(stop) for stop in self.name_massiv), len(self.name_massiv[1]))]  # ширина для названия
        separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
        #ДОДУМАТЬ ИДЕЮ С ВЫВОДОМ ТАБЛИЦЫ
        print(separator)
        header_row = f"| {headers[0]:^{col_widths[0]}} | {headers[1]:^{col_widths[1]}} |"
        print(header_row)
        print(separator)
        
        # Выводим остановки
        for i, stop in enumerate(stops, 1):
            row = f"| {i:^{col_widths[0]}} | {stop:<{col_widths[1]}} |"
            print(row)
        
        print(separator)



class Main():
    #так как надо работать со списками, создадим список со списками с аналогичными значениями
    stopover_list = [["Остановка 1","Адрес 1",15],["Остановка 2","Адрес 2",13],["Остановка 3","Адрес 3",9],["Остановка 4","Адрес 4",23],["Остановка 5","Адрес 5",5],["Остановка 6","Адрес 6",8]]
    print("=" * 80)
    print("***ВЫВОД ТЕКУЩЕГО МАРШРУТА АВТОБУСА***\n")
    print(stopover_list)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***ДОБАВЛЕНИЕ ОСТАНОВКИ***\n')
    name_stopover , address_stopover , time_stopover = input("Введите название новой остановки, её адрес и время до следующей остановки\n").split()
    a = Add_Stopover(stopover_list,name_stopover,address_stopover,time_stopover)
    a.AppendInList()
    print(a)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***РАСЧЕТ ОБЩЕГО ВРЕМЕНИ МАРШРУТА***\n')
    b = AllTime(stopover_list)
    b.RaschetTime()
    print(b)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***ОПРЕДЕЛЕНИЕ, ГДЕ БУДЕТ АВТОБУС ЧЕРЕЗ N ОСТАНОВОК***\n')
    c=DeltaStopover(stopover_list,IndexOstanovki)
    c.OpredelenieStopover()
    print(c)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***ОПРЕДЕЛЕНИЕ ОБРАТНОГО МАРШРУТА***\n')
    d = ReturnRoute(stopover_list,IndexOstanovki) #не забыть передать классу другой класс
    d.FindRoute()
    print(d)
    print('\n'+"=" * 80)

if __name__ == "__main__":
    Main()
