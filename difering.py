import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import telebot
from buttons import *
import pandas as pd
import email.encoders
import smtplib
from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle
from models import UserSearchExperiment, TrueUser
import telebot
import gspread
import random



COUNTRY = ['всі країни', '------------------------------', 'Україна  (UA)', 'Європа  (EU)', 'Азія  (ASIA)', 'Африка  (AFR)', '------------------------------', 'Австрія (AT)', 'Азербайджан (AZ)', 'Албанія (AL)', 'Алжир (DZ)', 'Андорра (AD)', 'Афганістан (AF)', 'Бангладеш (BD)', 'Бельгія (BE)', 'Білорусь (BY)', 'Болгарія (BG)', 'Боснія і Герцеговина (BA)', 'Великобританія (GB)', "В'єтнам (VN)", 'Ватикан (VA)', 'Вірменія (AM)', 'Гонконг (HK)', 'Греція (GR)', 'Грузія (GE)', 'Данія (DK)', 'Естонія (EE)', 'Єгипет (EG)', 'Ізраїль (IL)', 'Індія (IN)', 'Індонезія (ID)', 'Ірак (IQ)', 'Іран (IR)', 'Ірландія (IE)', 'Іспанія (ES)', 'Італія (IT)', 'Йорданія (JO)', 'Казахстан (KZ)', 'Камбоджа (KH)', 'Катар (QA)', 'Кенія (KE)', 'Киргизстан (KG)', 'Китай (CN)', 'Кіпр (CY)', 'КНДР (KP)', 'Республіка Косово (XK)', 'Кувейт (KW)', 'Лаос (LA)', 'Латвія (LV)', 'Леван (LB)', 'Литва (LT)', 'Лівія (LY)', 'Ліхтенштейн (LI)', 'Люксембург (LU)', 'Македонія (MK)', 'Мальта (MT)', 'Марокко (MA)', 'Молдова (MD)', 'Монако (MC)', 'Монголія (MN)', 'Нідерланди (NL)', 'Німеччина (DE)', 'Норвегія (NO)', 'ОАЕ (AE)', 'Пакистан (PK)', 'Південна Африка (ZA)', 'Південна Корея (KR)', 'Польща (PL)', 'Португалія (PT)', 'Росія (RU)', 'Румунія (RO)', 'Саудівська Аравія (SA)', 'Сербія (RS)', 'Сирія (SY)', 'Сінгапур (SG)', 'Словаччина (SK)', 'Словенія (SI)', 'Таджикистан (TJ)', 'Таїланд (TH)', 'Тайвань (TW)', 'Туреччина (TR)', 'Туркменістан (TM)', 'Угорщина (HU)', 'Узбекистан (UZ)', 'Україна (UA)', 'Фінляндія (FI)', 'Франція (FR)', 'Хорватія (HR)', 'Чеська республіка (CZ)', 'Чорногорія (ME)', 'Швейцарія (CH)', 'Швеція (SE)', 'Шрі-Ланка (LK)', 'Японія (JP)']
REGION = ['всі обл.', '-----------------------------', 'Захід України', 'Південь України', 'Північ України', 'Схід України', 'Центр України', '-----------------------------', 'Вінницька область', 'Волинська область', 'Дніпропетровська область', 'Донецька область', 'Житомирська область', 'Закарпатська область', 'Запорізька область', 'Івано-Франківська область', 'Київська область', 'Кіровоградська область', 'Крим автономна республіка', 'Луганська область', 'Львівська область', 'Миколаївська область', 'Одеська область', 'Полтавська область', 'Рівненська область', 'Сумська область', 'Тернопільська область', 'Харківська область', 'Херсонська область', 'Хмельницька область', 'Черкаська область', 'Чернівецька область', 'Чернігівська область']
WEIGHT = ['...', '1 т', '2 т', '3 т', '4 т', '5 т', '6 т', '7 т', '8 т', '9 т', '10 т', '11 т', '12 т', '13 т', '14 т', '15 т', '16 т', '17 т', '18 т', '19 т', '20 т', '21 т', '22 т', '23 т', '24 т', '25 ...']
VOLUME = ['...', '1 м³', '2 м³', '3 м³', '4 м³', '5 м³', '10 м³', '15 м³', '20 м³', '25 м³', '30 м³', '40 м³', '50 м³', '60 м³', '70 м³', '80 м³', '90 м³', '100 м³', '110 м³', '120 м³', '130 ...']
TRUCK = ['будь-який', '--------------------', 'тент', 'крита', 'ізотерм', 'цільнометал.', 'рефрижератор', '--------------------', 'автобус', 'автобус вантажопас.', 'автобус люкс', 'автовоз', 'автокран', 'бензовоз', 'бетонозмішувач', 'бітумовоз', 'борошновоз', 'бортова', 'будь-яка', 'відкрита', 'евакуатор', 'екскаватор', 'зерновоз', 'ізотерм', 'контейнер пустий', 'контейнеровіз', 'кормовіз', 'крита', 'лісовоз', 'маніпулятор', 'масловоз', 'мебльовіз', 'металовіз (ломовіз)', 'мікроавтобус', 'негабарит', 'панелевіз', 'платформа', 'птаховіз', 'рефрижератор', 'самоскид', 'скловіз', 'скотовоз', 'спецавто', 'тагач', 'тент', 'трал', 'трубовіз', 'цементовіз', 'цистерна газова', 'цистерна ізотерм.', 'цистерна харч.', 'цистерна хім.', 'цільнометал.', 'цільнопластиковий', 'щеповіз']

