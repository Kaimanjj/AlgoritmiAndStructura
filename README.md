# Лабораторная работа №2
## Подготовила Пивоварчук Дарья ИДБ-25-07
1. Подключенные библиотеки
```python
  import base64 #для конвертации данных
  from tabulate import tabulate #для форматирования списка в таблицу
```
3. Класс для нахождения индекса выбранной остановки в списке
```python
class IndexOstanovki:
    @staticmethod
    def OpredOstanovki(stopover_list,current_stopover):
        k=0
        for i in range(len(stopover_list)-1):
            if stopover_list[i][0]==current_stopover:
                return k
            k+=1
        return k
```
4. Добавление остановки 
```python
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
```
5. Расчет общего времени маршрута
```python
class AllTime:
    def __init__(self,stopover_list,dop_class_index,begining,end):
        self.stopover_list = stopover_list
        self.dop_class_index = dop_class_index
        self.begining = begining
        self.end = end
        self.time_way = 0
    def RaschetTime(self):
        index_begining = self.dop_class_index.OpredOstanovki(self.stopover_list, self.begining)
        index_end  = self.dop_class_index.OpredOstanovki(self.stopover_list, self.end)
        for i in range(index_begining, index_end):
            self.time_way += self.stopover_list[i][2]
    def __str__(self):
        return f'Общее время маршрута:{self.time_way}'
```
6. Определение, где будет автобус через N остановок
```python
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
```
7. Построение обратного маршрута 
```python
class ReturnRoute:
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
```
8. Класс для вывода маршрута в формате таблицы
```python
class Spreadsheet:
    def __init__(self, stopover_list):
        self.stopover_list = stopover_list
        self.headers = ["Название", "Адрес", "Время до следующей остановки"]
    def __str__(self):
        return f'Табличное представление информации\n{tabulate(self.stopover_list, headers=self.headers, tablefmt="pretty")}'
```
9. Класс для создания текстового файла 
```python
class TextFile:
    def __init__(self,stopover_list):
        self.stopover_list = stopover_list
        self.content = ''
        self.content_1 = ''
    def ConvertingFile(self):
        for route in self.stopover_list:
            encoded_name = base64.b64encode(str(route[0]).encode())
            encoded_address = base64.b64encode(str(route[1]).encode())
            encoded_time = base64.b64encode(str(route[2]).encode())
            with open('data.txt', 'a',encoding='utf-8') as file:
                file.write(f"{encoded_name}, {encoded_address}, {encoded_time}\n")
            encoded_name_bytes = base64.b64decode(encoded_name)
            decoded_name_text = encoded_name_bytes.decode('utf-8')
            encoded_address_bytes = base64.b64decode(encoded_address)
            decoded_address_text = encoded_address_bytes.decode('utf-8')
            encoded_time_bytes = base64.b64decode(encoded_time)
            decoded_time_text = encoded_time_bytes.decode('utf-8')
            with open('proverka.txt','a',encoding='utf-8') as file_pr:
                file_pr.write(f"{decoded_name_text}, {decoded_address_text}, {decoded_time_text}\n")
        with open('data.txt', 'r', encoding='utf-8') as file_route:
            self.content = file_route.read()
        with open('proverka.txt', 'r', encoding='utf-8') as file_route_1:
            self.content_1 = file_route_1.read()
    def __str__(self):
        return f'Текстовый файл маршрута (Base64):\n {self.content}\n Восстановленный текстовый файл маршрута:\n {self.content_1}'
```
10. Главная функция, которая вызывает остальные
```python
class Main:
    with open('data.txt', 'w', encoding='utf-8'):
        pass  # файл очищен
    with open('proverka.txt', 'w', encoding='utf-8'):
        pass  # файл очищен
    #так как надо работать со списками, создадим список со списками с аналогичными значениями
    stopover_list = [["Остановка 1","Адрес 1",15],["Остановка 2","Адрес 2",13],["Остановка 3","Адрес 3",9],["Остановка 4","Адрес 4",23],["Остановка 5","Адрес 5",5],["Остановка 6","Адрес 6",8]]
    print("=" * 80)
    print("***ВЫВОД ТЕКУЩЕГО МАРШРУТА АВТОБУСА***\n")
    print(stopover_list)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***ДОБАВЛЕНИЕ ОСТАНОВКИ***\n')
    name_stopover = str(input("Введите название новой остановки:\n"))
    address_stopover = str(input("Её адрес:\n"))
    time_stopover = input("И время до следующей остановки:\n")
    a = Add_Stopover(stopover_list,name_stopover,address_stopover,time_stopover)
    a.AppendInList()
    print(a)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***РАСЧЕТ ОБЩЕГО ВРЕМЕНИ МАРШРУТА***\n')
    beginning = input('С какой остановки начать путь:')
    end = input('До какой остановки:')
    b = AllTime(stopover_list,IndexOstanovki,beginning,end)
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

    print('\n'+"=" * 80)
    print('***ПРЕДСТАВЛЕНИЕ МАРШРУТА В ФОРМАТЕ ТАБЛИЦЫ***\n')
    f = Spreadsheet(stopover_list) 
    #f.ConvertingFile()
    print(f)
    print('\n'+"=" * 80)

    print('\n'+"=" * 80)
    print('***КОНВЕРТАЦИЯ МАРШРУТА В ТЕКСТОВЫЙ ФАЙЛ (BASE64)***\n')
    e = TextFile(stopover_list) 
    e.ConvertingFile()
    print(e)
    print('\n'+"=" * 80)
```
12. Вызов главной функции
```python
if __name__ == '__main__':
        Main()
```



   
