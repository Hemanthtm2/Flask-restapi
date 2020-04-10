from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello this is my first Flask app"

@app.route('/hithere')

def hi_there():
    return "I just hit /hithere"


@app.route('/add_two_nums', methods=["POST"])


def add_two_nums():

    dataDict=request.get_json()
   # return jsonify(dataDict)

    if "y" not in dataDict:
       return "ERROR",305
       
    x=dataDict["x"]
    y=dataDict["y"]

    z=x+y

    retJson={

            "z":z

            }
    return jsonify(retJson),200







@app.route('/bye')

def bye():

    age=10*3

    retJson = {

         'Name' : 'Hemanth',
         'Age' : age,
         "Phones" : [
               {
                 "phoneName" : "IphoneX",
                 
                 "phoneNum" : 9901361262

               },
               
               {

                 "phoneName" : "Google Pixel",
                 
                 "phoneNum" : 8075248443

               }

           

                 ]

        }
    
    return jsonify(retJson)



if __name__=="__main__":
   app.run(Debug=True,host="192.168.56.107",port=80)
