from django.db import models

# Create your models here.
class OurDogs (models.Model):
    dog_name = models.CharField (max_length=30 , verbose_name='Nombre del perro')
    dog_age = models.IntegerField (verbose_name= 'Edad del perro')
    dog_history = models.CharField (max_length=500 , verbose_name='Historia del perro' )
    dog_status = models.BooleanField(default=True , verbose_name='¿Adoptado?' )

    def __str__(self):
        return self.dog_name
    class Meta:
        verbose_name = 'Perro'
        verbose_name_plural = 'Perros'

class OurVolunteers (models.Model):
    volunteer_name = models.CharField (max_length=30, verbose_name='Nombre del voluntario')
    volunteer_age = models.IntegerField (verbose_name='Edad del voluntario')
    volunteer_reason_to_be_a_volunteer = models.CharField(max_length=500 , verbose_name='Razon por la que colabora')
    volunteer_favourite_dog_and_reason = models.CharField(max_length=500, verbose_name='Perro favorito y motivo')

    def __str__(self):
        return self.volunteer_name
    class Meta:
        verbose_name = 'Voluntario'
        verbose_name_plural = 'Voluntarios'

class OurCollaborativeInstitutions (models.Model):
    instituion_name = models.CharField (max_length=30, verbose_name='Nombre de la institucion')
    institution_reason_to_colaborate = models.CharField (max_length =500 , verbose_name='Razon por la que colabora')
    institution_vision_of_animals = models.CharField (max_length=500 , verbose_name='Vision de los animales')

    def __str__(self):
        return self.instituion_name
    class Meta:
        verbose_name = 'Institucion colaborativa'
        verbose_name_plural = 'Instituciones colaborativas'

class OthersProjects (models.Model):
    project_name = models.CharField(max_length=30 , verbose_name='Nombre del proyecto')
    institution_or_person_in_charge = models.CharField (max_length=30, verbose_name='Persona/institucion a cargo')
    project_objective =models.CharField (max_length =500, verbose_name='Objetivo del proyecto')

    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = 'Otro proyecto'
        verbose_name_plural = 'Otros proyectos'
