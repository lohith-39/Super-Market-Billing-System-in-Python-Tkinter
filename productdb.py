import sqlite3

def productData():
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY,Pid text,Pname text,Price text,Dis text)")
    con.commit()
    con.close()
def addProduct(Pid,Pname,Price,Dis):
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur=con.execute("INSERT INTO product VALUES(NULL,?,?,?,?)",(Pid,Pname,Price,Dis))
    con.commit()
    con.close()
def viewData():
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur.execute("SELECT * FROM product")
    rows=cur.fetchall()
    con.close()
    return rows
def delete(id):
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur.execute("DELETE FROM product WHERE id=?",(id,))
    con.commit()
    con.close()
def search(Pid="",Pname="",Price="",Dis=""):
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur.execute("SELECT * FROM product WHERE Pid=? OR Pname=? OR Price=? OR Dis=?",(Pid,Pname,Price,Dis))
    rows=cur.fetchall()
    con.close()
    return rows
def modify(id,Pid="",Pname="",Price="",Dis=""):
    con=sqlite3.connect("productdb.sqlite")
    cur=con.cursor()
    cur.execute("UPDATE product SET Pid=?,Pname=?,Price=?,Dis=?",(Pid,Pname,Price,Dis))
    con.commit()
    con.close()
        
    
productData()
