from flask import Flask , render_template
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://admin:GKQW0AUOfXHA8AoI@cluster0.qireg.mongodb.net/sms?retryWrites=true&w=majority")
db = client['sms']
col = db['detector']

@app.route("/")
def table():
    stress_list = []
    x = col.find().sort("_id",pymongo.DESCENDING).limit(20)
    for i in x:
        new_list = []
        new_list.append(i['Stress Value'])
        new_list.append(i['Date and Time'])
        stress_list.append(new_list)

   
    return render_template('table.html',data = stress_list)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000)
