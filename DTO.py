class usuario:
	idu=None
	nombre=None
	def __init__(self,idu,nom):
		self.nombre=nom
		self.idu=str(idu)

	def __str__(self):
		return  "id: "+self.idu+ " nombre: "+self.nombre

class lista:
	lid=None
	nombre=None
	id_user:None
	canciones=[]

	def __init__(self,lid,nom,idusr):
		self.lid=str(lid)
		self.nombre=nom
		self.id_user=str(idusr)

	def __str__(self):
		return 'id: '+str(self.lid)+' nombre: '+self.nombre+' canciones: '+str(self.canciones)+' id_user: '+self.id_user

class cancion:
	idc:None
	nombre=None
	archivo=None
	id_lista=None

	def __init__(self,idcc,nom,archivo,lista):
		self.nombre=nom
		self.idc=str(idcc)
		self.archivo=archivo
		self.id_lista=str(lista)

	def __str__(self):
		return 'id: '+self.idc+' nombre: '+self.nombre+' archivo: '+self.archivo+' id_lista: '+self.id_lista