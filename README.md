Este código Python se encarga de realizar solicitudes en la aplicación "Urban Grocers" para la prueba en la crea kits de productos en base a la siguiente lista de comprobación:

№ Prueba: 1
Descripción: El número permitido de caracteres (1): kit_body = { "name": "a"}        
Estado de Respuesta: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

№ Prueba: 2
Descripción: El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
Estado de Respuesta: Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

№ Prueba: 3
Descripción: El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	
Estado de Respuesta:Código de respuesta: 400

№ Prueba: 4
Descripción: El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
Estado de Respuesta: Código de respuesta: 400

№ Prueba: 5
Descripción: Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	
Estado de Respuesta: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

№ Prueba: 6
Descripción: Se permiten espacios: kit_body = { "name": " A Aaa " }	
Estado de Respuesta: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

№ Prueba: 7
Descripción: Se permiten números: kit_body = { "name": "123" }	
Estado de Respuesta: Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

№ Prueba: 8
Descripción: El parámetro no se pasa en la solicitud: kit_body = { }
Estado de Respuesta: Código de respuesta: 400 

№ Prueba: 9
Descripción: Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
Estado de Respuesta: Código de respuesta: 400

Se crearon los modulos: configuration.py, data.py, sender_stand_request.py, create_kit_name_kit_test.py

En 'configuration.py', se definen las siguiente variables:
URL_SERVICE: Esta variable almacena la URL base del servicio web al que se realizarán las solicitudes.
CREATE_USER_PATH: Esta variable representa la ruta específica para crear nuevos usuarios en el servicio.
La ruta completa para crear un usuario sería la concatenación de URL_SERVICE y CREATE_USER_PATH.
KITS_PATH: Similar a la variable anterior, esta representa la ruta para crear nuevos kits de productos.
La ruta completa para crear un kit sería la concatenación de URL_SERVICE y KITS_PATH.

En 'data.py', se define lo siguiente:
headers: Este diccionario define los encabezados que se utilizarán en las solicitudes HTTP.
En este caso, solo se establece el encabezado "Content-Type" con el valor "application/json". Esto indica que los datos enviados en el cuerpo de la solicitud estarán en formato JSON.
user_body: Este diccionario representa los datos de un usuario.
Contiene tres campos:
"firstName": El nombre del usuario (en este caso, “Max”).
"phone": El número de teléfono del usuario (en este ejemplo, “+10005553535”).
"address": La dirección del usuario (aquí, “8042 Lancaster Ave.Hamburg, NY”).
kit_name: Este diccionario que contiene el campo "name" tiene el valor “Mi conjunto”.
token: Este diccionario representa un token de autenticación.
El campo "authToken" contiene un valor de token (en este caso, “jknnFApafP4awfAIFfafam2fma”).

En 'sender_stand_request.py' se definen las siguiente funciones:
Función 'post_new_user(body)': Esta función se encarga de enviar una solicitud POST a la URL definida por configuration.URL_SERVICE y configuration.CREATE_USER_PATH. El cuerpo de la solicitud (body) se pasa en formato JSON. 
La función devuelve la respuesta de la solicitud POST, que es el resultado de intentar crear un nuevo usuario en el servicio web.

Función 'post_new_client_kit(bodykit, token)': Similar a la función anterior, esta función envía una solicitud POST para crear un nuevo kit de producto. La URL para la solicitud se compone de configuration.URL_SERVICE y configuration.KITS_PATH. El cuerpo de la solicitud (bodykit) se pasa en formato JSON. Los encabezados incluyen el tipo de contenido (Content-Type) y el token de autorización (Authorization), que se concatena con el token proporcionado. La función devuelve la respuesta de la solicitud POST, que es el resultado de intentar crear un nuevo kit de producto en el servicio web. 

En 'create_kit_name_kit_test.py' se definen varias funciones:

get_kit_body(kit_name, auth_token): Esta función crea un cuerpo de solicitud para un “kit de producto” con un nombre específico y un token de autenticación. El cuerpo de la solicitud incluye el nombre del kit y los encabezados actualizados con el token.
get_new_user_token(): Obtiene un token de autenticación para un nuevo usuario.
positive_assert(kit_name, auth_token): Realiza una solicitud para crear un nuevo kit de producto con un nombre específico y un token de autenticación. Luego, verifica que el código de estado de la respuesta sea 201 (creación exitosa).
negative_assert_no_name(kit_name, auth_token): Realiza una solicitud similar, pero sin proporcionar un nombre para el kit. Verifica que la respuesta tenga un código de estado 400 y un mensaje de error adecuado.
negative_assert_symbol(kit_name, auth_token): Realiza otra solicitud, pero con un nombre que contiene caracteres no permitidos. Verifica que la respuesta tenga un código de estado 400 y un mensaje de error adecuado.

Finalmente se desarrollan las funciones de prueba de acuerdo a la lista de comprobación antes mencionada.

Para la ejecución correcta de los modulos se necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
Se ejecutan todas las pruebas con el comando pytest.
