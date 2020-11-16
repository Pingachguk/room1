import requests
import os.path
import urllib.request
from urllib.parse import urlparse
from datetime import datetime, timedelta

from typing import Optional
from fastapi import FastAPI, Query, Header, Cookie
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://192.168.43.235:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SERVER_IMAGES = 'http://127.0.0.1:8000/images/'
#SERVER_IMAGES = 'http://192.168.43.235:8000/images/'
API_KEY = '1a5a6f3b-4504-40b7-b286-14941fd2f635'
APP_BASIC_LOGIN = 'ServiceUserAPI'
APP_BASIC_PASSWORD = 'Gu3nevehexusihuquhycywesukuciv'
API_ADDR = 'https://cloud.1c.fitness/app/2970/hs/api/v3/'
#USER_TOKEN = 'D5CC150F1EC19169F0984D4D0A210A95' #Храним в cookie и передаем в headers

API_LIST = {
    'confirm_phone': API_ADDR + 'confirm_phone/',
    'auth_client': API_ADDR + 'auth_client/',
    'reg_and_auth_client': API_ADDR + 'reg_and_auth_client/',
    
    'client': API_ADDR + 'client/',
    'tickets': API_ADDR + 'tickets/',
    'appoint': API_ADDR + 'appointment/', 
    'appointments': API_ADDR + 'appointments/',
    
    'clubs': API_ADDR + 'clubs/',
    
    'trainers': API_ADDR + 'appointment_trainers/',
    'employee': API_ADDR + 'employee/',
    
    'times': API_ADDR + 'appointment_times/',
    'services': API_ADDR + 'appointment_services/',
    
    'shop': API_ADDR + 'price_list/'
}

# Авторизуемся на сервере API
session = requests.Session()
session.auth = (APP_BASIC_LOGIN, APP_BASIC_PASSWORD)
session.headers = {'apikey': API_KEY}

