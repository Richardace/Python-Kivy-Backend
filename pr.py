from DTO import *
from DAO import *
from conexion import Conexion

def prdao():
	u = usuarioDAO()
	us1= u.select('pepe')
	print(str(us1))

	us2= u.select('asa')
	print(str(us2))

	l = listaDAO()
	ls1 = l.select(str(us1[0][0]))
	print(str(ls1))

	ls2 = l.select("")
	print(str(ls2))

	c = cancionDAO()
	cs1 = c.select(str(ls1[0][0]))
	print(str(cs1))

	cs2 = c.select(str(ls2[0][0]))
	print(str(cs2))

def prdao2():
	u = usuarioDAO()
	us1= u.select('pepe')
	print(str(us1))

	l = listaDAO()
	ls1 = l.select(us1.idu)
	print(str(ls1))

	c = cancionDAO()
	cs1 = c.select(ls1.lid)
	print(str(cs1[0]))	

def prdao3():
    u = usuarioDAO()
    us1= u.select('ddddfdgf')
    if(us1):
    	print('existe')
    else:
    	print('no existe')
    print(u.insert('aze'))

prdao3()