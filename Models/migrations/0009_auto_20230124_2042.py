# Generated by Django 3.2.16 on 2023-01-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0008_rename_edad_del_perro_ourdogs_dog_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='othersprojects',
            options={'verbose_name': 'Otro proyecto', 'verbose_name_plural': 'Otros proyectos'},
        ),
        migrations.AlterModelOptions(
            name='ourcollaborativeinstitutions',
            options={'verbose_name': 'Institucion colaborativa', 'verbose_name_plural': 'Instituciones colaborativas'},
        ),
        migrations.AlterModelOptions(
            name='ourdogs',
            options={'verbose_name': 'Perro', 'verbose_name_plural': 'Perros'},
        ),
        migrations.AlterModelOptions(
            name='ourvolunteers',
            options={'verbose_name': 'Voluntario', 'verbose_name_plural': 'Voluntarios'},
        ),
        migrations.AlterField(
            model_name='othersprojects',
            name='institution_or_person_in_charge',
            field=models.CharField(max_length=30, verbose_name='Persona/institucion a cargo'),
        ),
        migrations.AlterField(
            model_name='othersprojects',
            name='project_name',
            field=models.CharField(max_length=30, verbose_name='Nombre del proyecto'),
        ),
        migrations.AlterField(
            model_name='othersprojects',
            name='project_objective',
            field=models.CharField(max_length=500, verbose_name='Objetivo del proyecto'),
        ),
        migrations.AlterField(
            model_name='ourcollaborativeinstitutions',
            name='instituion_name',
            field=models.CharField(max_length=30, verbose_name='Nombre de la institucion'),
        ),
        migrations.AlterField(
            model_name='ourcollaborativeinstitutions',
            name='institution_reason_to_colaborate',
            field=models.CharField(max_length=500, verbose_name='Razon por la que colabora'),
        ),
        migrations.AlterField(
            model_name='ourcollaborativeinstitutions',
            name='institution_vision_of_animals',
            field=models.CharField(max_length=500, verbose_name='Vision de los animales'),
        ),
        migrations.AlterField(
            model_name='ourdogs',
            name='dog_age',
            field=models.IntegerField(verbose_name='Edad del perro'),
        ),
        migrations.AlterField(
            model_name='ourdogs',
            name='dog_history',
            field=models.CharField(max_length=500, verbose_name='Historia del perro'),
        ),
        migrations.AlterField(
            model_name='ourdogs',
            name='dog_name',
            field=models.CharField(max_length=30, verbose_name='Nombre del perro'),
        ),
        migrations.AlterField(
            model_name='ourdogs',
            name='dog_status',
            field=models.BooleanField(default=True, verbose_name='¿Adoptado?'),
        ),
        migrations.AlterField(
            model_name='ourvolunteers',
            name='volunteer_age',
            field=models.IntegerField(verbose_name='Edad del voluntario'),
        ),
        migrations.AlterField(
            model_name='ourvolunteers',
            name='volunteer_favourite_dog_and_reason',
            field=models.CharField(max_length=500, verbose_name='Perro favorito y motivo'),
        ),
        migrations.AlterField(
            model_name='ourvolunteers',
            name='volunteer_name',
            field=models.CharField(max_length=30, verbose_name='Nombre del voluntario'),
        ),
        migrations.AlterField(
            model_name='ourvolunteers',
            name='volunteer_reason_to_be_a_volunteer',
            field=models.CharField(max_length=500, verbose_name='Razon por la que colabora'),
        ),
    ]