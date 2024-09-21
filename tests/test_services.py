from flask_cognito_lib_custom.services import (
    cognito_service_factory,
    token_service_factory,
)
from flask_cognito_lib_custom.services.cognito_svc import CognitoService
from flask_cognito_lib_custom.services.token_svc import TokenService


def test_cognito_service_factory(cfg):
    assert isinstance(cognito_service_factory(cfg), CognitoService)


def test_token_service_factory(cfg):
    assert isinstance(token_service_factory(cfg), TokenService)
