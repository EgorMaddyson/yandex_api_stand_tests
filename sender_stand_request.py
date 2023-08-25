import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=product_ids,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = get_docs()
response = get_logs()
response = get_users_table()
response = post_new_user(data.user_body)
response = post_products_kits(data.product_ids)

print(response.status_code, '\n',)
