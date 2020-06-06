from DTO import *
from conexion import Conexion


class usuarioDAO:
	def insert(self , nombre):
		con = Conexion()
		sql = "INSERT INTO usuarios (id, nombre) VALUES (null,%s)"
		val=(nombre,)

		print(sql +nombre)
		return con.insert(sql,val)
	
	def select(self,nombre ):
		con = Conexion()
		sql = "SELECT * FROM usuarios where usuarios.nombre ='"+nombre+"'"
		#print(sql)
		val= con.select(sql)
		if val:
			return usuario(val[0][0],val[0][1])
		else:
			return False
			
class listaDAO:

	def select(self,iduss ):
		con = Conexion()
		sql = "SELECT * FROM lista WHERE lista.usuario_id = "+iduss
		val = con.select(sql)
		return lista(val[0][0],val[0][1],val[0][2])

class cancionDAO:

	def insert(self , nombre , archivo , lista):
		con = Conexion()
		sql = "INSERT INTO `cancion` (`id`, `nombre`, `archivo`, `lista_id`) VALUES (NULL, '%s', '%s', '%s')"
		val = (nombre, archivo,lista)

		return con.insert(sql,val)

	def select(self,idl ):
		con = Conexion()
		sql = "SELECT * FROM cancion WHERE lista_id="+idl
		val = con.select(sql)
		resul=[]

		for x in val:
			resul.append(cancion(x[0],x[1],x[2],x[3]))

		return resul
		


