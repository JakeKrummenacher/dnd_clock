from cmath import log
from crypt import methods
from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.cost_tracker import Cost_Tracker
from flask_app.models.world import World

@app.route('/add_max', methods = ['POST'])
def add_max():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_max = int(current_tracker[0]['max'])
    current_max += 1
    new_data = {
        "id": request.form['tracker_id'],
        "max": current_max
    }
    Cost_Tracker.update_max(new_data)
    return redirect('/')

@app.route('/remove_max', methods=['POST'])
def remove_max():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_max = int(current_tracker[0]['max'])
    current_max -= 1
    new_data = {
        "id": request.form['tracker_id'],
        "max": current_max
    }
    Cost_Tracker.update_max(new_data)
    return redirect('/')

@app.route('/add_unit', methods = ['POST'])
def add_unit():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_amount = int(current_tracker[0]['unit_amount'])
    current_amount += 1
    new_data = {
        "id": request.form['tracker_id'],
        "unit_amount": current_amount
    }
    Cost_Tracker.update_unit_amount(new_data)
    return redirect('/')

@app.route('/remove_unit', methods=['POST'])
def remove_unit():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_amount = int(current_tracker[0]['unit_amount'])
    current_amount -= 1
    new_data = {
        "id": request.form['tracker_id'],
        "unit_amount": current_amount
    }
    Cost_Tracker.update_unit_amount(new_data)
    return redirect('/')

@app.route('/add_cost', methods=['POST'])
def add_cost():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_cost = int(current_tracker[0]['cost'])
    current_cost += 1
    new_data = {
        "id": request.form['tracker_id'],
        "cost": current_cost
    }
    Cost_Tracker.update_cost(new_data)
    return redirect('/')

@app.route('/remove_cost', methods=['POST'])
def remove_cost():
    data = {
        "id": request.form['tracker_id']
    }
    current_tracker = Cost_Tracker.get_one(data)
    current_cost = int(current_tracker[0]['cost'])
    current_cost -= 1
    new_data = {
        "id": request.form['tracker_id'],
        "cost": current_cost
    }
    Cost_Tracker.update_cost(new_data)
    return redirect('/')

@app.route('/remove_tracker', methods=['POST'])
def remove_tracker():
    data = {"id": request.form['tracker_id']}
    Cost_Tracker.remove(data)
    return redirect('/')

@app.route('/tracker_form')
def tracker_form():
    print(World.get_day_amount())
    return render_template('tracker_form.html')

@app.route('/add_tracker', methods=['POST'])
def add_tracker():
    data = {
        "name": request.form['tracker_name'],
        "max": int(request.form['max']),
        "unit_name": request.form['unit_name'],
        "unit_amount": int(request.form['unit_amount']),
        "cost": int(request.form['cost'])
    }
    Cost_Tracker.add(data)
    return redirect('/')