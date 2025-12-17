#Лаптев Илья 1
#start code
import json
var=0
oper = 0
with open('task_3/dump.json', "r", encoding="utf-8") as f:
    templates = json.load(f )
while True:
    var=int(input("Введите действие:\n1–Вывести все записи \n2-Вывести запись по полю\n3-Добавить запись\n4-Удалить запись по полю\n5-Выйти из программы\n"))
    if var==1:
        for i in templates:
            print(f'Номер записи :{i["id"]} Латинское имя :{i["latin_name"]} {"не Пресноводная"if i["is_salt_water_fish"]else"пресноводная"} количество видов: {i["sub_type_count"]}')
    if var==2:
        isk = int(input("Введите id для поиска"))
        for i in templates:
            if i["id"]==isk:
                print(f'Номер записи :{i["id"]} Латинское имя :{i["latin_name"]} {"не Пресноводная"if i["is_salt_water_fish"]else"пресноводная"} количество видов: {i["sub_type_count"]}')
                break
        else:print("Нет такого id")
    if var==3:
        lis= [ 'name', 'latin_name','is_salt_water_fish','sub_type_count']
        spis={}
        spis["id"]=templates[-1]["id"]+1
        for i in lis:
            spis[i]=input("Введите значение для " +i)
            if i=='is_salt_water_fish':
                spis[i]= bool(spis[i])
            if i=='sub_type_count':
                spis[i]= int(spis[i])
        templates.append(spis)
        with open('task_3/dump.json', "w", encoding="utf-8") as f:
             json.dump(templates, f, indent=4, ensure_ascii=False)
    if var==4:
        isk = int(input("Введите id для удаление"))
        for v,i in enumerate(templates):
            if i["id"]==isk:
                del templates[v] 
                break
        else:print("Нет такого id")
        with open('task_3/dump.json', "w", encoding="utf-8") as f:
             json.dump(templates, f, indent=4, ensure_ascii=False)
    if var==5:
        print(f"Выполненно операций {oper}")
        break
    oper+=1
#end code