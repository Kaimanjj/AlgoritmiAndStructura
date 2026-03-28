#создадим словарь, где ключ - название остановки, значение - список с координатами и временем до следующей остановки 
# stopover_dict = {"Остановка 1": ["Адрес 1",15],
#                  "Остановка 2": ["Адрес 2",13],
#                  "Остановка 3": ["Адрес 3",9],
#                  "Остановка 4": ["Адрес 4",23],
#                  "Остановка 5": ["Адрес 5",5],
#                  "Остановка 6": ["Адрес 6",8]}


#так как надо работать со списками, создадим список со списками с аналогичными значениями
stopover_list = [["Остановка 1","Адрес 1",15],["Остановка 2","Адрес 2",13],["Остановка 3","Адрес 3",9],["Остановка 4","Адрес 4",23],["Остановка 5","Адрес 5",5],["Остановка 6","Адрес 6",8]]

#добавление остановки 
name_stopover , address_stopover , time_stopover = input("Введите название новой остановки, её адрес и время до следующей остановки\n").split()
time_stopover = int(time_stopover)

#print(f"Название:{name_stopover},{type(name_stopover)},Адрес:{address_stopover},{type(address_stopover)}, Время:{time_stopover},{type(time_stopover)}")

stopover_list.append([name_stopover,address_stopover,time_stopover])

#расчет общего времени маршрута
time_way = 0
for i in stopover_list:
    time_way += i[2]
print(time_way)

#Определение, где будет автобус через N остановок
current_stopover = input('Напишите название остановки, на которой сейчас находится автобус:\n')
count_stopover = int(input("Напишите количество остановок, которые должен проехать автобус:\n"))
def OpredOstanovki():
    k=0
    for i in range(len(stopover_list)-1):
        if stopover_list[i][0]==current_stopover:
            return k
        k+=1
kolichestvo = OpredOstanovki()
print(f'Через {count_stopover} остановок автобус будет на остновке под названием:{stopover_list[count_stopover+kolichestvo][0]}')



