import json
import requests
import traceback
from flask import make_response, jsonify, current_app, request
from flask_restful import Resource, reqparse
from flask_sieve import Validator

class Student(Resource):
    @classmethod
    def get(cls):
        return {'hello': 'world'}