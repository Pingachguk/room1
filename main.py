import requests
from typing import Optional
from fastapi import FastAPI, Query, Header
from pydantic import BaseModel, EmailStr, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = '1a5a6f3b-4504-40b7-b286-14941fd2f635'
APP_BASIC_LOGIN = 'ServiceUserAPI'
APP_BASIC_PASSWORD = 'Gu3nevehexusihuquhycywesukuciv'
API_ADDR = 'https://cloud.1c.fitness/app/2970/hs/api/v3/'
#USER_TOKEN = 'D5CC150F1EC19169F0984D4D0A210A95' #Храним в cookie и передаем в headers

API_LIST = {
    'confirm_phone': API_ADDR + 'confirm_phone/',
    'auth_client': API_ADDR + 'auth_client/',
    'reg_and_auth_client': API_ADDR + 'reg_and_auth_client/',
    
    'client': API_ADDR + 'client/'
}

# Авторизуемся на сервере API
session = requests.Session()
session.auth = (APP_BASIC_LOGIN, APP_BASIC_PASSWORD)
session.headers = {'apikey': API_KEY}


# РАБОТА С АВТОРИЗАЦИЕЙ

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
def get_client(utoken: str = Header(...)):
    response = session.get(API_LIST['client'], headers={'usertoken': utoken})
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