ADMIN = int(450947429)
API_TOKEN = '5321273519:AAFrwvLRDqZTQSQF9-PzIdk6jq0iyOuxDo8'
bot = telebot.TeleBot(API_TOKEN)


def get_information_google_sheets():
        # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = 'railwabot-71cc25b5077f.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # Пример чтения файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="'Ответы на форму (1)'!A1:N1000",
        majorDimension='COLUMNS'
    ).execute()
    datas = values.get('values')
    df = pd.DataFrame()
    for i in range(0, len(datas)):
        df[datas[i][0]] = datas[i][1:]
    return df


def temaplate_user(message): # отправляем пользователю шаблоны
    make_identificator()
    id_user = message.chat.id
    datas = get_information_google_sheets()
    user_df = datas.query(f'id == "{id_user}"')
    for i in range(0,len(user_df)):
        message = user_df.loc[i]
        msg = f'Країна відправлення - {message.tolist()[1]}\n' \
              f'Регіон відправлення(тільки для України) - {message.tolist()[2]}\n' \
              f'Країна призначення - {message.tolist()[3]}\n' \
              f'Регіон призначення(тільки для України) - {message.tolist()[4]}\n' \
              f'Дата початку пошуку - {message.tolist()[5]}\n' \
              f'Кінцева дата пошуку - {message.tolist()[6]}\n' \
              f'Маса вантажівкі від - {message.tolist()[7]}\n' \
              f'Маса вантажівки до - {message.tolist()[8]}\n' \
              f"Об'єм вантажіки від - {message.tolist()[9]}\n" \
              f"Об'єм вантажіки до - {message.tolist()[10]}\n" \
              f"Тип транспорту - {message.tolist()[11]}\n" \
              f"Ідентифікатор - {message.tolist()[13]}"
        bot.send_message(id_user, msg, reply_markup=keyboard_start())




def make_identificator(): # Создаём идентификатор
    gs = gspread.service_account(filename='railwabot-71cc25b5077f.json')
    sh = gs.open_by_key('1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo')
    worksheet = sh.sheet1
    identificator_list = worksheet.get('N2:N1000') # выбираем все уникальные знаяения
    for i in range(2,1000):
        if worksheet.get(f'N{i}') == [] and worksheet.get(f'M{i}') != []: # там где не присвоен идентификатор - присваиваем
            identificator = random.randint(100,10000000000)
            while identificator in identificator_list:
                identificator = random.randint(100,10000000000)
            worksheet.update_acell(f'N{i}', identificator)
        if worksheet.get(f'C{i}') == [] and worksheet.get(f'B{i}') != []:
            worksheet.update_acell(f'C{i}', 'Значення не вказано')
        if worksheet.get(f'E{i}') == [] and worksheet.get(f'D{i}') !=[]:
            worksheet.update_acell(f'E{i}', 'Значення не вказано')
        if worksheet.get(f'D{i}') == []:
            break

