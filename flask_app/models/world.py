from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class World:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.month = data['month']
        self.day = data['day']
        self.year = data['year']
        self.hour = data['hour']
        self.minute = data['minute']

    @classmethod
    def get(cls):
        query = "SELECT * FROM worlds WHERE id = 1"
        new_list = connectToMySQL('dnd_clock').query_db(query)
        world = new_list[0]
        return world
        
    @classmethod
    def get_display_hour(cls):
        world = World.get()
        display_hour_dict = {0:12, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11}
        display_hour = display_hour_dict[int(world['hour'])]
        return display_hour

    @classmethod
    def modify_minute(cls, is_add):
        world = World.get()
        current_minute = int(world['minute'])
        new_minute = current_minute + 1 if is_add else current_minute - 1
        if current_minute >= 5 and is_add:
            query = "UPDATE worlds SET minute = 0 WHERE id = 1;"
            World.modify_hour(True)
            return connectToMySQL('dnd_clock').query_db(query)
        elif current_minute <= 0 and not is_add:
            query = "UPDATE worlds SET minute = 5 WHERE id = 1;"
            World.modify_hour(False)
            return connectToMySQL('dnd_clock').query_db(query)
        else:
            data = {"minute": new_minute}
            query = "UPDATE worlds SET minute = %(minute)s WHERE id = 1;"
            return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def modify_hour(cls, is_add):
        world = World.get()
        current_hour = int(world['hour'])
        new_hour = current_hour + 1 if is_add else current_hour - 1
        if current_hour >= 23 and is_add:
            query = "UPDATE worlds SET hour = 0 WHERE id = 1;"
            World.modify_day(True)
            return connectToMySQL('dnd_clock').query_db(query)
        elif current_hour <= 0 and not is_add:
            query = "UPDATE worlds SET hour = 23 WHERE id = 1;"
            World.modify_day(False)
            return connectToMySQL('dnd_clock').query_db(query)
        else:
            data = {"hour": new_hour}
            query = "UPDATE worlds SET hour = %(hour)s WHERE id = 1;"
            return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def modify_day(cls, is_add):
        world = World.get()
        current_day = int(world['day'])
        new_day = current_day + 1 if is_add else current_day - 1
        day_amount = World.get_day_amount()
        if current_day >= day_amount and is_add:
            query = "UPDATE worlds SET day = 1 WHERE id = 1;"
            World.modify_month(True)
            return connectToMySQL('dnd_clock').query_db(query)
        elif current_day <= 1 and not is_add:
            days_dict = { 1: 35, 2: 34, 3: 35, 4: 32, 5: 35, 6: 34, 7: 35, 8: 34, 9: 35 }
            day_amount = days_dict[int(world['month'])]
            data = {"day_amount": day_amount}
            query = 'UPDATE worlds SET day = %(day_amount)s WHERE id = 1;'
            World.modify_month(False)
            return connectToMySQL('dnd_clock').query_db(query, data)
        else:
            data = {"day": new_day}
            query = "UPDATE worlds SET day = %(day)s WHERE id = 1;"
            return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def modify_month(cls, is_add):
        world = World.get()
        current_month = int(world['month'])
        new_month = current_month + 1 if is_add else current_month - 1
        if current_month >= 9 and is_add:
            query = "UPDATE worlds SET month = 1 WHERE id = 1;"
            World.modify_year(True)
            return connectToMySQL('dnd_clock').query_db(query)
        elif current_month <= 1 and not is_add:
            query = "UPDATE worlds SET month = 9 WHERE id = 1;"
            World.modify_year(False)
            return connectToMySQL('dnd_clock').query_db(query)
        else:
            data = {"month": new_month}
            query = "UPDATE worlds SET month = %(month)s WHERE id = 1;"
            return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def modify_year(cls, is_add):
        world = World.get()
        current_year = int(world['year'])
        new_year = current_year + 1 if is_add else current_year - 1
        data = {"year": new_year}
        query = "UPDATE worlds SET year = %(year)s WHERE id = 1;"
        return connectToMySQL('dnd_clock').query_db(query, data)

    @classmethod
    def update_date(cls, data):
        query = "UPDATE worlds SET month = %(month)s, day = %(day)s, year = %(year)s WHERE id = 1;"
        return connectToMySQL('dnd_clock').query_db(query, data)


    @classmethod
    def month_to_string(cls):
        world = World.get()
        month_dict = {
            1: "Dusha",
            2: "Skal",
            3: "Edogas",
            4: "Garn",
            5: "Sulta",
            6: "Janik",
            7: "Isbo",
            8: "Abash",
            9: "Evanora"
        }
        world_string = month_dict[int(world['month'])]
        return world_string

    @classmethod
    def get_day_amount(cls):
        world = World.get()
        days_dict = {
            1: 35, 2: 34, 3: 35, 4: 32, 5: 35, 6: 34, 7: 35, 8: 34, 9: 35
        }
        days_in_month = days_dict[world['month']]
        return days_in_month