"""
Datos de prueba para información de cliente usando técnicas de caja negra
"""


class CustomerTestData:
    # DATOS VÁLIDOS - Casos que deberían funcionar
    VALID_CUSTOMERS = [
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "juan.perez@email.com",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "test_case": "Cliente típico"
        },
        {
            "firstName": "María",
            "lastName": "García",
            "email": "maria.garcia@gmail.com",
            "cardName": "María García",
            "cardNumber": "5555555555554444",
            "cvv": "456",
            "test_case": "Cliente con nombre femenino"
        },
        {
            "firstName": "José Luis",
            "lastName": "Rodríguez López",
            "email": "joseluis.rodriguez@hotmail.com",
            "cardName": "José Luis Rodríguez",
            "cardNumber": "378282246310005",
            "cvv": "789",
            "test_case": "Cliente con nombres compuestos"
        }
    ]

    # CASOS LÍMITE - Valores en los extremos
    BOUNDARY_CASES = [
        {
            "firstName": "A",  # Mínimo
            "lastName": "B",  # Mínimo
            "email": "a@b.co",  # Mínimo válido
            "cardName": "A B",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "test_case": "Valores mínimos válidos"
        },
        {
            "firstName": "NombreMuyLargoParaProbarLimites",  # Máximo
            "lastName": "ApellidoMuyLargoParaProbarLimites",  # Máximo
            "email": "correomuylargoparaprobarlimites@dominiomuylargoparaprobarlimites.com",
            "cardName": "NombreMuyLargo ApellidoMuyLargo",
            "cardNumber": "4111111111111111",
            "cvv": "999",
            "test_case": "Valores máximos válidos"
        }
    ]

    # DATOS INVÁLIDOS - Casos que NO deberían funcionar
    INVALID_CUSTOMERS = [
        # Campos vacíos
        {
            "firstName": "",
            "lastName": "Pérez",
            "email": "test@email.com",
            "cardName": "Test",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "firstName vacío",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "",
            "email": "test@email.com",
            "cardName": "Juan",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "lastName vacío",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "email vacío",
            "should_fail": True
        },

        # Emails inválidos
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "email-sin-arroba",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "email sin @",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "@sinusuario.com",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "email sin usuario",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "usuario@",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "123",
            "expected_error": "email sin dominio",
            "should_fail": True
        },

        # Tarjetas inválidas
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "juan@test.com",
            "cardName": "Juan Pérez",
            "cardNumber": "",
            "cvv": "123",
            "expected_error": "tarjeta vacía",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "juan@test.com",
            "cardName": "Juan Pérez",
            "cardNumber": "1234",
            "cvv": "123",
            "expected_error": "tarjeta muy corta",
            "should_fail": True
        },
        {
            "firstName": "Juan",
            "lastName": "Pérez",
            "email": "juan@test.com",
            "cardName": "Juan Pérez",
            "cardNumber": "4111111111111111",
            "cvv": "",
            "expected_error": "CVV vacío",
            "should_fail": True
        }
    ]
