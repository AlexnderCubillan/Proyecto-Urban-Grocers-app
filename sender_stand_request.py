import configuration
import requests
import data
# Funcion para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Enviar la solicitud para crear un nuevo usuario
response_new_user = post_new_user(data.user_body);

# Extraer el authToken del JSON de respuesta
auth_token = response_new_user.json().get('authToken')

print(response_new_user.status_code)
print("Auth Token:", auth_token)

# Funcion para crear un nuevo kit de producto
def post_new_client_kit(bodykit):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=bodykit,
                         headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer "+str(auth_token)}
                         )

response_new_kit = post_new_client_kit(data.kit_name);
print(response_new_kit.status_code)
print(response_new_kit.json())