def delete_template(message): # Удаляем шаблон по идентификатору
    try:
        delete_identificator = message.text.split('\n')[-1].split(' ')[-1]
    except:
        bot.send_message(message.chat.id, 'Перепрошую, але боту треба переслати повідомлення з шаблоном', reply_markup=keyboard_start())
        return
    gs = gspread.service_account(filename='railwabot-71cc25b5077f.json')
    sh = gs.open_by_key('1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo')
    worksheet = sh.sheet1
    column_identificator = worksheet.get('N1:N1000')
    if [delete_identificator] not in column_identificator:
        bot.send_message(message.chat.id, 'Перепрошую, але боту треба переслати повідомлення з шаблоном', reply_markup=keyboard_start())
        return
    row_delete = column_identificator.index([delete_identificator]) + 1
    worksheet.delete_row(row_delete)
    bot.send_message(message.chat.id, 'Шаблон успішно видалено', reply_markup=keyboard_start())

def add_to_database():
    identifacators = []
    for identi in UserSearchExperiment:
        identifacators.append(identi.identificator)
    gs = gspread.service_account(filename='railwabot-71cc25b5077f.json')
    sh = gs.open_by_key('1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo')
    worksheet = sh.sheet1
    datas = worksheet.get('A2:N1000')
    for i in range(0, len(datas)):
        if datas[i][-1] not in identifacators:
            UserSearchExperiment.create(
                country_start_template = datas[i][1],
                region_start_template = datas[i][2],
                country_finish_template = datas[i][3],
                region_finish_template = datas[i][4],
                date_start_template = datetime.datetime.strptime(datas[i][5], '%d.%m.%Y').date(),
                date_finish_template = datetime.datetime.strptime(datas[i][6], '%d.%m.%Y').date(),
                weight_start_template = datas[i][7],
                weight_finish_template = datas[i][8],
                volum_start_template = datas[i][9],
                volume_finish_template = datas[i][10],
                type_truck_template = datas[i][11],
                id_user = datas[i][12],
                identificator = datas[i][13],
                route_start = 'None',
                route_end = 'None',
                distance = 'None',
                price = 'None',
                price_on_km = 'None',
                truck_type = 'None',
                weight = 'None',
                volume = 'None',
                cargo_type = 'None',
                contact = 'None',
                id_card = 'None')



def variations(obj): #получение вариантов выбора
    list_obj = []
    for i in range(0,len(obj)):
        list_obj.append(obj[i].text)
    return list_obj