@app.get("/api/clubs")
def get_clubs():
    clubs = []
    api_keys = [
        "24955a4d-0467-4886-ba0b-1f54d5a50bb2",
        "c164bc33-4dfe-4235-bae7-0b5aa38f2452",
        "a955977a-1177-48a5-a12a-70199432c5cb",
        "1799c52b-a66a-4187-ac5a-073e4515ec46",
        "0cc5eb3f-a77e-406d-a212-aa3d514415d3",
        "19d06469-3a5e-43f9-977c-ca18324a31e1",
        "bf10824c-dab7-413d-addf-cc80c4111576",
        "1a5a6f3b-4504-40b7-b286-14941fd2f635",
        "abb08603-c6b0-4c22-989d-c61377fa3bd3",
        "9c5a3bb6-16b1-48f3-9e78-84299a619fda",
        "31b8db60-cb60-457f-bed0-69c9a3a65e84",
        "6a8a7d85-4836-4ace-a495-9a5262975b83",
        "a5d8ff5a-f6ee-421a-bd11-769fbf6b658c",
        "e25f4e9d-92ec-4750-9b84-8655bb89f0ff",
        "f7bd7973-287a-4a0e-a706-745b25758182",
        "bfbce456-def7-43d0-a8f4-725176c67341",
        "bf54b61c-9039-4df2-b837-d85c6f0cbf4f"
    ]
    
    """
    for key in api_keys:
        response = session.get(API_LIST['clubs'], headers={'apikey': key})
        response_json = response.json()
        response_data = response_json['data'][0]
        clubs.append({
            'id': response_data['id'],
            'name': response_data['title'],
            'address': response_data['title'],
            'city_code': None,
            'city': None
        })
        
    return clubs
    """
    
    result = [{"id":"bf1e201a-01c3-11eb-bbdb-005056838e97","name":"пр-т Маршала Блюхера, 6к2","address":"пр-т Маршала Блюхера, 6к2","city_code":None,"city":None},{"id":"a23e2522-e7ad-11ea-bbd8-005056838e97","name":"набережная реки Смоленки, 3к1, ЖК \"Самоцветы\"","address":"набережная реки Смоленки, 3к1, ЖК \"Самоцветы\"","city_code":None,"city":None},{"id":"e64f0bc2-0652-11eb-bbdb-005056838e97","name":"FITROOM.RU - Выборгское шоссе ","address":"FITROOM.RU - Выборгское шоссе ","city_code":None,"city":None},{"id":"22bd71b4-e7af-11ea-bbd8-005056838e97","name":"Загребский бульвар, 9, ЖК \"Радуга\"","address":"Загребский бульвар, 9, ЖК \"Радуга\"","city_code":None,"city":None},{"id":"d987364c-e7ae-11ea-bbd8-005056838e97","name":"Кудрово, Каштановая аллея, 2","address":"Кудрово, Каштановая аллея, 2","city_code":None,"city":None},{"id":"630de9d9-e7ae-11ea-bbd8-005056838e97","name":"Лыжный переулок, 2","address":"Лыжный переулок, 2","city_code":None,"city":None},{"id":"cb28be84-0651-11eb-bbdb-005056838e97","name":"Мск, 3-й Донской проезд, 1","address":"Мск, 3-й Донской проезд, 1","city_code":None,"city":None},{"id":"39158ee8-e79e-11ea-bbd8-005056838e97","name":"Московский пр-т, 183-185, ЖК \"Граф Орлов\"","address":"Московский пр-т, 183-185, ЖК \"Граф Орлов\"","city_code":None,"city":None},{"id":"97a2081f-e7ac-11ea-bbd8-005056838e97","name":"Московский пр-т, 75, ЖК \"Времена года\"","address":"Московский пр-т, 75, ЖК \"Времена года\"","city_code":None,"city":None},{"id":"d2c3b3d6-e7ad-11ea-bbd8-005056838e97","name":"Ждановская ул., д.43, кор. 1, ЖК \"Премьер Палас\"","address":"Ждановская ул., д.43, кор. 1, ЖК \"Премьер Палас\"","city_code":None,"city":None},{"id":"37948207-e7ae-11ea-bbd8-005056838e97","name":"пр-т Маршала Блюхера, 9к1, ЖК \"Фламинго\"","address":"пр-т Маршала Блюхера, 9к1, ЖК \"Фламинго\"","city_code":None,"city":None},{"id":"64b8476a-e7ad-11ea-bbd8-005056838e97","name":"пр-т Юрия Гагарина, 7","address":"пр-т Юрия Гагарина, 7","city_code":None,"city":None},{"id":"d987364c-e7ae-11ea-bbd8-005056838e97","name":"Кудрово, Каштановая аллея, 2","address":"Кудрово, Каштановая аллея, 2","city_code":None,"city":None},{"id":"915d3c3b-daff-11ea-bbd8-005056838e97","name":"Пушкин, Московское шоссе, 34","address":"Пушкин, Московское шоссе, 34","city_code":None,"city":None},{"id":"603cb73d-e7af-11ea-bbd8-005056838e97","name":"ул. Дыбенко, 8к3, ЖК \"Ренессанс\"","address":"ул. Дыбенко, 8к3, ЖК \"Ренессанс\"","city_code":None,"city":None},{"id":"42632fd3-e7af-11ea-bbd8-005056838e97","name":"ул. Красного Текстильщика, 7","address":"ул. Красного Текстильщика, 7","city_code":None,"city":None},{"id":"15281aec-07c8-11eb-bbdb-005056838e97","name":"Самара, Парковый переулок, 5","address":"Самара, Парковый переулок, 5","city_code":None,"city":None}] 
    return result
# РАБОТА С АВТОРИЗАЦИЕЙ

