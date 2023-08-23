from flask import Flask, render_template, redirect, url_for, session
from forms import (AddUser, FindUsers)
import json

import os
here = os.path.dirname(__file__)
FILE_PATH = "users.json"
FILE_PATH = os.path.join(here, FILE_PATH)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

def get_all(items, condition, status):
    temp = []
    for item in items:
        if item[condition] == status:
            temp.append(item)
    return temp

@app.route('/', methods=["GET","POST"])
def index():
    
    with open(FILE_PATH, "r") as user_file:
        users = json.load(user_file)["users"]
    count = len(users)
    
    return render_template(
        "index.html",
        count = count,
    )

@app.route('/add', methods=["GET","POST"])
def add_user():
    add_user = AddUser()
    
    with open(FILE_PATH, "r") as user_file:
        users = json.load(user_file)
        
    if add_user.validate_on_submit():
        name = add_user.name.data
        course = add_user.course.data
        hall = add_user.hall.data
        block = add_user.block.data
        flat = str(add_user.flat.data)
        
        # Handle optional fields
        if add_user.ig.data is not None:
            ig = add_user.ig.data
        else:
            ig = "Not provided"
        if add_user.sc.data is not None:
            sc = add_user.sc.data
        else:
            sc = "Not provided"
        if add_user.room.data is not None:
            room = add_user.room.data
        else:
            room = "Not provided"
            
        new_user = {
            "name": f"{name}",
            "course": f"{course}",
            "ig": f"{ig}",
            "sc": f"{sc}",
            "hall": f"{hall}",
            "block": f"{block}",
            "flat": f"{flat}",
            "room": f"{room}",
        }
        
        users["users"].append(new_user)
        with open(FILE_PATH, "w+") as user_file:
            json.dump(users, user_file, indent=4)
        
        session["hall"] = hall
        session["block"] = block
        session["flat"] = flat
           
        return redirect(url_for("display"))

    return render_template(
        "add_user.html", 
        add_user = add_user)

@app.route('/find', methods=["GET","POST"])
def find():
    find_users = FindUsers()
        
    if find_users.validate_on_submit():
        
        hall = find_users.hall.data
        block = find_users.block.data
        flat = str(find_users.flat.data)
        
        session["hall"] = hall
        session["block"] = block
        session["flat"] = flat
        
        return redirect( 
            url_for("display")
        )
        
        

    return render_template(
        "find.html",
        find_users = find_users
    )
    
@app.route('/display', methods=["GET","POST"])
def display():
    
    hall = session.get("hall")
    block = session.get("block")
    flat = session.get("flat")
    
    print(type(hall))
    print(type(block))
    print(type(flat))
    
    with open(FILE_PATH, "r") as user_file:
        users = json.load(user_file)["users"]
            
    users = get_all(users, "hall", hall)
        
    same_block = get_all(users, "block", block)
    same_block.sort(key = lambda c: c["flat"])
    
    same_flat = get_all(same_block, "flat", flat)
    same_flat.sort(key = lambda c: (c["flat"], c["room"]))
    
    return render_template(
        "display.html",
        same_flat = same_flat,
        same_block = same_block
    )