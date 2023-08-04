from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app import DATABASE
#******* constructor*************
class Recipe():
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date'] 
        self.timecooking  = data['timecooking']       
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = user.User.get_by_id({'id':self.user_id})
        #self.owner= None


    #**********CRUD Queries**********
    @classmethod
    def create_recipe(cls,data):
        query="""INSERT INTO recipes (user_id,name,description,instructions,date,timecooking) 
        VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(date)s,%(timecooking)s);"""
        # this query will return the id of the new recipe insert
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #get all recipes
    @classmethod
    def get_recipes(cls):
        query="SELECT * FROM recipes;"

        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        recipes=[]
        for row in results:
            recipes.append(cls(row))
        return recipes
    
    #get one recipe by id
    @classmethod
    def get_by_id_recipe(cls,data):
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    @classmethod
    def update_recipe(cls,data):
        query="""UPDATE recipes SET 
        name=%(name)s,description=%(description)s,instructions=%(instructions)s,date=%(date)s ,timecooking=%(timecooking)s
        WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_recipe(cls,data):
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    #validate recipe
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'])<1:
            flash("you must add a name","name")
            is_valid = False
        if len(data['description'])<3:
            flash("All fields required","description")
            is_valid = False    
        if len(data['instructions'])<3:
            flash("All fields required!","instructions")
            is_valid = False

        if len (data['date'])<0:
            flash("All fields required!","date")
            is_valid = False
        
        if len(data['timecooking'])<1:
            flash("All fields required!","timecooking")
            is_valid=False
        
        return is_valid
