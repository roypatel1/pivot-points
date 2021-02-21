from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
from pivotpointsfiblist import fibRetracementListL2H, fibRetracementListH2L, pivotPointsLowAndHigh, cluster1L2H

app = Flask(__name__)

# Get fib retracement high to low
@app.route('/fib/h2l', methods=['GET'])
def get_fib_retracement_high_to_low():
    stock = request.args.get('sym')
    start = request.args.get('start')
    end = request.args.get('end')
    candles = int(request.args.get('candles'))
    return fibRetracementListH2L(stock, start, end, candles)


# Get fib retracement low to high
@app.route('/fib/l2h', methods=['GET'])
def get_fib_retracement_low_to_high():
    stock = request.args.get('sym')
    start = request.args.get('start')
    end = request.args.get('end')
    candles = int(request.args.get('candles'))
    return fibRetracementListL2H(stock, start, end, candles)


# Get pivot points
@app.route('/pivotpoints', methods=['GET'])
def get_pivot_points():
    stock = request.args.get('sym')
    start = request.args.get('start')
    end = request.args.get('end')
    candles = int(request.args.get('candles'))
    return pivotPointsLowAndHigh(stock, start, end, candles)


# Get cluster l2h points
@app.route('/clusterl2h', methods=['GET'])
def get_cluster_l2h():
    stock = request.args.get('sym')
    start = request.args.get('start')
    end = request.args.get('end')
    candles = int(request.args.get('candles'))
    return cluster1L2H(stock, start, end, candles)


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
def updateemp(emp_id):
    emp_in_db = [emp for emp in empDB if (emp['id'] == emp_id)]
    print(emp_in_db[0]['name'])
    print(emp_in_db[0]['title'])
    if 'name' in request.json:
        emp_in_db[0]['name'] = request.json["name"]
    if 'title' in request.json:
        emp_in_db[0]['title'] = request.json["title"]
    return jsonify({'emp': emp_in_db[0]})


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
