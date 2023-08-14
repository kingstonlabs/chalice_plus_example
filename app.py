from chalice import Chalice, CORSConfig, CognitoUserPoolAuthorizer
from chalice_plus.urls import register_urls
from sqlalchemy import create_engine

from chalicelib.lambdas import register_lambdas
from chalicelib.urls import urlpatterns
from chalicelib.settings import (
    COGNITO_USER_POOL_ARN, COGNITO_USER_POOL_NAME,
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_NAME,
)


app = Chalice(app_name='chalice-plus-example')
app.engine = create_engine(
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
)

authorizer = CognitoUserPoolAuthorizer(
    COGNITO_USER_POOL_NAME,
    provider_arns=[COGNITO_USER_POOL_ARN]
)

cors_config = CORSConfig(allow_headers=['X-Fields'])

register_urls(app, urlpatterns, cors=cors_config, authorizer=authorizer)
register_lambdas()
