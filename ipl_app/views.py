from django.shortcuts import render
from .models import *

def home(request):
    if request.method=="POST":
        data={
            "name":request.POST["Name"].capitalize(),
            "team":request.POST["Team"].upper(),
            "category":request.POST["Category"],
            "runs":int(request.POST["Runs"]),
            "balls":int(request.POST["Ba_wi"])
        }
        if data["category"]=="Batsman":
            data["sr"]=(data["runs"]/data["balls"])*100
        else:
            data["avg"]=data["runs"]/data["balls"]
        coll.insert_one(data)
    return render(request,"home.html")

def dashboard(request):
    val= list(coll.aggregate([
        {"$match": {"category": "Batsman"}},
        {"$group": {"_id": None,"totalRuns": {"$sum": "$runs"},"avgsr": {"$avg": "$sr"},} }]))

    val1= list(coll.aggregate([
        {"$match": {"category": "Bowler"}},
        {"$group": {"_id": None,"totalwicket": {"$sum": "$balls"},"avg": {"$avg": "$avg"},} }
        ]))
    
    bat=list(coll.find({"category":"Batsman"}))
    ball=list(coll.find({"category":"Bowler"}))
    top_bat=list(coll.find({"category":"Batsman"}).sort({"sr": -1 }).limit(3))
    top_ball=list(coll.find({"category":"Bowler"}).sort({"avg": 1 }).limit(3))
    return render(request,"dashboard.html",{"bat":bat,"ball":ball,"top_bat":top_bat,"top_ball":top_ball,"val":val[0],"val1":val1[0]})
