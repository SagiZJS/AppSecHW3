import sqlite3

def get_conn():
    return sqlite3.connect("hw3.db",check_same_thread=False)

def init_db(c):
    c.execute("drop table if exists users;")
    c.execute("create table users (username varchar(45) not null, password varchar(45) not null, twofa varchar(45) not null, primary key(username));")

    c.execute("drop table if exists records;")
    c.execute("create table records (id integer primary key AUTOINCREMENT, username varchar(45) not null, query text, result text, foreign key(username) references users(username));")

    c.execute("drop table if exists logs;")
    c.execute("create table logs (username varchar(45), datetime varchar(60), action int, foreign key (username) references users(username));")
    
    insert_user(c,"admin","Administrator@1","12345678901")

    print("init",fetch_users(c))
    print("initialized")


def fetch_users(c):
    c.execute("select username from users")
    return c.fetchall()

def fetch_log(c,username):
    c.execute("select * from logs where username=?", (username,))
    return c.fetchall()

def insert_log(c,username, time, action):
    c.execute("insert into logs (username, datetime, action) values(?,?,?)",(username, time, action,))


def insert_record(c,username, query, result):
    c.execute("insert into records (username, query, result) values(?,?,?)", (username,query,result,))

def fetch_record(c,username):
    c.execute("select * from records where username = ? ", (username,))
    return c.fetchall()


def insert_user(c,username, password, tfa):
    c.execute("insert into users values(?,?,?)",(username,password,tfa))


def check_user(c,username):
    c.execute("select username from users where username=?;",(username,))
    return c.fetchall()
def fetch_user(c,username, password, tfa):
    c.execute("select username from users where username=? and password=? and twofa=?;",(username,password,tfa,))
    return c.fetchall()

    