def variations_country_start():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')  # отключаем режим вэбдрайвера
    options.add_argument('--headless')  # Разкоментировать для выполнения задач в фоне
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\lemes\\pythonProgect_towork\\Cars_Bot\\chromedriver\\chromedriver.exe',
        options=options)
    driver.get(url='https://della.ua/search/')
    dropdown_box_depart_country = driver.find_elements(By.XPATH,
                                                       '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                       'div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/select/option')
    msg = variations(dropdown_box_depart_country)
    for i in range(0, len(msg)):
        return




def scaning_db():
    add_to_database()
    LOGIN_USER = ### логин
    PASSWORD_USER = ### пароль
    # Собираем все идентифакаторы из базы данных
    identificators = []
    for ident in UserSearchExperiment:
        identificators.append(ident.identificator)
    identificators = list(set(identificators))
    for idetificator in identificators:
        line_db = UserSearchExperiment.select().where(UserSearchExperiment.identificator == idetificator).get()
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')  # отключаем режим вэбдрайвера
        #options.add_argument('--headless')  # Разкоментировать для выполнения задач в фоне
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\lemes\\pythonProgect_towork\\Cars_Bot\\chromedriver\\chromedriver.exe',
            options=options)

        try:
            driver.get(url='https://della.ua/search/')
            for cookie in pickle.load(open('mohylovtrans@gmail.com_cookies', 'rb')):
                driver.add_cookie(cookie)
            driver.refresh()
            driver.find_element(By.NAME, 'trans_cargo').click()

            '''Выбираем страну отправления'''
            dropdown_box_depart_country = driver.find_elements(By.XPATH,
                                                               '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                               'div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/select/option')
            #variation_dropdown_box_depart_country = variations(dropdown_box_depart_country)  # Варианты выбора страны отправления
            index = COUNTRY.index(line_db.country_start_template)
            dropdown_box_depart_country[index].click()
            #for i in range(0, len(dropdown_box_depart_country)):  # выбор страны отправления
            #    if dropdown_box_depart_country[i].text == line_db.country_start_template:
            #        dropdown_box_depart_country[i].click()

            '''Выбираем область отправления ! надо добавить в будущем фильтр только для Украины'''
            dropdown_region_departure = driver.find_elements(By.XPATH,
                                                             '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                             'div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/select/option')
            #variation_region_departure = variations(dropdown_region_departure)  # Варианты выбора области отправления
            if line_db.region_start_template == 'Значення не вказано':
                index = REGION.index('всі обл.')
            else:
                index = REGION.index(line_db.region_start_template)
            dropdown_region_departure[index].click()
            #for i in range(0, len(dropdown_region_departure)):
            #    if dropdown_region_departure[i].text == line_db.region_start_template:
            #        dropdown_region_departure[i].click()
    
            '''Выбираем страну назначения'''
            dropdown_destination_country = driver.find_elements(By.XPATH,
                                                                '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                                'div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td/select/option')
            #variation_country_destination = variations(dropdown_destination_country)  # Варианты страны назначения
            index = COUNTRY.index(line_db.country_finish_template)
            dropdown_destination_country[index].click()
            #for i in range(0, len(dropdown_destination_country)):
            #    if dropdown_destination_country[i].text == line_db.country_finish_template:
            #        dropdown_destination_country[i].click()
    
            '''Выбираем область назначения'''
            dropdown_destination_region = driver.find_elements(By.XPATH,
                                                               '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                               'div/table/tbody/tr[2]/td[4]/table/tbody/tr[2]/td/select/option')
            variation_region_destination = variations(dropdown_destination_region)  # Варианты области назначения
            if line_db.region_finish_template == 'Значення не вказано':
                index = REGION.index('всі обл.')
            else:
                index = REGION.index(line_db.region_finish_template)
            dropdown_destination_region[index].click()
            #for i in range(0, len(dropdown_destination_region)):
            #    if dropdown_destination_region[i].text == line_db.region_finish_template:
            #        dropdown_destination_region[i].click()
    
            '''Выбираем дату начала'''
            data_start = driver.find_element(By.ID, 'calInputTextFrom')
            data_start.clear()
            data_start.send_keys(str(line_db.date_start_template.strftime("%d.%m.%Y")))
    
            '''Выбираем дату конца'''
            data_finish = driver.find_element(By.ID, 'calInputTextTo')
            data_finish.clear()
            data_finish.send_keys(str(line_db.date_finish_template.strftime("%d.%m.%Y")))
    
            '''Выбираем массу от'''
            weight_start = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                          'div/table/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[4]/select/option')
            index = WEIGHT.index(line_db.weight_start_template)
            weight_start[index].click()
            #for i in range(0, len(weight_start)):
            #    if weight_start[i].text == line_db.weight_start_template:
            #        weight_start[i].click()
    
            '''Выбираем массу до'''
            weight_end = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                        'div/table/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[4]/select/option')
            index = WEIGHT.index(line_db.weight_finish_template)
            weight_end[index].click()
            #for i in range(0, len(weight_end)):
            #    if weight_end[i].text == line_db.weight_finish_template:
            #        weight_end[i].click()
    
            '''Выбираем объём от'''
            volume_start = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                          'div/table/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[6]/select/option')
            index = VOLUME.index(line_db.volum_start_template)
            volume_start[index].click()
            #for i in range(0, len(volume_start)):
            #    if volume_start[i].text == line_db.volum_start_template:
            #        volume_start[i].click()
    
            '''Выбираем объём до'''
            volume_end = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                        'div/table/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[6]/select/option')
            index = VOLUME.index(line_db.volume_finish_template)
            volume_end[index].click()
            #for i in range(0, len(volume_end)):
            #    if volume_end[i].text == line_db.volume_finish_template:
            #        volume_end[i].click()
    
            '''Выбираем транспорт'''
            transport = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                       'div/table/tbody/tr[2]/td[5]/table/tbody/tr[5]/td/div/div[1]/select/option')
            index = TRUCK.index(line_db.type_truck_template)
            transport[index].click()
            #for i in range(0, len(transport)):
            #    if transport[i].text == line_db.type_truck_template:
            #        transport[i].click
    
            '''Клацаем поиск'''
            driver.find_element(By.XPATH,
                                '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/div/table/tbody/tr[3]/td/table/tbody/tr/td').click()

            '''высчитываем все карточки, которые есть у нас в БД'''
            cards_db = []
            for id in UserSearchExperiment.select().where(UserSearchExperiment.identificator == idetificator):
                cards_db.append(id.id_card)
            actual_cards = []  # создаём поле с актуальными карточками
    
            '''Извлекаем информацию из каждой картчоки'''
            cards = driver.find_elements(By.CLASS_NAME, 'request_card')

            for card in cards:
                route = card.find_elements(By.CLASS_NAME, 'locality')  # выбираем маршщрут из div
                route_start = route[0].text
                route_end = route[1].text
                try:
                    distance = card.find_element(By.CLASS_NAME, 'distance').text
                except:
                    distance = 'Значення не вказано'
                try:
                    price = card.find_element(By.CLASS_NAME, 'price_main').text.replace('\n ', '')
                except:
                    price = 'Значення не вказано'
                try:
                    price_on_km = card.find_element(By.CLASS_NAME, 'price_additional').text
                except:
                    price_on_km = 'Значення не вказано'
                truck_type = card.find_element(By.CLASS_NAME, 'truck_type').text
                weight = card.find_element(By.CLASS_NAME, 'weight').text
                try:
                    volume = card.find_element(By.CLASS_NAME, 'cube').text
                except:
                    volume = 'Значення не вказано'
                cargo_type = card.find_element(By.CLASS_NAME, 'cargo_type').text
                id_card = card.get_attribute('data-request_id')
                # Клацаем кнопочку с информацией
                find_buttons_information = card.find_element(By.CLASS_NAME, 'show_request_info_btn').click()
                contact_name = card.find_element(By.CLASS_NAME, 'contact_name').text
                contacts = card.find_elements(By.CLASS_NAME, 'value')
                contact = contact_name + "-" + contacts


                if route_start != '' and id_card not in cards_db:
                    ''' добавление в бд информации сейчас занимаюсь єтим методом'''
                    if line_db.route_start == 'None':
                        line_db.route_start = route_start
                        line_db.route_end = route_end
                        line_db.disctance = distance
                        line_db.price = price
                        line_db.price_on_km = price_on_km
                        line_db.truck_type = truck_type
                        line_db.weight = weight
                        line_db.volume = volume
                        line_db.cargo_type = cargo_type
                        line_db.id_card = id_card
                        line_db.contact = contact
                        line_db.save()
                    #добавление новіх строк в БД
                    else:
                        UserSearchExperiment.create(
                            country_start_template = line_db.country_start_template,
                            region_start_template = line_db.region_start_template,
                            country_finish_template = line_db.country_finish_template,
                            region_finish_template = line_db.region_finish_template,
                            date_start_template = line_db.date_start_template,
                            date_finish_template = line_db.date_finish_template,
                            weight_start_template = line_db.weight_start_template,
                            weight_finish_template = line_db.weight_finish_template,
                            volum_start_template = line_db.volum_start_template,
                            volume_finish_template = line_db.volume_finish_template,
                            type_truck_template = line_db.type_truck_template,
                            id_user = line_db.id_user,
                            identificator = line_db.identificator,
                            route_start = route_start,
                            route_end = route_end,
                            disctance = distance,
                            price = price,
                            price_on_km = price_on_km,
                            truck_type = truck_type,
                            weight = weight,
                            volume = volume,
                            cargo_type = cargo_type,
                            contact = contact,
                            id_card = id_card )



                    msg = str(
                        f' рейса - {route_start} Конец рейса - {route_end} Растояние - {distance} Цена - {price} '
                        f'Цена за км - {price_on_km} Типа автомобиля - {truck_type} Весс - {weight} Объём - {volume}'
                        f'Тип груза {cargo_type}')
                    bot.send_message(line_db.id_user, msg)
                actual_cards.append(id_card)

            # удаляем неактивные заявки
            for line in UserSearchExperiment.select().where(UserSearchExperiment.identificator == idetificator):
               if line.id_card not in actual_cards and line.id_card!= 'None':
                    line.delete_instance()


        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()


