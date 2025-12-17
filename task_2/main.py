#Лаптев Илья 1
#start code
import json
n_k =int( input("Введите номер квалификации"))
poisk = False
with open('task_2/dump.json', "r", encoding="utf-8") as f:
    templates = json.load(f )
for section in templates:
    if section["model"]== "data.specialty" and section["pk"]==n_k:
        print(f'=============== Найдено =============== \n{section["fields"]["code"]}>> Специальность "{section["fields"]["title"]}", {section["fields"]["c_type"]}')
        poisk = True
    if section["model"]== "data.skill" and section["pk"]==n_k:
        print(f'{section["fields"]["code"]}>> Специальность "{section["fields"]["title"]}"')
if not poisk:
    print("=============== Не найдено ===============")
#end code