def get_key_by_club(club_id):
    api_keys_clubs = [
        {"club_id": "bf1e201a-01c3-11eb-bbdb-005056838e97", "key": "24955a4d-0467-4886-ba0b-1f54d5a50bb2"},
        {"club_id": "a23e2522-e7ad-11ea-bbd8-005056838e97", "key": "c164bc33-4dfe-4235-bae7-0b5aa38f2452"},
        {"club_id": "e64f0bc2-0652-11eb-bbdb-005056838e97", "key": "a955977a-1177-48a5-a12a-70199432c5cb"},
        {"club_id": "22bd71b4-e7af-11ea-bbd8-005056838e97", "key": "1799c52b-a66a-4187-ac5a-073e4515ec46"},
        {"club_id": "d987364c-e7ae-11ea-bbd8-005056838e97", "key": "0cc5eb3f-a77e-406d-a212-aa3d514415d3"},
        {"club_id": "630de9d9-e7ae-11ea-bbd8-005056838e97", "key": "19d06469-3a5e-43f9-977c-ca18324a31e1"},
        {"club_id": "cb28be84-0651-11eb-bbdb-005056838e97", "key": "bf10824c-dab7-413d-addf-cc80c4111576"},
        {"club_id": "39158ee8-e79e-11ea-bbd8-005056838e97", "key": "1a5a6f3b-4504-40b7-b286-14941fd2f635"},
        {"club_id": "97a2081f-e7ac-11ea-bbd8-005056838e97", "key": "abb08603-c6b0-4c22-989d-c61377fa3bd3"},
        {"club_id": "d2c3b3d6-e7ad-11ea-bbd8-005056838e97", "key": "9c5a3bb6-16b1-48f3-9e78-84299a619fda"},
        {"club_id": "37948207-e7ae-11ea-bbd8-005056838e97", "key": "31b8db60-cb60-457f-bed0-69c9a3a65e84"},
        {"club_id": "64b8476a-e7ad-11ea-bbd8-005056838e97", "key": "6a8a7d85-4836-4ace-a495-9a5262975b83"},
        {"club_id": "d987364c-e7ae-11ea-bbd8-005056838e97", "key": "a5d8ff5a-f6ee-421a-bd11-769fbf6b658c"},
        {"club_id": "915d3c3b-daff-11ea-bbd8-005056838e97", "key": "e25f4e9d-92ec-4750-9b84-8655bb89f0ff"},
        {"club_id": "603cb73d-e7af-11ea-bbd8-005056838e97", "key": "f7bd7973-287a-4a0e-a706-745b25758182"},
        {"club_id": "42632fd3-e7af-11ea-bbd8-005056838e97", "key": "bfbce456-def7-43d0-a8f4-725176c67341"},
        {"club_id": "15281aec-07c8-11eb-bbdb-005056838e97", "key": "bf54b61c-9039-4df2-b837-d85c6f0cbf4f"}
    ]
    
    for item in api_keys_clubs:
        if item['club_id'] == club_id:
            return item['key']

class ModelConfirmPhone(BaseModel):
    phone: str = Field(..., min_length=11)
    confirmation_code: Optional[str] = None
    
@app.post("/api/auth/confirm-phone", name='Подтверждение номера телефона')
def confirm_phone(item: ModelConfirmPhone):
    """
    Осуществляется подтверждение номера телефона клиента с помощью СМС-подтверждения. При вызове метода без передачи кода подтверждения будет сформирован и отправлен по СМС новый код подтверждения. Если передать в метод верный код подтверждения, будет возвращён ключ для установки пароля (pass_token).
    """
    item_clear = {}
    for k, v in item.dict().items():
        if v is not None:
            item_clear[k] = v
            
    response = session.post(API_LIST['confirm_phone'], json=item_clear)
    return response.json();

class ModelMarketing(BaseModel):
    utm_source: Optional[str] = Field(None, title='Сайт, откуда пришел')
    utm_medium: Optional[str] = Field(None, title='Рекламная модель')
    utm_campaing: Optional[str] = Field(None, title='Рекламная компания')
    utm_content: Optional[str] = Field(None, title='Ключевая фраза из РК')
    utm_term: Optional[str] = Field(None, title='Элемент контента, на который нажал пользователь перед переходом на сайт')
    utm_source: Optional[str] = Field(None, title='Рекламный источник')
    utm_referrer: Optional[str] = Field(None, title='Рекламная ссылка')

