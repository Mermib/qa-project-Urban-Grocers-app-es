import sender_stand_request
import data

def positive_assert(kit_body):
    #Actualiza el campo name de data kit_body
    kit_body_current = sender_stand_request.get_kit_body(kit_body)

    #Respuesta de crear un kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body_current, sender_stand_request.get_new_user_token())

    # Comprueba si la respuesta contiene el código 201
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body

def negative_assert_code_400(kit_body):
    # Actualiza el campo name de data kit_body
    kit_body = sender_stand_request.get_kit_body(kit_body)

    # Respuesta de crear un kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_new_user_token())

    # Comprueba si la respuesta contiene el código 400.
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_name(kit_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.get_new_user_token())

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


#tests
#Prueba 1, nombre con una letra
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Prueba 2, nombre con 511 letras
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3, nombre sin letra
def test_create_kit_0_letter_in_name_get_error_response():
    #negative_assert_code_400("")
    mykit_body = sender_stand_request.get_kit_body("")
    negative_assert_no_name(mykit_body)

#Prueba 4, nombre con 512 letras
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5, nombre con simbolos
def test_create_kit_special_letter_in_name_get_success_response():
    positive_assert('"№%@","')

#Prueba 6, nombre con espacios
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa ")

#Prueba 7, nombre con numeros
def test_create_numbers_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba 8, El parámetro no se pasa en la solicitud
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    mykit_body = data.kit_bodydata.copy()

    # El parámetro "name" se elimina de la solicitud
    mykit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(mykit_body)

# Prueba 9, Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    mykit_body = sender_stand_request.get_kit_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(mykit_body, sender_stand_request.get_new_user_token())

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400