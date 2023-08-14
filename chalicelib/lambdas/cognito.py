from sqlalchemy.orm import Session
from chalicelib.apps.users.models import User
from app import app


@app.lambda_function(name="PostCognitoConfirmation")
def post_cognito_confirmation(event, context):
    user_id = event['request']['userAttributes']['sub']
    username = event['userName']
    email = event['request']['userAttributes']['email']

    with Session(app.engine) as session:
        user = User(
            id=user_id,
            username=username,
            email=email,
        )
        session.add(user)
        session.commit()
    return event
