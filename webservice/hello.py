from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
from pivotpointsfiblist import fibRetracementList

app = Flask(__name__)

empDB = [
    {
        'id': '101',
        'name': 'Saravanan S',
        'title': 'Technical Leader'
    },
    {
        'id': '201',
        'name': 'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
]

# Get fib retracement
@app.route('/fib/h2l', methods=['GET'])
def getFibRetracementHighToLow():
    return fibRetracementList()


#Delete request
@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})

#Post request
@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)


# Put request for resource
@app.route('/empdb/employee/<empId>', methods=['PUT'])
def updateEmp(empId):
    empInDb = [emp for emp in empDB if (emp['id'] == empId)]
    print(empInDb[0]['name'])
    print(empInDb[0]['title'])
    if 'name' in request.json:
        empInDb[0]['name'] = request.json["name"]
    if 'title' in request.json:
        empInDb[0]['title'] = request.json["title"]
    return jsonify({'emp': empInDb[0]})


# Get request for specific resource
@app.route('/empdb/employee/<empId>', methods=['GET'])
def getEmp(empId):
    usr = [emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp': usr})


# Get request for all resource
@app.route('/empdb/employee', methods=['GET'])
def getAllEmp():
    return jsonify({'emps': empDB})


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
