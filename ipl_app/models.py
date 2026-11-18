from django.db import models
from pymongo import MongoClient

con=MongoClient("mongodb+srv://prathiksha383:prathiksha383@cluster0.khqiya2.mongodb.net/project?retryWrites=true&w=majority&appName=Cluster0")
coll=con["Prathi"]["data"]