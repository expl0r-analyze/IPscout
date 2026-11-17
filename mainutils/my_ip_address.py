import requests

def get_location():
    try:
        #Получение внешнего айпи адреса.
        ip_response = requests.get("https://api.ipify.org?format=json")
        ip = ip_response.json()["ip"]
            
         #получение данных о местоположении
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
            
        #вывод данных
        print(f"Айпи: {data.get('ip')}")
        print(f"Страна: {data.get('country')}")
        print(f"Регион: {data.get('region')}")
        print(f"Координаты: {data.get('loc')}")
        print(f"Провайдер: {data.get('org')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
    except KeyError:
        print("Подключение не установлено!")
              

while True:
    get_location()

    choice = input("Желаете продолжить? (д/Н): ")

    if choice == "д" or choice == "y":
        continue
    elif choice == "Н" or choice == "N":
        print("Благодарим за использование. Хорошего дня!")
        break

    else:
        print("Ошибка! Неизвестное значение, сессия завершена!!!")
        break
    
