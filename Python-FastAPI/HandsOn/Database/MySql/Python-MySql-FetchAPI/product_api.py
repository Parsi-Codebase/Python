from database import get_connection
from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get('/')
def home():
    return {'message':'Welcome to Product API'}
@app.post('/add')
def add(name:str,price:int,stock:int):
    conn=get_connection()
    cur=conn.cursor()
    qry='insert into products(name,price,stock) values(%s,%s,%s)'
    data=(name,price,stock)
    cur.execute(qry,data)
    conn.commit()
    cur.close()
    conn.close()
    return {'message':'Product Added Successfully'}
@app.get('/getproducts')
def getall():
 try:
     conn=get_connection()
     cur=conn.cursor()
     qry='Select * from Products'
     cur.execute(qry)
     result= cur.fetchall()
     cur.close()
     conn.close()
     return result
 except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get('/getbyId')
def getbyId(id:int):
 try:
     con=get_connection()
     cur=con.cursor()
     qry="Select * from products where id=%s"
     data=(id,)
     cur.execute(qry,data)
     result=cur.fetchone()
     cur.close()
     con.close()
     return result
 except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.delete("/delete")
def delete(id:int):
 try:
     conn=get_connection()
     cur=conn.cursor()
     qry='delete from products where id=%s'
     data=(id,)
     cur.execute(qry,data)
     conn.commit()
     cur.close()
     conn.close()
     return {'message':'Product Deleted Successfully'}
 except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.put("/edit")
def edit(id:int,price:int,stock:int):
    try:
     conn=get_connection()
     cur=conn.cursor()
     qry='update products set price=%s,stock=%s where id=%s'
     data=(price,stock,id)
     cur.execute(qry,data)
     conn.commit()
     cur.close()
     conn.close()
     return {'message':'Product Edited Successfully'}
    except Exception as e:
     raise HTTPException(status_code=500, detail=str(e))
    
     
    
    