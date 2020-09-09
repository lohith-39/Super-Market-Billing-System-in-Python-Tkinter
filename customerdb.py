import sqlite3

def customerData():
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY,Cid text,Cname text,Phno text)")
    con.commit()
    con.close()
def addCustomer(Cid,Cname,Phno):
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur=con.execute("INSERT INTO customer VALUES(NULL,?,?,?)",(Cid,Cname,Phno))
    con.commit()
    con.close()
def viewData():
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur.execute("SELECT * FROM customer")
    rows=cur.fetchall()
    con.close()
    return rows
def delete(id):
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur.execute("DELETE FROM customer WHERE id=?",(id,))
    con.commit()
    con.close()
def search(Cid="",Cname="",Phno=""):
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur.execute("SELECT * FROM customer WHERE Cid=? OR Cname=? OR Phno=?",(Cid,Cname,Phno))
    rows=cur.fetchall()
    con.close()
    return rows
def modify(id,Cid="",Cname="",Phno=""):
    con=sqlite3.connect("customerdb.sqlite")
    cur=con.cursor()
    cur.execute("UPDATE customer SET Cid=?,Cname=?,Phno=?",(Cid,Cname,Phno))
    con.commit()
    con.close()
        
    
customerData()
