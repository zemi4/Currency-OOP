from currency.parsing import *
from currency.postgresql import *

# Создание объекта Базы данных
objBD = PostgresQL('currency', 'postgres', 'zemi4tut', 'localhost', '5432')

# создание объектов парсинга
usd = ParserNBRB('http://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2019-3-28&endDate=2019-6-28')
euro = ParserNBRB('http://www.nbrb.by/API/ExRates/Rates/Dynamics/292?startDate=2019-3-28&endDate=2019-6-28')
rub = ParserNBRB('http://www.nbrb.by/API/ExRates/Rates/Dynamics/298?startDate=2019-3-28&endDate=2019-6-28')
pln = ParserNBRB('http://www.nbrb.by/API/ExRates/Rates/Dynamics/293?startDate=2019-3-28&endDate=2019-6-28')
uah = ParserNBRB('http://www.nbrb.by/API/ExRates/Rates/Dynamics/290?startDate=2019-3-28&endDate=2019-6-28')

name_table = 'currency_3_month'
table_settings = '''
                    Дата text,
                    Доллар real,
                    Евро real,
                    Росс_руб real,
                    Злотых real,
                    Гривен real
                '''

# создание таблицы (если существует то pass)
if objBD.check_table(name_table):
    pass
else:
    objBD.create_table(name_table, table_settings)

# запись данных в таблицу
for d, u, e, r, p, ua in zip(usd.pars_date(), usd.pars_cur(), euro.pars_cur(), rub.pars_cur(), pln.pars_cur(),
                             uah.pars_cur()):
    values = [(d, u, e, r, p, ua)]
    objBD.insert_data(name_table, values)

