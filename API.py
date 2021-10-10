from flask import Flask, Response, request
import pymongo
import json
import os 

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host = "localhost",     # if you want to connect pymongo to another host then can change this line
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.company      # Database name is company
    mongo.server_info()
except:
    print('Cannot connect to DB')
    Response(
        response = json.dumps({"message":"cannot connect"}),
        status = 500,
        mimetype = "application/json"
    )

@app.route('/',methods=['GET','POST'])
def main_page():
    try:
        if request.method=='POST': # if user clicked sign-up then 'POST' method
            return Response(
                response = json.dumps(
                    {"message":"Go to add-user",
                    "link for redirect":"localhost:/add-user"}
                ),
                status = 200,
                mimetype = "application/json"
            )
        elif request.method=='GET': # if user clicked login then 'GET' method
            return Response(
                response = json.dumps(
                    {"message":"Go to Login",
                    "link for redirect":"localhost:/login"}
                ),
                status = 200,
                mimetype = "application/json"
            )
    except Exception:
        print('Cannot connect to DB')
        Response(
            response = json.dumps({"message":"cannot connect",
                                    "Exception":f"{Exception}"}),
            status = 500,
            mimetype = "application/json"
        )


@app.route('/login',methods = ['GET'])
def login():
    try:    # here users is collection in company database
        for x in db.users.find({"email":request.form['email'],"pass":request.form['pass']}): # to find user in database
            return Response(
                response = json.dumps({"message":"Login success, User identified",
                                        "user":f"{x}",
                                        "link for redirect":"localhost:/index"}),
                status = 200,
                mimetype = "application/json"
            )
    except Exception:
        return Response(
            response = json.dumps({"message":"Error in login cannot find user"}),
            status = 500,
            mimetype = "application/json"
        )

@app.route('/add-user',methods = ['POST'])
def add_user():
    try:
        email = request.form['email']
        passwd = request.form['pass']

        db.users.insert_one({"email":email,"pass":passwd})  # insert 1 document of userdata

        return Response(
            response = json.dumps({"message":"user added, Go back to login",
                                    "Link to login":"localhost:/login"}),
            status = 200,
            mimetype = "application/json"
        )
    except Exception:
        print(Exception)
        return Response(
            response = json.dumps({"message":"Sorry there is some error"}),
            status = 500,
            mimetype = "application/json"
        )

@app.route('/index',methods=['GET'])
def index():
    try:
        return Response(
            response=json.dumps({"message":"Index page",
                                "api for hospital availability":"localhost/availability"}),
            status=200,
            mimetype="application/json"
        )
    except Exception:
        return Response(
            response = json.dumps({"message":"Sorry there is some error in Index Page"}),
            status = 500,
            mimetype = "application/json"
        )

@app.route('/availability',methods=['GET'])
def show_details():
    try:
        file=os.path.join("","Data.json")   
        with open(file) as data:
            res=json.load(data)     # reads data from file Data.json
        return Response(
            response=json.dumps(res),
            status=200,
            mimetype="application/json"
        )
    except:
        return Response(
            response=json.dumps({"message":"Can't show details"}),
            status=500,
            mimetype="application/json"
        )

@app.route('/availability/search',methods=['GET'])
def search():
    try:
        file=os.path.join("","Data.json")
        with open(file) as data:
          res=json.load(data)   # reads data from Data.json

        l=list(filter(lambda x:x['STATE']==request.form['state'] and x['DISTRICT']==request.form['dist'],res))
        # l is a list of results that are found from filtering Data.json
        return Response(
            response=json.dumps(l),
            status=200,
            mimetype='application/json'
        )
    except:
        return Response(
            response=json.dumps({"message":"Error in searching results"}),
            status=500,
            mimetype="application/json"
        )

if __name__ == '__main__':
    app.run(debug=True,port=80) # runs on port 80 to send response on postman