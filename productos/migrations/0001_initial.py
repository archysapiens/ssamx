# Generated by Django 2.1.1 on 2020-02-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organismos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Edo', models.CharField(max_length=2)),
                ('Nombre', models.CharField(max_length=100)),
                ('Calle', models.CharField(max_length=100)),
                ('Numero_Ext', models.CharField(max_length=30)),
                ('Numero_Int', models.CharField(max_length=30)),
                ('Colonia', models.CharField(max_length=100)),
                ('Municipio', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=3)),
                ('CP', models.CharField(max_length=5)),
                ('Longitud', models.CharField(max_length=100)),
                ('Latitud', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Rol', models.CharField(max_length=2)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_email', models.CharField(max_length=100)),
                ('Nombre', models.CharField(max_length=100)),
                ('AppPaterno', models.CharField(max_length=100)),
                ('AppMaterno', models.CharField(max_length=100)),
                ('Sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=1)),
                ('Edad', models.CharField(max_length=2)),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='Fecha de Nacimiento')),
                ('Foto', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Tel_Oficina', models.CharField(max_length=20)),
                ('Extension', models.CharField(max_length=20)),
                ('Tel_Mobil', models.CharField(max_length=20)),
                ('Organismo', models.CharField(max_length=100)),
                ('Unidad_Responsable', models.CharField(max_length=3)),
                ('Credenciales', models.CharField(max_length=100)),
                ('Pregunta', models.CharField(max_length=100)),
                ('Respuesta', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=20)),
                ('Cargo', models.CharField(max_length=100)),
            ],
        ),
    ]
