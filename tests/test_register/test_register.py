from endpoints_models.register.model import DataRegister, ResponseRegister


def test_register(app):
    """"""
    data = DataRegister.random()
    response = app.register.post_registred(data=data, type_response=ResponseRegister)
    assert response.status_code == 201, "Check code"
