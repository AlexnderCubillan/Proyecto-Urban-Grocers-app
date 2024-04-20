import sender_stand_request
import data

# Función para obtener el cuerpo de la solicitud del kit de producto
def get_kit_body(kit_name, auth_token):
    # Crear una copia de los encabezados para no modificar el original
    headers_copy = data.headers.copy()
    # Añadir el token de autenticación al encabezado 'Authorization'
    headers_copy['Authorization'] = f'Bearer {auth_token}'
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_kit_body = data.kit_name.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = kit_name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body, headers_copy

# Función para obtener el token de autenticación de un nuevo usuario
def get_new_user_token():
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable user_response
    response_new_user = sender_stand_request.post_new_user(data.user_body)
    # Extrae el auth_token de registro de nuevo usuario
    user_auth_token = response_new_user.json().get('authToken')
    return user_auth_token

# Función para afirmar positivamente la creación de un kit de producto
def positive_assert(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201

def negative_assert_no_name(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit_response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def negative_assert_symbol(kit_name, auth_token):
    # Obtener el cuerpo de la solicitud y los encabezados actualizados
    kit_body, headers = get_kit_body(kit_name, auth_token)
    # El resultado se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert kit.response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert kit.response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                             "Los nombres solo pueden contener caracteres latinos,  "\
                                             "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

# Prueba 1.
def test_1():
    auth_token = get_new_user_token()
    positive_assert("a",auth_token)

# Prueba 2.
def test_2():
    auth_token = get_new_user_token()
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",auth_token)

def test_3():
    auth_token = get_new_user_token()
    negative_assert_no_name("",auth_token)

def test_4():
    auth_token = get_new_user_token()
    negative_assert_no_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",auth_token)

def test_5():
    auth_token = get_new_user_token()
    positive_assert("\"№%@\",",auth_token)

def test_6():
    auth_token = get_new_user_token()
    positive_assert(" A Aaa ",auth_token)

def test_7():
    auth_token = get_new_user_token()
    positive_assert("123",auth_token)

def test_8():
    auth_token = get_new_user_token()
    negative_assert_symbol({},auth_token)

def test_9():
    auth_token = get_new_user_token()
    negative_assert_symbol( { "name": 123 },auth_token)