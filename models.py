import peewee
from peewee import MySQLDatabase, Model, CharField, DateField ,SqliteDatabase
import pymysql
import pandas as pd




db_true_users = SqliteDatabase('create_templates.sqlite3')
class TrueUser(Model):
    user_id = CharField()
    class Meta:
        database = db_true_users

if __name__ == '__main__':
    db_true_users.create_tables([TrueUser])








user = 'root'
password = 'Algoritm2000'
db_name = 'user_search_proba'


db_user_search = MySQLDatabase(db_name, user=user, password=password, host='localhost') # Занятость базы данных
class UserSearchExperiment(Model):
    country_start_template = CharField() # Страна назначения в шаблоне
    region_start_template = CharField() # Регион отправления в шаблоне
    country_finish_template = CharField() # Страна назначения в шаблоне
    region_finish_template = CharField() # Регион назначения в шаблоне
    date_start_template = DateField() # Дата начала поиска
    date_finish_template = DateField() # Дата окончания поиска
    weight_start_template = CharField() # Начальный вес
    weight_finish_template = CharField() # Конечный вес
    volum_start_template = CharField() # Начальный объём
    volume_finish_template = CharField() # Конечный объём
    type_truck_template = CharField() # Тип грузовика
    id_user = CharField() # user_id
    identificator = CharField() # Идентификатор шаблона в гугл шиит
    """ячейки сохранения инфы из сайта"""
    route_start = CharField()
    route_end = CharField()
    distance = CharField()
    price = CharField()
    price_on_km = CharField()
    truck_type = CharField()
    weight = CharField()
    volume = CharField()
    cargo_type = CharField()
    contact = CharField()
    id_card = CharField()
    class Meta:
        database = db_user_search

if __name__ == '__main__':
    db_user_search.create_tables([UserSearchExperiment])










