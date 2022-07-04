from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)

@app.route('/new_test', methods=['POST']) # for calling the API from Postman/SOAPUI
def new_test_function():
    if (request.method=='POST'):
        oper1=request.json['val0']
        val1=int(request.json['val1'])
        val2 = int(request.json['val2'])

        if(oper1=='add'):
            res =val1 + val2 + 5
            result= 'the sum of '+str(val1)+' and '+str(val2) +' is '+str(res)

        if (oper1== 'subtract'):
            res = val1 - val2 - 5
            result = 'the difference of ' + str(val1) + ' and ' + str(val2) + ' is ' + str(res)

        if (oper1 == 'multiply'):
            res = val1 * val2 * 5
            result = 'the product of ' + str(val1) + ' and ' + str(val2) + ' is ' + str(res)

        if (oper1 == 'divide'):
            r = val1 / val2
            result = 'the quotient when ' + str(val1) + ' is divided by ' + str(val2) + ' is ' + str(r)
        return jsonify(result)

@app.route('/new_test1', methods=['POST']) # for calling the API from Postman/SOAPUI
def new_test_function1():
    if (request.method=='POST'):
        name=request.json['name']
        email_id= request.json['email_id']
        phone_number = request.json['phone_number']
        result1 = name + " " + email_id + " " + str(phone_number)
        return jsonify(result1)

@app.route('/url_test1') # for calling the API from Postman/SOAPUI
def url_test_function1():
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')

    return '''<h1> my result is :  {}, {} </h1>'''.format(test1,test2)


@app.route('/url_test2') # for calling the API from Postman/SOAPUI
def url_test_function2():
    test1 = int(request.args.get('val1'))
    test2 = int(request.args.get('val2'))
    test3=  int(request.args.get('val3'))
    result = test1 * test2 + test3
    return '''<h1> my result is :  {}, {}, {}, {} </h1>'''.format(test1,test2, test3, result)




if __name__ == '__main__':
    app.run()
