import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_kit_body(name):
    current_kitbody = data.kit_bodydata.copy()
    current_kitbody["name"] = name
    return current_kitbody

def get_new_user_token():
    user_created = post_new_user(data.user_body.copy())
    auth_token = user_created.json()["authToken"]
    token = data.headers.copy()
    token["Authorization"] = f"Bearer {auth_token}"
    return token

def post_new_client_kit(kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                          json=kit_body,  # inserta el cuerpo de solicitud
                          headers=auth_token)  # inserta los encabezados
