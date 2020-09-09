import sqlite3

def billData():
    con=sqlite3.connect("billdb.sqlite")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bill(bno text,time text,cno text,name text,qua text,tot text)")
    con.commit()
    con.close()
def addB(bno,time,cno,name,qua,tot):
    con=sqlite3.connect("billdb.sqlite")
    cur=con.cursor()
    cur=con.execute("INSERT INTO bill VALUES(?,?,?,?,?,?)",(bno,time,cno,name,qua,tot))
    con.commit()
    con.close()
def delete(bno,name):
    con=sqlite3.connect("billdb.sqlite")
    cur=con.cursor()
    cur.execute("DELETE FROM bill WHERE bno=? AND name=?",(bno,name,))
    con.commit()
    con.close()
def modify(bno="",time="",cno="",name="",qua="",tot=""):
    con=sqlite3.connect("billdb.sqlite")
    cur=con.cursor()
    cur.execute("UPDATE product SET bno=?,time=?,cno=?,name=?,qua=?,tot=?",(bno,time,cno,name,qua,tot))
    con.commit()
    con.close()
billData()
    
    
