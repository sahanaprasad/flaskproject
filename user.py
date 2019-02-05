from flask import Flask,render_template,request
import sqlite3 as sql

import os

app=Flask(__name__)

@app.route('/') #homepage 
def home():
	return render_template('friends.html')

@app.route('/adminback') #homepage 
def homeadmin():
	return render_template('admin.html')

@app.route('/logout') #homepage 
def logout():
	msg="Logged out sucessfully"
	return render_template('result2.html',msg=msg)
@app.route('/visitor') #homepage 
def visitor():
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from genrestable4')
	
	rows=cur.fetchall();
	return render_template('homepage.html',rows=rows)

@app.route('/loggeduser/<username>') #homepage 
def loggeduser(username):
	return render_template('aftersignin.html',username=username)

@app.route('/login') #homepage 
def login():
	return render_template('login.html')

@app.route('/userlogin/<username>') #homepage 
def userlogin(username):
	return render_template('aftersignin.html',username=username)

@app.route('/signin',methods=['POST','GET']) #homepage 
def signin():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		con=sql.connect('database.db')
		con.row_factory = sql.Row
	
		cur=con.cursor()
		cur.execute('select username,password from users1')
	
		rows=cur.fetchall();

		for row in rows:
			if(row["username"]==username and row["password"] ==password):
				return render_template('aftersignin.html',username=username)
		return render_template('login.html')

@app.route('/forgetpassword') #homepage 
def forgetpassword():
	return render_template('updatepassword.html')

@app.route('/updatepassword',methods=['POST','GET']) #homepage 
def updatepassword():
	if request.method=='POST':
		username=request.form['username']
		con=sql.connect('database.db')
		con.row_factory = sql.Row
	
		cur=con.cursor()
		cur.execute('select username from users1')
		rows=cur.fetchall();
		for row in rows:
			if(row["username"]==username):
				return render_template('upadateform.html',username=username)
		return render_template('updatepassword.html')

@app.route('/updatepassword2',methods=['POST','GET']) #homepage 
def updatepassword2():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		con=sql.connect('database.db')
		con.row_factory = sql.Row
	
		cur=con.cursor()
		cur.execute('Update users1 set password= ? where username= ? ',(password,username,))
		msg="Password sucessfully Updated"
		return render_template('updatesucessfull.html',msg=msg)
@app.route('/adminbackhome') #homepage 
def homeadminback():
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from genrestable4')
	
	rows=cur.fetchall();
	return render_template('list2.html',rows=rows)

@app.route('/homepage')       # for visitor show genere list
def homepage():
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from genrestable4')
	
	rows=cur.fetchall();
	return render_template('homepage.html',rows=rows)
	
	
@app.route('/newgenre')			# Add new genere
def new_genre():
	return render_template('genres.html')	
	
@app.route('/addshow',methods=['POST','GET'])   #On submit store it to the database	
def addshow():
	if request.method=='POST':
		#try:
			genre=request.form['genre']
			ID=request.form['ID']
			
			with sql.connect('database2.db')as con:
				cur=con.cursor()
				#cur.execute('INSERT INTO genres(genre) VALUES(?)',(genre))
				cur.execute('INSERT INTO genrestable4(ID,genre) VALUES(?,?)',(ID,genre))
				con.commit()
				msg="New genre added sucessfully"
		
			return render_template('result.html',msg = msg)
			con.close()

@app.route('/newshow')            #Add a new show 
def newshow():
	return render_template('shows.html')

@app.route('/showlistnow/<msg>')            #Add a new show 
def showlist(msg):
	if(msg=="Big_Bang_Theory"):
		return render_template('bbt.html')
	elif(msg=="Games_of_thrones"):
		return render_template('got.html')
	elif(msg=="Friends"):
		return render_template('friends2.html')
	elif(msg=="How_I_met_your_mother"):
		return render_template('himym.html')
	elif(msg=="13_Reasons_why"):
		return render_template('13reasons.html')
	elif(msg=="Lost"):
		return render_template('lost.html')
	elif(msg=="Breaking_Bad"):
		return render_template('bb.html')
	elif(msg=="Flash"):
		return render_template('flash.html')
	elif(msg=="Sherlock_Homes"):
		return render_template('sher.html')
	elif(msg=="Supernatural"):
		return render_template('supernatural.html')


@app.route('/addnewshow',methods=['POST','GET'])	# On submit store it the database
def addnewshow():
	if request.method=='POST':
		#try:
			gid=request.form['g_id']
			sid=request.form['s_id']
			sname=request.form['showname']
			rating=request.form['rating']
			suggestions=request.form['suggestions']
			
			with sql.connect('database2.db')as con:
				cur=con.cursor()
				#cur.execute('INSERT INTO genres(genre) VALUES(?)',(genre))
				cur.execute('INSERT INTO showlist2(g_id,s_id,sname,rating,suggestions) VALUES(?,?,?,?,?)',(gid,sid,sname,rating,suggestions))
				con.commit()
				msg="New show added sucessfully"
			return render_template('result.html',msg = msg)	
	
	
@app.route('/enternew')    # open new registration page
def new_student():
	return render_template('user.html')

@app.route('/addrec',methods=['POST','GET'])	# on submit store it to the databse
def addrec():
	if request.method=='POST':
		#try:
			username=request.form['username']
			email=request.form['email']
			first_name=request.form['first_name']
			last_name=request.form['last_name']
			dob=request.form['dob']
			pwd=request.form['pwd']
			activity=request.form['activity']
			
			with sql.connect('database.db')as con:
				cur=con.cursor()
				cur.execute('INSERT INTO users1(username,email,firstname,lastname,dob,password,activity) VALUES(?,?,?,?,?,?,?)',(username,email,first_name,last_name,dob,pwd,activity))

				
				con.commit()
				msg="User account created sucessfully"
		
			return render_template('result2.html',msg = msg)
			con.close()
	
