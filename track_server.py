from flask import Flask,request,jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/api/v1.0/track_me/position/<lat>/<longi>/<timestamp>',methods=['GET','POST'])
def pos(lat,longi,timestamp):
	if request.method=='GET':
		conn = sql.connect('C:\\Users\\windows 7\\Desktop\\track_me.db')
		cur=conn.cursor();
		x=cur.execute("SELECT * FROM position ORDER BY id DESC LIMIT 1")
		for i in x:
			x=i
		conn.commit()
		return jsonify({'lat': x[1],'longi':x[2],'timestamp':x[3]})
	if request.method=='POST':
		conn = sql.connect('C:\\Users\\windows 7\\Desktop\\track_me.db')
		cur = conn.cursor()
		cur.execute("INSERT INTO POSITION (LAT,LONGI,TIMESTAMP)  VALUES (?,?,?)",(lat,longi,timestamp))
		conn.commit()
		return "Added to database"
		

	   
	    



if __name__ == '__main__':
    app.run(debug=True)

