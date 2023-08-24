# USAGE:
# pytest -v --no-header | tee tests/results.txt

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from forms import (
    AddUser,
    FindUsers,
)

import re
def extract_csrf_token(content):
    match = re.search(
        r'<input[^>]*name="csrf_token"[^>]*value="([^"]+)"', 
        content)
    if match:
        return match.group(1)
    return None

def test_AddUser_empty():
    '''
    Test an empty AddCourse form
    Expect the form to fail validation
    '''
    with app.test_request_context("/add"):
        form = AddUser()
        assert not form.validate()
        assert form.errors
        
def test_AddUser_all_fields_valid():
    with app.test_request_context('/add'):
        with app.test_client() as client:
            response = client.get('/add')
            csrf_token = extract_csrf_token(response.data.decode("utf-8"))

            form = AddUser(
                name = "Test Name",
                course = "Test Course",
                ig = "test_ig",
                sc = "test_sc",
                hall = "Radnor",
                block = "0",
                flat = 1,
                room = 1,
                csrf_token = csrf_token
            )
            assert form.validate()
            assert not form.errors
            
def test_AddUser_no_optnl_fields():
    with app.test_request_context('/add'):
        with app.test_client() as client:
            response = client.get('/add')
            csrf_token = extract_csrf_token(response.data.decode("utf-8"))

            form = AddUser(
                name = "Test Name",
                course = "Test Course",
                hall = "Radnor",
                block = "0",
                flat = 1,
                room = 1,
                csrf_token = csrf_token
            )
            assert form.validate()
            assert not form.errors
            
def test_AddUser_hall_invalid():
    with app.test_request_context('/add'):
        with app.test_client() as client:
            response = client.get('/add')
            csrf_token = extract_csrf_token(response.data.decode("utf-8"))

            form = AddUser(
                name = "Test Name",
                course = "Test Course",
                ig = "test_ig",
                sc = "test_sc",
                hall = "Not a real hall",
                block = "0",
                flat = 1,
                room = 1,
                csrf_token = csrf_token
            )
            assert not form.validate()
            assert form.errors
            
def test_FindUsers_empty():
    '''
    Test an empty FindUsers form
    Expect the form to fail validation
    '''
    with app.test_request_context("/find"):
        form = FindUsers()
        assert not form.validate()
        assert form.errors
        
def test_FindUsers_all_fields_valid():
    with app.test_request_context('/find'):
        with app.test_client() as client:
            response = client.get('/find')
            csrf_token = extract_csrf_token(response.data.decode("utf-8"))

            form = FindUsers(
                hall = "Radnor",
                block = "0",
                flat = 1,
                csrf_token = csrf_token
            )
            assert form.validate()
            assert not form.errors
            
def test_FindUsers_hall_invalid():
    with app.test_request_context('/find'):
        with app.test_client() as client:
            response = client.get('/find')
            csrf_token = extract_csrf_token(response.data.decode("utf-8"))

            form = FindUsers(
                hall = "Not a real hall",
                block = "0",
                flat = 1,
                csrf_token = csrf_token
            )
            assert not form.validate()
            assert form.errors