from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class Cost_Tracker:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.max = data['max']
        self.unit_name = data['unit_name']
        self.unit_amount = data['unit_amount']
        self.cost = data['cost']
        self.world_id = data['world_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cost_trackers;"
        return connectToMySQL('dnd_clock').query_db(query)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cost_trackers WHERE id = %(id)s;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def update_max(cls, data):
        query = "UPDATE cost_trackers SET max = %(max)s WHERE id = %(id)s;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def update_unit_amount(cls, data):
        query = "UPDATE cost_trackers SET unit_amount = %(unit_amount)s WHERE id = %(id)s;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def update_cost(cls, data):
        query = "UPDATE cost_trackers SET cost = %(cost)s WHERE id = %(id)s;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def remove(cls, data):
        query = "DELETE FROM cost_trackers WHERE id = %(id)s;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def add(cls, data):
        query = "INSERT INTO cost_trackers (name, max, unit_name, unit_amount, cost, world_id) VALUES (%(name)s, %(max)s, %(unit_name)s, %(unit_amount)s, %(cost)s, 1);"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def get_total(cls):
        trackers = Cost_Tracker.get_all()
        sum = 0
        for i in range(len(trackers)):
            amount = int(trackers[i]['max']) - int(trackers[i]['unit_amount'])
            sum += amount * int(trackers[i]['cost'])
        return sum