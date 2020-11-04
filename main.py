import requests
import os.path
import urllib.request
from urllib.parse import urlparse

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
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SERVER_IMAGES = 'http://127.0.0.1:8000/images/'
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
    'clubs': API_ADDR + 'clubs/',
    'trainers': API_ADDR + 'appointment_trainers/'
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
    
    result = [{"id":"bf1e201a-01c3-11eb-bbdb-005056838e97","name":"FITROOM.RU - пр-т Маршала Блюхера 6","address":"FITROOM.RU - пр-т Маршала Блюхера 6","city_code":None,"city":None},{"id":"a23e2522-e7ad-11ea-bbd8-005056838e97","name":"FITROOM.RU - В.О. наб. реки Смоленки, ЖК Самоцветы","address":"FITROOM.RU - В.О. наб. реки Смоленки, ЖК Самоцветы","city_code":None,"city":None},{"id":"e64f0bc2-0652-11eb-bbdb-005056838e97","name":"FITROOM.RU - Выборгское шоссе ","address":"FITROOM.RU - Выборгское шоссе ","city_code":None,"city":None},{"id":"22bd71b4-e7af-11ea-bbd8-005056838e97","name":"FITROOM.RU - Загребский бульвар, ЖК Радуга.","address":"FITROOM.RU - Загребский бульвар, ЖК Радуга.","city_code":None,"city":None},{"id":"d987364c-e7ae-11ea-bbd8-005056838e97","name":"FITROOM.RU - Каштановая аллея, Новый Оккервиль","address":"FITROOM.RU - Каштановая аллея, Новый Оккервиль","city_code":None,"city":None},{"id":"630de9d9-e7ae-11ea-bbd8-005056838e97","name":"FITROOM.RU - Лыжный переулок","address":"FITROOM.RU - Лыжный переулок","city_code":None,"city":None},{"id":"cb28be84-0651-11eb-bbdb-005056838e97","name":"FITROOM.RU - МОСКВА  3-Донской проезд ","address":"FITROOM.RU - МОСКВА  3-Донской проезд ","city_code":None,"city":None},{"id":"39158ee8-e79e-11ea-bbd8-005056838e97","name":"FITROOM.RU - Московский пр.  ЖК Граф Орлов","address":"FITROOM.RU - Московский пр.  ЖК Граф Орлов","city_code":None,"city":None},{"id":"97a2081f-e7ac-11ea-bbd8-005056838e97","name":"FITROOM.RU - Московский пр., ЖК Времена Года","address":"FITROOM.RU - Московский пр., ЖК Времена Года","city_code":None,"city":None},{"id":"d2c3b3d6-e7ad-11ea-bbd8-005056838e97","name":"FITROOM.RU - П.С., ул. Ждановская, ЖК Премьер Палас","address":"FITROOM.RU - П.С., ул. Ждановская, ЖК Премьер Палас","city_code":None,"city":None},{"id":"37948207-e7ae-11ea-bbd8-005056838e97","name":"FITROOM.RU - пр. Маршала Блюхера, ЖК Фламинго.","address":"FITROOM.RU - пр. Маршала Блюхера, ЖК Фламинго.","city_code":None,"city":None},{"id":"64b8476a-e7ad-11ea-bbd8-005056838e97","name":"FITROOM.RU - пр. Юрия Гагарина  ЖК Космос","address":"FITROOM.RU - пр. Юрия Гагарина  ЖК Космос","city_code":None,"city":None},{"id":"d987364c-e7ae-11ea-bbd8-005056838e97","name":"FITROOM.RU - Каштановая аллея, Новый Оккервиль","address":"FITROOM.RU - Каштановая аллея, Новый Оккервиль","city_code":None,"city":None},{"id":"915d3c3b-daff-11ea-bbd8-005056838e97","name":"FITROOM.RU - Пушкин Московское шоссе ","address":"FITROOM.RU - Пушкин Московское шоссе ","city_code":None,"city":None},{"id":"603cb73d-e7af-11ea-bbd8-005056838e97","name":"FITROOM.RU - ул. Дыбенко,  ЖК Ренессанс","address":"FITROOM.RU - ул. Дыбенко,  ЖК Ренессанс","city_code":None,"city":None},{"id":"42632fd3-e7af-11ea-bbd8-005056838e97","name":"FITROOM.RU - ул. Красного Текстильщика","address":"FITROOM.RU - ул. Красного Текстильщика","city_code":None,"city":None},{"id":"15281aec-07c8-11eb-bbdb-005056838e97","name":"FITROOM.RU- САМАРА Парковый переулок","address":"FITROOM.RU- САМАРА Парковый переулок","city_code":None,"city":None}];
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
    response = session.get(API_LIST['client'], headers={'usertoken': utoken, 'apikey': key})
    return response.json()

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
            
    print(item_clear)
    response = session.put(API_LIST['client'], json=item_clear, headers={'usertoken': utoken})
    return response.json();


# РАБОТА С ТРЕНЕРАМИ

@app.get("/api/trainers", name="Получить тренеров")
def get_trainers(utoken: str = Header(...), club_id: str = Header(...)):
    key = get_key_by_club(club_id)
    response = session.get(API_LIST['trainers'], params={'club_id': club_id}, headers={'usertoken': utoken, 'apikey': key})
    rj = response.json()
    
    if rj['result']:
        for item in rj['data']:
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
        
    return rj