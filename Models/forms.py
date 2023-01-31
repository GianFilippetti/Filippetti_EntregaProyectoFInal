from django import forms

class OurDogsForms (forms.Form):
    dog_name = forms.CharField (max_length=30, label = 'Nombre del perro' )
    dog_age = forms.IntegerField (label = 'Edad del perro')
    dog_history = forms.CharField (max_length=500, label = 'Historia del perro')
    dog_status = forms.BooleanField(required=False, label ='Estado del perro') 


class OurVolunteersForms (forms.Form):
    volunteer_name = forms.CharField (max_length=30, label ='Nombre del voluntario' )
    volunteer_age = forms.IntegerField (label = 'Edad del voluntario')
    volunteer_reason_to_be_a_volunteer = forms.CharField(max_length=500, label = 'Razon de ser voluntario' )
    volunteer_favourite_dog_and_reason = forms.CharField(max_length=500, label = 'Perro favorito y motivo' )


class OurCollaborativeInstitutionsForms (forms.Form):
    instituion_name = forms.CharField (max_length=30, label = 'Nombre de la institucíon' )
    institution_reason_to_colaborate = forms.CharField (max_length=500 , label = 'Razon por la que colabora' )
    institution_vision_of_animals = forms.CharField (max_length=500, label = 'Vision de los animales' )

class OthersProjectsForms (forms.Form):
    project_name = forms.CharField(max_length=30 , label = 'Nombre del proyecto')
    institution_or_person_in_charge = forms.CharField (max_length=30 ,label = 'Persona/institucíon a cargo' )
    project_objective = forms.CharField (max_length =500, label = 'Objetivo del proyecto' )