@app.route('/newpage/<msg>')	# Show all the list of the show to the user without delete button
def new_page(msg):
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select * from showlist2 where g_id= ?',(msg,))
	
	rows=cur.fetchall();
	return render_template('newpage.html',rows=rows)

@app.route('/showlist/<msg>')   # Show all the list of the show to the user with delete button
def new_page2(msg):
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from showlist2 where g_id= ?',(msg,))
	
	rows=cur.fetchall();
	return render_template('newpage2.html',rows=rows)	
	

@app.route('/admin') #homepage login
def admin():
	return render_template('adminlogin.html')

@app.route('/adminlogin',methods=['GET','POST']) #homepage admin
def adminlogin():
	if request.method=='POST':
		password=request.form['password']
		if(password=='password'):
			return render_template('admin.html')
@app.route('/list')  # List all the generes to the admin
def listgenere():
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from genrestable4')
	
	rows=cur.fetchall();
	return render_template('list2.html',rows=rows)

@app.route('/listgenereuser/<msg>')  # List all the generes to the user
def listgenereuser(msg):
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select ID,genre from genrestable4')
	
	rows=cur.fetchall();
	return render_template('list3.html',rows=rows,msg1=msg)	

@app.route('/showlistuser/<msg>/<msg1>')   # Show all the list of the show to the user with delete button
def new_page3(msg,msg1):
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select s_id,sname from showlist2 where g_id= ?',(msg,))
	
	rows=cur.fetchall();
	return render_template('newpage3.html',rows=rows,msg1=msg1)	

@app.route('/rateshow/<msg>/<msg1>/<msg2>')  # List all the generes to the admin
def rateshow(msg,msg1,msg2):
	return render_template('rateshow.html',msg=msg,msg1=msg1,msg2=msg2)

@app.route('/rateshowsubmit/<msg1>',methods=['GET','POST'])
def rateshowsubmit(msg1):
	if request.method=='POST':

		sid=request.form['s_id']
		sname=request.form['sname']
		uname=request.form['uname']
		ratings=request.form['sratings']
		comments=request.form['comments']
			
		with sql.connect('database2.db')as con:
			cur=con.cursor()
			#cur.execute('INSERT INTO genres(genre) VALUES(?)',(genre))
			cur.execute('INSERT INTO usercomment3(sid,sname,uname,rating,comments) VALUES(?,?,?,?,?)',			(sid,sname,uname,ratings,comments))
			msg="Your Ratings has been recorded sucesfully !!"
			con.commit()
			
		return render_template('commentadded.html',msg = msg,msg1=msg1)	
	

@app.route('/deleteshow/<ID>')	# Delete the selected genere (for admin)

def deleteshow(ID):
	try:
		with sql.connect('database2.db')as con:
			cur=con.cursor()
			cur.execute('DELETE from genrestable4 where ID= ?',(ID,))
			con.commit()
			msg="Record sucessfully deleted sucessfully"

	finally:
			
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute('select * from genrestable4')
		rows=cur.fetchall();
		return render_template('list2.html',rows=rows)
		con.close()
@app.route('/deleteshowlist/<ID>/<ID2>')   # Delete the selected show (for admin)

def deleteshowlist(ID,ID2):
	try:
		with sql.connect('database2.db')as con:
			cur=con.cursor()
			cur.execute('DELETE from showlist2 where s_id= ? and g_id= ?',(ID,ID2,))
			con.commit()
			msg="record sucessfully deleted"

	finally:	
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute('select * from showlist2')
		rows=cur.fetchall();
		return render_template('newpage2.html',rows=rows)
		con.close()
@app.route('/deleteuser/<ID>')   # Delete the selected user (for admin)

def deleteuserlist(ID):
	try:
		with sql.connect('database.db')as con:
			cur=con.cursor()
			cur.execute('DELETE from users1 where username= ?',(ID,))
			con.commit()
			msg="record sucessfully deleted"

	finally:
			
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute('select * from users1')
		rows=cur.fetchall();
		return render_template('list.html',rows=rows)
		con.close()	
@app.route('/deletecomment/<ID>/<msg>')   # Delete the selected user (for admin)

def deletecomment(ID,msg):
	try:
		with sql.connect('database2.db')as con:
			cur=con.cursor()
			cur.execute('DELETE from usercomment3 where sname= ?',(ID,))
			con.commit()

	finally:
			
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute('select * from usercomment3')
		rows=cur.fetchall();
		return render_template('usercommenttableshow.html',rows=rows,msg=msg)
		con.close()		
						
@app.route('/userdetails')    # show all the user details

def list():	
	con=sql.connect('database.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from users1')
	
	rows=cur.fetchall();
	return render_template('list.html',rows=rows)		
	
@app.route('/listusercomments/<msg>')    # show all the user details
def listcomments(msg):	
	con=sql.connect('database2.db')
	con.row_factory = sql.Row
	
	cur=con.cursor()
	cur.execute('select *from usercomment3 where uname= ?',(msg,))
	
	rows=cur.fetchall();
	return render_template('usercommenttableshow.html',rows=rows,msg=msg)
@app.route('/got') #homepage 
def got():
	return render_template('got.html')
@app.route('/hiym') #homepage 
def friends():
	return render_template('himym.html')
@app.route('/sh') #homepage 
def sh():
	return render_template('sher.html')
@app.route('/thr') #homepage 
def thr():
	return render_template('13reasons.html')
@app.route('/bb') #homepage 
def bb():
	return render_template('bb.html')			
if __name__=='__main__':
	app.run(debug=True)
