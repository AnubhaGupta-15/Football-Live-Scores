# imports
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import request
from flask import Flask
from flask import render_template
import requests
import mysql.connector
from mysql.connector.constants import ClientFlag
from flask import session
import regex

# initializes the app (__name__ = the file name)
app = Flask(__name__)

# session key for sessions
app.secret_key = 'sessionkey'

# database configuration
config = {
    'user': 'root',
    'password': 'hello123',
    'host': '34.89.109.27',
    'database': 'footballdb'
}

# index page initialization
@app.route('/')
def index():
    return render_template("index.html")

# login page init
@app.route('/LoginNew')
def loginNew():
    return render_template("loginnew.html")

# logout page init
@app.route('/logout')
def logout():
    # remove session instances
    session.pop("userid", None)
    session.pop("teamid", None)
    return render_template("loginnew.html")

# Registration page init
@app.route('/Registration')
def Registration():
    return render_template("registration.html")

# Get User Settings method
@app.route('/Settings')
def UserSettings():
    # grab sessions and place in id
    userid = session['userid'][0]
    teamid = session['teamid'][0]

    # init db con
    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    # Read user data from user id
    cursor.execute("SELECT Name FROM Users WHERE userid = %s", ([userid]))
    name = cursor.fetchone()

    cursor.execute("SELECT password FROM Users WHERE userid = %s", ([userid]))
    password = cursor.fetchone()

    cursor.execute("SELECT email FROM Users WHERE userid = %s", ([userid]))
    email = cursor.fetchone()

    # return UserSettings page with equivalent data
    return render_template("UserSettings.html", userid = userid, name = name[0], email = email[0], password = password[0])

# standings page init which uses live.html which contains widget external api code
@app.route('/standings')
def standings():
    return render_template('live.html')

# display teams method that gets users team fixures based on team api
@app.route('/displayTeams', methods=['GET','POST'])
def displayTeams():
    teamid = session['teamid'][0]
    return render_template('fixture.html', value = teamid)


# update user method
@app.route('/updateUser', methods=['GET','POST'])
def updateUser():
    # get user input
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']

    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    # Update function 
    cursor.execute("UPDATE Users SET Name=%s, password=%s, email=%s WHERE UserId=%s", (name, password, email, session['userid'][0]))
    con.commit()  # and commit changes

    return redirect(url_for('UserSettings'))

# Delete user method
@app.route('/deleteUser', methods=['GET','POST'])
def deleteUser():
    # get session user id
    userid = session['userid'][0]
    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    # delete from Users table and delete their fav team our the favouriteTeam table
    cursor.execute("DELETE FROM Users WHERE UserId=%s", ([userid]))
    con.commit()  # and commit changes

    cursor.execute("DELETE FROM FavouriteTeam WHERE UserId=%s", ([userid]))
    con.commit()  # and commit changes

    # pop their sessions as they no longer exist
    session.pop("userid", None)
    session.pop("teamid", None)
    return redirect(url_for('Registration'))

# Register method
@app.route('/register', methods=['POST'])
def register():
    # get user information
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    teamID = request.form['favouriteTeam']
    con = mysql.connector.connect(**config)
    cursor = con.cursor()
    
    # insert into Users table 
    cursor.execute("INSERT INTO Users (name, password, email) VALUES (%s, %s, %s)", (name, password, email))
    con.commit()  # and commit changes

    # get particular UserId from the just created User
    cursor.execute("SELECT UserId FROM Users WHERE email = %s", ([email]))
    out = cursor.fetchall()

    # Loop through the data
    grabTeams = ""
    for row in out:
        # insert into favourite team table
         cursor = con.cursor()
         cursor.execute("INSERT INTO FavouriteTeam (userID, teamID) VALUES (%s, %s)", (row[0], teamID))
         con.commit()  # and commit changes

        # get our favourite team data if we ever need to use
         cursor = con.cursor()
         cursor.execute("SELECT * FROM FavouriteTeam WHERE userId = %s", ([row[0]]))
         grabTeams = cursor.fetchone()

    id ,user, team = grabTeams
    return redirect(url_for('loginNew'))

# User login method 
@app.route('/userlogin', methods=['POST'])
def userlogin():
    # request form from email and password
    email = request.form['email']
    password = request.form['password']

    # check if user exists here
    con = mysql.connector.connect(**config)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Users WHERE email = %s AND password = %s", (email, password))
    out = cursor.fetchall()

    # if doesn't exist then return failed response message
    if len(out) == 0:
        return render_template("loginnew.html", errorMessage = "Invalid Credentials")
    else:
        # set user and team sessions on successful login  
        cursor.execute("SELECT UserId FROM Users WHERE email = %s", ([email]))
        out = cursor.fetchone()
        userid = out

        session['userid'] = userid

        cursor.execute("SELECT TeamId FROM FavouriteTeam WHERE UserId = %s", (session['userid']))
        out2 = cursor.fetchone()
        teamid = out2

        session['teamid'] = teamid
        return redirect(url_for('UserSettings'))

if __name__ == '__main__':
    app.run(debug = True)