class ModelRegAndAuthClient(BaseModel):
    phone: str = Field(..., min_length=11, title='Номер телефона')
    pass_token: str = Field(..., title='Токен доступа из Confirm Phone')
    autopassword_to_sms: Optional[bool] = Field(False)
    password: Optional[str] = Field(None, title='Пароль')
    last_name: Optional[str] = Field(None, title='Фамилия')
    name: Optional[str] = Field(None, title='Имя')
    second_name: Optional[str] = Field(None, title='Отчество')
    email: Optional[EmailStr] = Field(None, title='Адрес почты')
    birthday: Optional[str] = Field(None, title='Дата рождения')
    club: Optional[str] = Field(None, title='Идентификатор клуба')
    marketing: Optional[ModelMarketing] = None
    
@app.post("/api/auth/reg", name="Регистрация")
def registration(item: ModelRegAndAuthClient):
    """
    Метод предназначен для авторизации клиента по номеру телефона и паролю, в замен клиент получает ключ (user_token) для инициализация клиента во время произведения операций.
    """
    item_clear = {}
    for k, v in item.dict().items():
        if v is not None:
            item_clear[k] = v
            
    response = session.post(API_LIST['reg_and_auth_client'], json=item_clear)
    return response.json();

class ModelAuth(BaseModel):
    phone: str = Field(..., min_length=11, title='Номер телефона')
    password: Optional[str] = Field(None, title='Пароль')
    
@app.post("/api/auth/login", name="Авторизация")
def login(item: ModelAuth):
    """
    Метод предназначен для авторизации клиента по номеру телефона и паролю, в замен клиент получает временный ключ(user_token) для инициализация клиента во время произведения операций.
    """
    item_clear = {}
    for k, v in item.dict().items():
        if v is not None:
            item_clear[k] = v
            
    response = session.post(API_LIST['auth_client'], json=item_clear)
    rj = response.json()
    if rj['result'] == False:
        if rj['error'] == 4003:
            return {'result': False, 'error_message': 'Не правильный логин или пароль'}
    return response.json();



# РАБОТА С КЛИЕНТОМ

