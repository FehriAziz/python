from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self , data) :
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email=data['email']
        self.created_at=['created_at']
        self.updated_at =['updated_at']
    


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL('users-schema').query_db(query)
        users=[]
        for u in result :
            users.append(cls(u))
        return users

