from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle
from difering import variations
from models import UserSearchExperiment
import telebot


'''Кусок кода для проверки работоспособности бота'''


ADMIN = admin = int(450947429)
API_TOKEN = '5491247029:AAH-jh2OD2p-Qc7YTeV3V5r8JWyDZ-mUyfU'

bot = telebot.TeleBot(API_TOKEN)






options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled') # отключаем режим вэбдрайвера
#options.add_argument('--headless') #Разкоментировать для выполнения задач в фоне
driver = webdriver.Chrome(executable_path='C:\\Users\\lemes\\pythonProgect_towork\\Cars_Bot\\chromedriver\\chromedriver.exe',
                          options=options)








try:
    driver.get(url='https://della.ua/search/')
    for cookie in pickle.load(open('mohylovtrans@gmail.com_cookies', 'rb')):
        driver.add_cookie(cookie)
    driver.refresh()
    driver.find_element(By.NAME, 'trans_cargo').click()


    '''Выбираем страну отправления'''
    dropdown_box_depart_country = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                                 'div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/select/option')
    variation_dropdown_box_depart_country = variations(dropdown_box_depart_country) # Варианты выбора страны отправления
    for i in range(0,len(dropdown_box_depart_country)): # выбор страны отправления
        if dropdown_box_depart_country[i].text == 'Україна  (UA)':
            dropdown_box_depart_country[i].click()


    '''Выбираем область отправления ! надо добавить в будущем фильтр только для Украины'''
    dropdown_region_departure = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                              'div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/select/option')
    variation_region_departure = variations(dropdown_region_departure) # Варианты выбора области отправления
    for i in range(0,len(dropdown_region_departure)):
        if dropdown_region_departure[i].text == 'Захід України':
            dropdown_region_departure[i].click()

    '''Выбираем страну назначения'''
    dropdown_destination_country = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                                  'div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td/select/option')
    variation_country_destination = variations(dropdown_destination_country) # Варианты страны назначения
    for i in range(0,len(dropdown_destination_country)):
        if dropdown_destination_country[i].text == 'Україна  (UA)':
            dropdown_destination_country[i].click()

    '''Выбираем область назначения'''
    dropdown_destination_region = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                                 'div/table/tbody/tr[2]/td[4]/table/tbody/tr[2]/td/select/option')
    variation_region_destination = variations(dropdown_destination_region) # Варианты области назначения
    for i in range(0,len(dropdown_destination_region)):
        if dropdown_destination_region[i].text == 'Схід України':
            dropdown_destination_region[i].click()

    '''Выбираем дату начала'''
    data_start = driver.find_element(By.ID, 'calInputTextFrom')
    data_start.clear()
    data_start.send_keys('30.03.2023')

    '''Выбираем дату конца'''
    data_finish = driver.find_element(By.ID, 'calInputTextTo')
    data_finish.clear()
    data_finish.send_keys('25.04.2023')

    '''Выбираем массу от'''
    weight_start = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                  'div/table/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[4]/select/option')
    for i in range(0,len(weight_start)):
        if weight_start[i].text == '1 т':
            weight_start[i].click()

    '''Выбираем массу до'''
    weight_end = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                'div/table/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[4]/select/option')
    for i in range(0, len(weight_end)):
        if weight_end[i].text == '25 ...':
            weight_end[i].click()

    '''Выбираем объём от'''
    volume_start = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                  'div/table/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[6]/select/option')

    for i in range(0,len(volume_start)):
        if volume_start[i].text == '1 м³':
            volume_start[i].click()

    '''Выбираем объём до'''
    volume_end = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                                'div/table/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[6]/select/option')
    for i in range(0,len(volume_end)):
        if volume_end[i].text == '130 ...':
            volume_end[i].click()

    '''Выбираем транспорт'''
    transport = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/'
                                               'div/table/tbody/tr[2]/td[5]/table/tbody/tr[5]/td/div/div[1]/select/option')
    variation_transport = variations(transport)
    #for i in range(0, len(variation_transport)):
        #print(variation_transport[i])
    for i in range(0,len(transport)):
        if transport[i].text == 'будь-який':
            transport[i].click

    '''Клацаем поиск'''
    driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/div[1]/div[2]/div[2]/div[3]/div/table/tbody/tr[3]/td/table/tbody/tr/td').click()


    '''высчитываем все карточки, которые есть у нас в БД'''
    cards_db = []
    for id in UserSearchExperiment:
        cards_db.append(id.id_card)
    actual_cards = [] # создаём поле с актуальными карточками

    '''Извлекаем информацию из каждой картчоки'''
    cards = driver.find_elements(By.CLASS_NAME, 'request_card')
    for card in cards:
        route = card.find_elements(By.CLASS_NAME, 'locality') # выбираем маршщрут из div
        route_start = route[0].text
        route_end = route[1].text
        try:
            distance = card.find_element(By.CLASS_NAME, 'distance').text
        except:
            distance = '???'
        try:
            price = card.find_element(By.CLASS_NAME, 'price_main').text.replace('\n ','')
        except:
            price = '???'
        try:
            price_on_km = card.find_element(By.CLASS_NAME, 'price_additional').text
        except:
            price_on_km = '???'
        try:
            truck_type = card.find_element(By.CLASS_NAME, 'truck_type').text
        except:
            truck_type = 'none'
        try:
            weight = card.find_element(By.CLASS_NAME, 'weight').text
        except:
            weight = 'none'
        try:
            volume = card.find_element(By.CLASS_NAME, 'cube').text
        except:
            volume = '???'
        cargo_type = card.find_element(By.CLASS_NAME, 'cargo_type').text
        id_card = card.get_attribute('data-request_id')
        try:
            find_buttons_information = card.find_element(By.CLASS_NAME, 'show_request_info_btn').click()
            #time.sleep(3)

        except:
            print('нету кнопки')
        #contact_name = card.find_element(By.CLASS_NAME, 'contact_name').text
        #contacts = card.find_elements(By.CLASS_NAME, 'value')
        #print(contacts)

        print(route_start)
        print(route_end)
        print(distance)
        print(price)
        print(price_on_km)
        print(truck_type)
        print(weight)
        print(volume)
        #print(contact_name)
        print('_____________________________________')

    '''
        if route_start != '' and id_card not in cards_db:
            UserSearchExperiment.create(
                                        db_user = 'valera',
                                        route_start=route_start,
                                        route_end=route_end,
                                        distance=distance,
                                        price=price,
                                        price_on_km=price_on_km,
                                        truck_type=truck_type,
                                        weight=weight,
                                        volume=volume,
                                        cargo_type=cargo_type,
                                        id_card=id_card
                                        )
    
            msg = str(f'Начало рейса - {route_start} Конец рейса - {route_end} Растояние - {distance} Цена - {price} '
                  f'Цена за км - {price_on_km} Типа автомобиля - {truck_type} Весс - {weight} Объём - {volume}'
                  f'Тип груза {cargo_type}')
            bot.send_message(ADMIN, msg)
        actual_cards.append(id_card)
    #print('Печатаем актуальные карточки')
    #print(actual_cards)


    for line in UserSearchExperiment:
        if line.id_card not in actual_cards:
            #print(line.id_card)
            line.delete_instance()

    '''











except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
