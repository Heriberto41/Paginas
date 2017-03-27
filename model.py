import web, datetime

db_host='am1shyeyqbxzy8gc.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name='jem52cv0hn307cd3'
db_user='k32fygihhm3c7rtr'
db_pw='tywi4bftys2ma080'

db=web.database(
  dbn='mysql',
  host=db_host,
  db=db_name,
  user=db_user,
  pw=db_pw
	)

def get_posts():
    return db.select('productoss', order='id_producto ASC')

def get_post(id_producto):
    try:
        return db.select('productoss', where='id_producto=$id_producto', vars=locals())[0]
    except:
        return None

def new_post(producto, varchar, existencias, precio_compra, precio_venta, imagen_producto):
    db.insert('productoss', producto=producto, descripcion=varchar, existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto, posted_on=datetime.datetime.utcnow())

def del_post(id_producto):
    db.delete('productoss', where="id_producto=$id_producto", vars=locals())

def update_post(id_producto, producto, varchar, existencias, precio_compra, precio_venta, imagen_producto):
    db.update('productoss', where="id_producto=$id_producto", vars=locals(),
        producto=producto, descripcion=varchar,  existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto, posted_on=datetime.datetime.utcnow())