@app.get("/api/client", name="Получить клиента")
def get_client(utoken: str = Header(...), club_id: str = Header(...)):
    key = get_key_by_club(club_id)
    week_name = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];
    month_name = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];
    month_short_name = ['Янв', 'Фев', 'Мар', 'Апр', 'Мая', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Нояб', 'Дек']
    client_object = {
        'office_id': None,
        'is_verified': False,
        'info': {},
        'subscriptions': {},
        'workouts': {
            'reserved': [],
            'active': [],
            'count': 0
        },
        'workouts_history': {},
        'cabinet': {
            'cover': 'https://i.pinimg.com/originals/2c/84/0e/2c840e86d494c5e809f850b00a69ad29.jpg',
            'is_editable': True
        }
    }
    
    client_response = session.get(API_LIST['client'], headers={'usertoken': utoken, 'apikey': key})
    client_json = client_response.json()
    
    tickets_response = session.get(API_LIST['tickets'], headers={'usertoken': utoken, 'apikey': key})
    tickets_json = tickets_response.json()
    
    def get_calendar_day(date):
        date = datetime.fromisoformat(date)
        return {
            'id': datetime.strftime(date, '%Y-%m-%d'),
            'day': date.day,
            'day_name': week_name[date.isoweekday() - 1],
            'month_number': date.month,
            'month_name' : month_name[date.month - 1],
            'month_short_number': str(date.day) + ' ' + month_short_name[date.month - 1],
            'date_iso': datetime.strftime(date, '%Y-%m-%d'),
            'year': date.year,
            'today': datetime.strftime(date, '%Y-%m-%d') == datetime.strftime(datetime.today(), '%Y-%m-%d') if True else False,
            'time': datetime.strftime(date, '%H:%M')
        }
    
    def get_category(title):
        categories = {
            'Пробная тренировка с тренером':'trainer',
            'Разовая тренировка с тренером':'trainer',
            'Пакет из 4 тренировок с тренером':'trainer',
            'Пакет из 8 тренировок с тренером':'trainer',
            'Пакет из 12 тренировок с тренером':'trainer'
        }
        
        for item in categories:
            if item == title:
                return categories[item]
            
    def get_flags(title):
        categories = {
            'Пробная тренировка с тренером':'trainer:first',
            'Разовая тренировка с тренером':'trainer:once',
            'Пакет из 4 тренировок с тренером':'trainer:package',
            'Пакет из 8 тренировок с тренером':'trainer:package',
            'Пакет из 12 тренировок с тренером':'trainer:package'
        }
        
        for item in categories:
            if item == title:
                return categories[item]
    
    if tickets_json['result']:
        client_object['subscription_flags'] = {'trainer': [], 'office': []}
        for item_ticket in tickets_json['data']:
            # status not_active ? при 0 на абонементе / показывать при active если 0?
            item_ticket['category_type'] = get_category(item_ticket['title'].strip())
            getter_flags = get_flags(item_ticket['title'].strip()).split(':')
            if getter_flags:
                client_object['subscription_flags'][getter_flags[0]].append(getter_flags[1])
            
    
    appointments_response = session.get(API_LIST['appointments'], headers={'usertoken': utoken, 'apikey': key})
    appointments_json = appointments_response.json()
    
    if appointments_json['result'] and (len(appointments_json['data']) > 0):
        for item_app in appointments_json['data']:
            app_club_id = item_app['club_id']
            app_appointment_id = item_app['appointment_id']
            app_key = get_key_by_club(app_club_id)
            
            appoint_response = session.get(API_LIST['appoint'], 
                        params={'club_id': app_club_id,'appointment_id': app_appointment_id}, 
                        headers={'usertoken': utoken, 'apikey': app_key})
            appoint_json = appoint_response.json()
            
            
            if appoint_json['result']:
                if not appoint_json['data']['canceled']:
                    """
                    СОХРАНЯЕМ ФОТО С СЕРВЕРА НА СВОЙ
                    """
                    if appoint_json['data']['employee']['photo']:
                        photo_name = os.path.basename(urlparse(appoint_json['data']['employee']['photo']).path)
                        check_photo = os.path.exists('images/' + photo_name)
                        if check_photo:
                            appoint_json['data']['employee']['photo'] = SERVER_IMAGES + photo_name
                        else:
                            photo_read = session.get(data['photo'])
                            photo_write = open('images/' + photo_name, 'wb')
                            photo_write.write(photo_read.content)
                            photo_write.close()
                            appoint_json['data']['employee']['photo'] = SERVER_IMAGES + photo_name
                    
                    
                    # Устанавливаем категории для записи
                    if str(appoint_json['data']['employee']['name']).strip() == 'Аренда зала':
                        appoint_json['data']['category_type'] = 'office'
                    else:
                        appoint_json['data']['category_type'] = 'trainer'
                        
                    # Категории для статуса    
                    if appoint_json['data']['status'] == 'reserved' or appoint_json['data']['status'] == 'temporarily_reserved_need_payment':
                        appoint_json['data']['status_type'] = 'reserved'
                    else:
                        appoint_json['data']['status_type'] = 'active'
                        
                        
                    # Добавляем разделенные имя и фамилию
                    employee_name = appoint_json['data']['employee']['name'].split()
                    if employee_name[0]:
                        appoint_json['data']['employee']['surname'] = employee_name[0]
                        
                    if employee_name[1]:
                        appoint_json['data']['employee']['firstname'] = employee_name[1]
                        
                    # Преобразуем дату в дату с параметрами    
                    appoint_json['data']['date_object'] = get_calendar_day(appoint_json['data']['start_date'])
                    status_type = appoint_json['data']['status_type']
                    client_object['workouts'][status_type].append(appoint_json['data'])
                    client_object['workouts']['count']+= 1
        
    client_object['office_id'] = client_json['data']['club']['id']
    client_object['info'] = client_json['data']
    client_object['subscriptions'] = tickets_json['data']
    
    # is_verified code
        
    return {'result': True, 'data': client_object}



class ModelClientUpdate(BaseModel):
    club: Optional[str] = Field(None, title='Идентификатор клуба')
    do_not_disturb: Optional[bool] = Field(None, title="Не беспокоить")
    email: Optional[EmailStr] = Field(None, title='Адрес почты')
    name: Optional[str] = Field(None, title='Имя')
    last_name: Optional[str] = Field(None, title='Фамилия')
    second_name: Optional[str] = Field(None, title='Отчество')
    birthday: Optional[str] = Field(None, title='Дата рождения')
    sex: Optional[str] = Field(None, title='Пол клиента')
    
@app.put("/api/client", name="Редактировать клиента")
def update_client(item: ModelClientUpdate, utoken: str = Header(...)):
    item_clear = {}
    for k, v in item.dict().items():
        if v is not None:
            item_clear[k] = v
            
    response = session.put(API_LIST['client'], json=item_clear, headers={'usertoken': utoken})
    print(response.content)
    return response.json();


# РАБОТА С ТРЕНЕРАМИ

# Отменяем тренеровку
@app.get("/api/training/cancel")
def get_training_cancel(club_id: Optional[str] = Query(...), appointment_id: Optional[str] = Query(...), utoken: str = Header(...)):
    key = get_key_by_club(club_id)
    
    app_response = session.delete(API_LIST['appoint'], 
                                    params={'club_id': club_id, 'appointment_id': appointment_id}, 
                                    headers={'usertoken': utoken, 'apikey': key})
    app_response_json = app_response.json()
    
    return app_response_json


# Получаем информацию о тренере
@app.get("/api/trainers/detail")
def get_trainer_detail(club_id: Optional[str] = Query(...), employee_id: Optional[str] = Query(...), utoken: str = Header(...)):
    key = get_key_by_club(club_id)
    
    employee_response = session.get(API_LIST['employee'], 
                                    params={'club_id': club_id, 'employee_id': employee_id}, 
                                    headers={'usertoken': utoken, 'apikey': key})
    employee_response_json = employee_response.json()
    
    if employee_response_json['result']:
        data = employee_response_json['data']
        if data['photo']:
            photo_name = os.path.basename(urlparse(data['photo']).path)
            check_photo = os.path.exists('images/' + photo_name)
            if check_photo:
                data['photo'] = SERVER_IMAGES + photo_name
            else:
                photo_read = session.get(data['photo'])
                photo_write = open('images/' + photo_name, 'wb')
                photo_write.write(photo_read.content)
                photo_write.close()
                data['photo'] = SERVER_IMAGES + photo_name
                
        return {'result': True, 'data': data}
    return employee_response_json


# Получаем данные о тренерах с рассписанием
@app.get("/api/trainers", name="Свободные тренера и время")
def get_trainers_all(club_id: Optional[str] = Query(...), date: Optional[str] = Query(None), time: Optional[str] = Query(None), utoken: str = Header(...)):
    key = get_key_by_club(club_id)
    week_name = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];
    month_name = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];
    month_short_name = ['Янв', 'Фев', 'Мар', 'Апр', 'Мая', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Нояб', 'Дек']
    services = {}
    trainers = {
        "result": True,
        "data": {
            "club_id": club_id,
            "office_id": None,
            #"club_object": None,
            #"timetable": [],
            #"calendar": [],
            "trainers": []
        }
    }
    
    def get_calendar_day(date):
        date = datetime.fromisoformat(date)
        return {
            'id': datetime.strftime(date, '%Y-%m-%d'),
            'day': date.day,
            'day_name': week_name[date.isoweekday() - 1],
            'month_number': date.month,
            'month_name' : month_name[date.month - 1],
            'month_short_number': str(date.day) + ' ' + month_short_name[date.month - 1],
            'date_iso': datetime.strftime(date, '%Y-%m-%d'),
            'year': date.year,
            'today': datetime.strftime(date, '%Y-%m-%d') == datetime.strftime(datetime.today(), '%Y-%m-%d') if True else False
        }
        
    
    """
    ПОЛУЧАЕМ СПИСОК УСЛУГ ДЛЯ ТРЕНЕРОВ И СТУДИИ
    """
    service_response = session.get(API_LIST['services'], params={'club_id': club_id}, headers={'usertoken': utoken, 'apikey': key})
    service_response_json = service_response.json()
    
    if service_response_json['result']:
        for item_service in service_response_json['data']:
            if item_service['title'] == "Персональная тренировка":
                services['trainer'] = item_service['id']
            elif item_service['title'] == "АРЕНДА СТУДИИ ДЛЯ ТРЕНЕРА":
                services['office'] = item_service['id']
        
    
    
    """
    ПОЛУЧАЕМ СПИСОК ТРЕНЕРОВ ДЛЯ СТУДИИ
    """
    response = session.get(API_LIST['trainers'], params={'club_id': club_id}, headers={'usertoken': utoken, 'apikey': key})
    rj = response.json()
    
    
    if rj['result']:
        for item in rj['data']:
            # Получили тренеров и заменили фотки на локальный сервер (1С не даёт смотреть фото без авторизации)
            if item['photo']:
                photo_name = os.path.basename(urlparse(item['photo']).path)
                check_photo = os.path.exists('images/' + photo_name)
                if check_photo:
                    item['photo'] = SERVER_IMAGES + photo_name
                else:
                    photo_read = session.get(item['photo'])
                    photo_write = open('images/' + photo_name, 'wb')
                    photo_write.write(photo_read.content)
                    photo_write.close()
                    item['photo'] = SERVER_IMAGES + photo_name
        
            
            # Если это студия а не тренер, записываем главный ID
            if not item['position']['id']:
                trainers['data']['office_id'] = item['id']
                name_split = item['name'].split()
                item['name'] = name_split[0] + ' ' + name_split[1] 
                print(item['name'])
                #trainers['data']['club_object'] = item
        
        
            """
            ПОЛУЧАЕМ ВРЕМЯ ТРЕНЕРА С ПАРАМЕТРОМ УСЛУГИ
            """
            service_id = None
            if item['id'] == trainers['data']['office_id']:
                service_id = services['office']
            else:
                service_id = services['trainer']
                
            response_times = session.get(
                API_LIST['times'], 
                params={'club_id': club_id, 'employee_id': item['id'], 'service_id': service_id}, 
                headers={'usertoken': utoken, 'apikey': key}
            )
            
            response_times_json = response_times.json()['data']
            if len(response_times_json):
                times = {}
                
                for item_time in response_times_json:
                    item_date_convert = datetime.fromisoformat(item_time['date_time'])
                    item_date_string = datetime.strftime(item_date_convert, '%Y-%m-%d')
                    item_hour = int(datetime.strftime(item_date_convert, '%H'))
                    item_season = None

                    # Определяем время суток
                    if item_hour >= int('06') and item_hour <= int('11'): item_season = 'morning'
                    if item_hour >= int('12') and item_hour <= int('17'): item_season = 'day'
                    if item_hour >= int('18') and item_hour <= int('23'): item_season = 'evening'
                    if item_hour >= int('00') and item_hour <= int('05'): item_season = 'night'
                    
                    if not item_date_string in times:
                        times[item_date_string] = {
                            "morning": {
                                "season": 'morning',
                                "season_name": 'Утро',
                                "time_list": []
                            },
                            "day": {
                                "season": 'day',
                                "season_name": 'День',
                                "time_list": []
                            },
                            "evening": {
                                "season": 'evening',
                                "season_name": 'Вечер',
                                "time_list": []
                            },
                            "night": {
                                "season": 'night',
                                "season_name": 'Ночь',
                                "time_list": []
                            }
                        }
                    
                    times[item_date_string][item_season]['time_list'].append({
                            'time': item_time['time'],
                            'status': 'free'
                        })
                    
                calendar = {}
                date_times = {}
                for item_time in response_times_json:
                    item_date_convert = datetime.fromisoformat(item_time['date_time'])
                    item_date_string = datetime.strftime(item_date_convert, '%Y-%m-%d')
                    calendar[item_date_string] = get_calendar_day(item_time['date_time'])
                    
                    if not item_date_string in date_times:
                        date_times[item_date_string] = []
                        
                    date_times[item_date_string].append(item_time['time'])
                    
                #item['timetable'] = response_times_json
                item['calendar'] = calendar
                item['times'] = times
                item['date_times'] = date_times
                trainers['data']['trainers'].append(item)
        
    return trainers


# АБОНЕМЕНТЫ МАГАЗИН

@app.get("/api/shop/products", name="Абонементы / каталог товаров")
def get_shop_products(club_id: Optional[str] = Query(...), utoken: str = Header(...)):
    key = get_key_by_club(club_id)
    subscriptions = {
        'first': {
            'trainer': []
        },
        'once': {
            'office': [],
            'trainer': []  
        },
        'package': {
            'office': [],
            'trainer': []
        }
    }
    
    def get_category(title):
        categories = {
            'Пробная тренировка с тренером': {'first': 'trainer'},
            'Разовая тренировка с тренером': {'once': 'trainer'},
            'Пакет из 4 тренировок с тренером': {'package':'trainer'},
            'Пакет из 8 тренировок с тренером': {'package':'trainer'},
            'Пакет из 12 тренировок с тренером': {'package':'trainer'}
        }
        
        for item in categories:
            if item == title:
                return categories[item]
    
    response = session.get(API_LIST['shop'], params={'club_id': club_id}, headers={'usertoken': utoken, 'apikey': key})    
    response_json = response.json()
    
    if response_json['result']:
        data = response_json['data']
        for item in data:
            category = get_category(item['title'].strip())
            
            if category:
                # Получаем название первого индекса с названием категории
                type_category = next(iter(category))
                item['category_type'] = category[type_category]
                subscriptions[type_category][category[type_category]].append(item)
            
    return {
        'result': True,
        'data': subscriptions
    }
    
    
class ModelSubscriptionWrite(BaseModel):
    club_id: Optional[str] = Field(...)
    employee_id: Optional[str] = Field(...)
    date: Optional[str] = Field(...)
    time: Optional[str] = Field(...)


# ЗАПИСЬ НА ТРЕНЕРОВКУ С АБОНЕМЕНТА
@app.post("/api/subscription/write", name="Запись на тренеровку с абонемента")
def subscriptions_write(item: ModelSubscriptionWrite,
                        utoken: str = Header(...)):
    
    key = get_key_by_club(item.club_id)
    service_id = None
    
    # ВЫЯСНЯЕМ ID УСЛУГИ ТРЕНЕРА
    response_trainer = session.get(API_LIST['services'], 
                                   params={'club_id': item.club_id, 'employee_id': item.employee_id}, 
                                   headers={'usertoken': utoken, 'apikey': key})    
    response_trainer_json = response_trainer.json()
    
    if response_trainer_json['result']:
        if response_trainer_json['data']:
            service_id = response_trainer_json['data'][0]['id']
            
            write_object = {
                'club_id': item.club_id,
                'employee_id': item.employee_id,
                'service_id': service_id,
                'date_time': item.date + ' ' + item.time
            }
            
            response_write = session.post(API_LIST['appoint'],
                                         json=write_object,
                                         headers={'usertoken': utoken, 'apikey': key})
            
    return response_write.json()
    