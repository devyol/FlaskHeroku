class Pokemon:

	#public Pokemon(parametros):{}
	def __init__(self,id,nombre,especie,tipo,foto):
		self.id = id
		self.nombre = nombre
		self.especie = especie
		self.tipo = tipo
		self.foto = foto

	def imprimir_tipo(self):
		print(self.nombre + ' es de tipo: ' + self.tipo);


	def dump(self):

		return {

			'id' : self.id,
			'nombre' : self.nombre,
			'especie' : self.especie,
			'tipo' : self.tipo,
			'foto' : self.foto
		}