def delete_template_pasttime():
    # Удаляем шаблон из гугл таблицы
    today = datetime.datetime.today()
    gs = gspread.service_account(filename='railwabot-71cc25b5077f.json')
    sh = gs.open_by_key('1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo')
    worksheet = sh.sheet1
    columns_dates = worksheet.get('G1:G1000')
    for i in range(len(columns_dates), -1, -1):
        if datetime.datetime.strptime(columns_dates[i][0], "%d.%m.%Y") < today:
            worksheet.delete_rows(i+1)
    # Удаляем все записи с прошедшей даты из базы данных
    for line in UserSearchExperiment.select().where(UserSearchExperiment.date_finish_template <= today):
        line.delete_instance()



def add_true_user(user_id):
    user_id = user_id.text
    TrueUser.create(user_id=user_id)
    bot.send_message(ADMIN, f'Користувача - {user_id} успішно додано')


def delete_true_user(user_id_delete):
    user_id_delete = user_id_delete.text
    gs = gspread.service_account(filename='railwabot-71cc25b5077f.json')
    sh = gs.open_by_key('1sQjOjHhkFpZF3PNButXn70_LSizDIcAFDb0AGJT3ywo')
    worksheet = sh.sheet1
    users = worksheet.get('M1:M1000')
    indexs_delete = []
    while [user_id_delete] in users:
        indexs_delete.append(users.index([user_id_delete])+1)
        users[users.index([user_id_delete])] = 'delete'
    indexs_delete = sorted(indexs_delete, reverse=True)
    for i in range(0,len(indexs_delete)):
        worksheet.delete_rows(indexs_delete[i])
    for line in UserSearchExperiment.select().where(UserSearchExperiment.id_user == user_id_delete):
        line.delete_instance()
    for user in TrueUser:
        if user.user_id == user_id_delete:
            user.delete_instance()
            bot.send_message(ADMIN, f'Користувача - {user_id_delete} видалено')
            return
    bot.send_message(ADMIN, "Користувача не знайдено")

def verification(chat_id):
    users = []
    for user in TrueUser:
        users.append(user.user_id)
    if chat_id in users:
        return True
    else:
        return False

def msg_not_verification(chat_id):
    return bot.send_message(chat_id, 'Вибачте, доступ обмежений')

def msg_for_all_user(message):
    text = message.text
    for user in TrueUser:
        bot.send_message(user.user_id, text, reply_markup=keyboard_start())

def msg_for_admin(message):
    bot.forward_message(ADMIN, message.chat.id, message_id=message.message_id)