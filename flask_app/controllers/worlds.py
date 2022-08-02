from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.cost_tracker import Cost_Tracker
from flask_app.models.world import World

@app.route('/')
def show_world_info():
    world = World.get()
    trackers = Cost_Tracker.get_all()
    sum = Cost_Tracker.get_total()
    month_name = World.month_to_string()
    display_hour = World.get_display_hour()
    if int(world['hour']) > 11:
        meridian = "PM"
    elif int(world['hour']) <= 11:
        meridian = "AM"
    return render_template('world_info.html', world = world, trackers=trackers, sum = sum, month_name = month_name, meridian = meridian, display_hour = display_hour)

@app.route('/add_minute')
def add_minute():
    World.modify_minute(True)
    return redirect('/')

@app.route('/remove_minute')
def remove_minute():
    World.modify_minute(False)
    return redirect('/')

@app.route('/add_hour')
def modify_hour():
    World.modify_hour(True)
    return redirect('/')

@app.route('/remove_hour')
def remove_hour():
    World.modify_hour(False)
    return redirect('/')

@app.route('/add_day')
def add_day():
    World.modify_day(True)
    return redirect('/')

@app.route('/remove_day')
def remove_day():
    World.modify_day(False)
    return redirect('/')

@app.route('/add_month')
def add_month():
    World.modify_month(True)
    return redirect('/')

@app.route('/remove_month')
def remove_month():
    World.modify_month(False)
    return redirect('/')

@app.route('/add_year')
def add_year():
    World.modify_year(True)
    return redirect('/')

@app.route('/remove_year')
def remove_year():
    World.modify_year(False)
    return redirect('/')

@app.route('/custom_date')
def date_form():
    months = [
        "Dusha",
        "Skal",
        "Edogas",
        "Garn",
        "Sulta",
        "Janik",
        "Isbo",
        "Abash",
        "Evanora"
        ]
    return render_template('date_form.html', months=months)

@app.route('/update_date', methods=['POST'])
def update_date():
    month = int(request.form['month'])
    day = int(request.form['day'])
    year = int(request.form['year'])
    data = {
        "month": month,
        "day": day,
        "year": year
    }
    World.update_date(data)
    return redirect('/')