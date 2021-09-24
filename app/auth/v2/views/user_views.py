from pdb import set_trace
from flask_restful import Resource, reqparse
from app.auth.v2.models.user_models import UserModel

user_model_view = UserModel()

class UserRegister(Resource):
    """
    User class view for register endpoint
    """

    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Please input an email")
    parser.add_argument("username", type=str, required=True, help="Please input your name")
    parser.add_argument("password", type=str, required=True, help="Please input your password")
    parser.add_argument("confirm_password", type=str, required=True, help="Please confirm your password")



    def post(self):
        """
        HTTP method to register a new user
        """
        try:
            args = UserRegister.parser.parse_args()
            username = args.get('username')
            email = args.get('email')
            password = args.get('password')
            confirm_password = args.get('confirm_password')
        except Exception as e:
            return {
                "status": 400,
                "error": "Invalid Key error {}".format(e)
            }, 400

        new_user = user_model_view.create_user(
            username=args.get('username'),
            email=args.get('email'),
            password=args.get('password'),
            confirm_password=args.get('confirm_password')
        )

        return {
            "status": 201,
            "data": new_user
        }, 201
