from flask import Flask,request,jsonify
import day

app = Flask(__name__);

@app.get('/get')
def func():
    data = day.getall()
    json_list=[]
    for item in data:
        content = {}
        content = {'id':item[0],'name':item[1], 'department':item[2]}
        json_list.append(content)
    return(jsonify(json_list))

list=[]

@app.post("/postmethod")
def postfunc():
    data = request.get_json();
    print("--data--");
    day.Insert(data)
    return("Got Data");

@app.patch("/update")
def updatefun():
    data = request.get_json();
    print("--data--");
    day.update(data)
    return("Got Data");

@app.delete("/del/<id>")
def delfun(id):
    day.delete(id);
    return("Deleted")

if __name__=='__main__':
    app.run(debug=True, port=1001)

