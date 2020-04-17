from django.db import models

class Usuario(models.Model):
	id_email = models.CharField(max_length=100)
	Nombre = models.CharField(max_length=100)
	AppPaterno = models.CharField(max_length=100)
	AppMaterno = models.CharField(max_length=100)
	GENERO=(('H', 'Hombre'),('M', 'Mujer'))
	Sexo =models.CharField(max_length=1, choices=GENERO, default='H')
	Edad=models.CharField(max_length=2)
	fecha_nacimiento = models.DateTimeField('Fecha de Nacimiento')
	Foto = models.ImageField(default='default.jpg', upload_to='profile_pics')
	Tel_Oficina = models.CharField(max_length=20)
	Extension = models.CharField(max_length=20)
	Tel_Mobil = models.CharField(max_length=20)
	Organismo=models.CharField(max_length=100)
	Unidad_Responsable=models.CharField(max_length=3)
	Credenciales=models.CharField(max_length=100)
	Pregunta=models.CharField(max_length=100)
	Respuesta=models.CharField(max_length=100)
	Password=models.CharField(max_length=20)
	Cargo=models.CharField(max_length=100)

	def NombreCompleto(self):
		cadena="{0} {1}, {2}"
		return cadena.format(self.AppPaterno, self.AppMaterno,self.Nombre)

	def __str__(self):
		return self.NombreCompleto()

class Organismos(models.Model):
	Id_Edo=models.CharField(max_length=2)
	Nombre = models.CharField(max_length=100)
	Calle = models.CharField(max_length=100)
	Numero_Ext = models.CharField(max_length=30)
	Numero_Int = models.CharField(max_length=30)
	Colonia = models.CharField(max_length=100)
	Municipio = models.CharField(max_length=100)
	Estado = models.CharField(max_length=3)
	CP = models.CharField(max_length=5)
	Longitud = models.CharField(max_length=100)
	Latitud = models.CharField(max_length=100)

	def NombreEstado(self):
		cadena="{0} {1}"
		return cadena.format(self.Id_Edo, self.Nombre)

	def __str__(self):
		return self.NombreEstado()

class Roles(models.Model):
	Id_Rol = models.CharField(max_length=2)
	Descripcion = models.CharField(max_length=100)

	def NombreRol(self):
		cadena="{0} {1}"
		return cadena.format(self.Id_Rol, self.Descripcion)

	def __str__(self):
		return self.NombreRol()

class Periodos(models.Model):
	anio = models.IntegerField(default=0)
	qna = models.CharField(max_length=2)
	fecha_envio = models.DateTimeField('Fecha de Quincena')
	descripcion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1)
	ART74_FED = (('A', 'ARTICULO 74'), ('F', 'FEDERAL'))
	art74_fed = models.CharField(max_length=1, choices=ART74_FED, default='A')

class Archivos(models.Model):
	id_archivo = models.IntegerField(default=0)
	desc_archivo = models.CharField(max_length=50)

class Remesas(models.Model):
	id_remesas = models.IntegerField(default=0)
	fecha_registro = models.DateTimeField('Fecha de Registro')
	fecha_validacion = models.DateTimeField('Fecha de Vañidacion')
	fecha_carga = models.DateTimeField('Fecha de carga')
	tipo_archivo = models.CharField(max_length=1)
	archivo = models.CharField(max_length=250)
	registros = models.IntegerField(default=0)
	observaciones = models.CharField(max_length=250)
	etiqueta_envio = models.CharField(max_length=30)
	archivo_error = models.CharField(max_length=250)
	registros_error = models.IntegerField(default=0)
	estatus = models.CharField(max_length=1)
	id_tipo_nom = models.CharField(max_length=2)
	fecha_agregacion = models.IntegerField(default=0)
	tabla_staging = models.CharField(max_length=50)
	tabla_ods = models.CharField(max_length=50)
	lista_urs = models.CharField(max_length=1024)
	art74_fed = models.CharField(max_length=1)















