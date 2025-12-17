#Лаптев Илья 1
#start code
import json
def op_1(templates):
    for i in templates:
        print(f'Номер записи :{i["id"]} Латинское имя :{i["latin_name"]} {"не Пресноводная"if i["is_salt_water_fish"]else"пресноводная"} количество видов: {i["sub_type_count"]}')
def op_2(templates):
    while True:
        isk = input("Введите id для поиска")
        try:
            isk = int(isk)
            break
        except:
            print("Вы ввели некоректное значение")
    for i in templates:
        if i["id"]==isk:
            op_1([i])
            break
    else:print("Нет такого id")
def op_3(templates):
    lis= [ 'name', 'latin_name','is_salt_water_fish','sub_type_count']
    spis={}
    try:
        spis["id"]=templates[-1]["id"]+1
    except:spis["id"]=1
    for i in lis:
        while True:
            spis[i]=input("Введите значение для " +i)
            if i=='is_salt_water_fish':
                try:
                    spis[i]= bool(spis[i])
                    break
                except:
                    print("Вы ввели некоректное значение")
            elif i=='sub_type_count':
                try:
                    spis[i]= int(spis[i])
                    break
                except:
                    print("Вы ввели некоректное значение")
            else:break
    templates.append(spis)
    with open('task_3/dump.json', "w", encoding="utf-8") as f:
        json.dump(templates, f, indent=4, ensure_ascii=False)
def op_4(templates):
    while True:
        isk = input("Введите id для удаления")
        try:
            isk = int(isk)
            break
        except:
            print("Вы ввели некоректное значение")
    for v,i in enumerate(templates):
        if i["id"]==isk:
            del templates[v] 
            break
    else:print("Нет такого id")
    with open('task_3/dump.json', "w", encoding="utf-8") as f:
        json.dump(templates, f, indent=4, ensure_ascii=False)
def chicl(pov=0):
    with open('task_3/dump.json', "r", encoding="utf-8") as f:
        templates = json.load(f )
    while True:
        var=input("Введите действие:\n1–Вывести все записи \n2-Вывести запись по полю\n3-Добавить запись\n4-Удалить запись по полю\n5-Выйти из программы\n")    
        if  var in ["1","2","3","4","5"]:
            var=int(var)
            break
        else:print("Вы ввели некоректное значение")
    if var ==1:
        op_1(templates)
    if var ==2:
        op_2(templates)
    if var ==3:
        op_3(templates)
    if var ==4:
        op_4(templates)
    if var ==5:
        print(f"Выполненно операций {pov}")
        return
    chicl(pov=pov+1)
chicl()
#end code
