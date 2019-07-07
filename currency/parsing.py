import requests
import json


class ParserNBRB:

    # создание парсера
    def __init__(self, url):
        self.URL = url

    # Получить JSON
    def update_JSON(self):
        self.response = requests.get(self.URL).json()
        return self.response

    # ЗАПИСАТЬ JSON В ФАЙЛ
    def write_json(self):
        try:
            data = json.load(open('parser.json'))
        except:
            data = []
        data.append(self.response)
        with open('parser.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    # парсинг даты
    def pars_date(self):
        result = []
        for sp in self.update_JSON():
            result.append(sp['Date'][:10])
        return result

    # парсинг курса
    def pars_cur(self):
        result = []
        for sp in self.update_JSON():
            result.append(sp['Cur_OfficialRate'])
        return result

