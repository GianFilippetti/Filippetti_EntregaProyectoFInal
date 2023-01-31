from django.shortcuts import render
from Models.models import OurDogs , OurVolunteers ,OurCollaborativeInstitutions  , OthersProjects
from Models.forms import OurDogsForms , OurVolunteersForms , OurCollaborativeInstitutionsForms , OthersProjectsForms
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Mas adelante voy a probar las otras clases
# Create your views here.
@login_required
def create_our_dogs (request):

    if request.method == 'GET':
        context = {
            'dog_form' : OurDogsForms ()
        }
        return render (request , 'our_dogs/create_our_dogs.html' , context = context)
    elif request.method == 'POST':
        dog_form =OurDogsForms (request.POST)
        if dog_form.is_valid ():
            OurDogs.objects.create (
                dog_name = dog_form.cleaned_data ['dog_name'],
                dog_age = dog_form.cleaned_data ['dog_age'],
                dog_history= dog_form.cleaned_data ['dog_history'],
                dog_status = dog_form.cleaned_data ['dog_status'],
            )
            context = {
                'message' : 'Se agrego el nuevo perro'
            }
            return render ( request , 'our_dogs/create_our_dogs.html' , context = context)
        else:
            context = {
                'dog_form_errors': dog_form.errors ,
                'dog_form' : OurDogsForms ()
            }
            return render ( request , 'our_dogs/create_our_dogs.html' , context = context)
@login_required
def create_our_volunteers (request):
    if request.method == 'GET':
        context = {
            'volunteer_form' :OurVolunteersForms()
        }
        return render (request , 'our_volunteers/create_our_volunteer.html' , context = context)
    elif request.method == 'POST':
        volunteer_form = OurVolunteersForms(request.POST)
        if volunteer_form.is_valid ():
            OurVolunteers.objects.create (
                volunteer_name = volunteer_form.cleaned_data ['volunteer_name'],
                volunteer_age = volunteer_form.cleaned_data ['volunteer_age'],
                volunteer_reason_to_be_a_volunteer = volunteer_form.cleaned_data ['volunteer_reason_to_be_a_volunteer'],
                volunteer_favourite_dog_and_reason = volunteer_form.cleaned_data ['volunteer_favourite_dog_and_reason'],
            )
            context = {
                'message' : 'Se agrego el nuevo voluntario'
            }
            return render ( request , 'our_volunteers/create_our_volunteer.html' , context = context)
        else:
            context = {
                'volunteer_form_errors': volunteer_form.errors ,
                'volunteer_form' : OurVolunteersForms ()
            }
            return render ( request , 'our_volunteers/create_our_volunteer.html' , context = context)
@login_required
def create_our_collaborative_institutions (request):
    if request.method == 'GET':
        context = {
            'colaborative_institution_form' :OurCollaborativeInstitutionsForms ()
        }
        return render (request , 'our_colaborative_institutions/create_our_colaborative_institution.html' , context = context)
    elif request.method == 'POST':
        colaborative_institution_form = OurCollaborativeInstitutionsForms (request.POST)
        if colaborative_institution_form.is_valid ():
            OurCollaborativeInstitutions .objects.create (
                instituion_name = colaborative_institution_form.cleaned_data ['instituion_name'],
                institution_reason_to_colaborate = colaborative_institution_form.cleaned_data ['institution_reason_to_colaborate'],
                institution_vision_of_animals= colaborative_institution_form.cleaned_data ['institution_vision_of_animals'],
            )
            context = {
                'message' : 'Se agrego la nueva institucion colaborativa'
            }
            return render ( request , 'our_colaborative_institutions/create_our_colaborative_institution.html' , context = context)
    else:
            context = {
                'colaborative_institution_errors': colaborative_institution_form.errors ,
                'colaborative_institution_form' : OurCollaborativeInstitutionsForms ()
            }
            return render ( request , 'our_colaborative_institution.html', context = context)
@login_required
def create_others_projects (request):
    if request.method == 'GET':
        context = {
            'others_projects_form' : OthersProjectsForms ()
        }
        return render (request , 'others_projects/create_others_projects.html' , context = context)
    elif request.method == 'POST':
        others_projects_form = OthersProjectsForms (request.POST)
        if others_projects_form.is_valid ():
            OthersProjects.objects.create (
                project_name = others_projects_form.cleaned_data ['project_name'],
                institution_or_person_in_charge = others_projects_form.cleaned_data ['institution_or_person_in_charge'],
                project_objective= others_projects_form.cleaned_data ['project_objective'],
            )
            context = {
                'message' : 'Se agrego el nuevo proyecto'
            }
            return render ( request , 'others_projects/create_others_projects.html' , context = context)
        else:
            context = {
                'others_projects_form_errors': others_projects_form.errors ,
                'others_projects_form'  : OthersProjectsForms ()
            }
            return render ( request , 'others_projects/create_others_projects.html' , context = context)
@login_required
def list_our_dogs (request):
    if 'search' in request.GET:
        search = request.GET ['search']
        all_dogs = OurDogs.objects.filter(dog_name__icontains = search)
    else:
        all_dogs = OurDogs.objects.all 
    context = {
        'our_dogs': all_dogs
    }
    return render (request ,'our_dogs/list_our_dogs.html', context = context )
@login_required
def list_our_volunteers (request):
    if 'search' in request.GET:
        search = request.GET [search]
        all_volunteers = OurVolunteers.objects.filter(volunteer_name__icontains = search) 
    else:
        all_volunteers = OurVolunteers.objects.all 
    context = {
        'our_volunteers': all_volunteers,
    }
    return render (request ,'our_volunteers/list_our_volunteers.html', context = context )
@login_required
def list_our_collaborative_institutions(request):
    if 'search' in request.GET:
        search = request.GET [search]
        all_institutions = OurCollaborativeInstitutions .objects.filter (instituion_name__icontais = search )
    else:
        all_institutions = OurCollaborativeInstitutions .objects.all 
    context = {
        'our_collaborative_institutions': all_institutions,
    }
    return render (request ,'our_colaborative_institutions/list_our_colaborative_institutions_list.html', context = context)
@login_required
def list_others_projects (request):
    if 'search' in request.GET:
        search = request.GET [search]
        all_projects = OthersProjects.objects.filter (project_name__icontais = search)
    else:
        all_projects = OthersProjects.objects.all ()
    context = {
        'others_projects': all_projects,
    }
    return render (request ,'others_projects/list_others_projects.html', context = context )
@login_required
def update_our_dogs (request , id):
    our_dogs = OurDogs.objects.get (id = id)
    if request.method == 'GET':
        context = {
            'dog_form' : OurDogsForms (
                initial = {
                    'dog_name': our_dogs.dog_name,
                    'dog_age': our_dogs.dog_age,   
                    'dog_history': our_dogs.dog_history,
                    'dog_status': our_dogs.dog_status,
                }
            )
        }
        return render (request , 'our_dogs/update_our_dogs.html' , context = context)
    elif request.method == 'POST':
        dog_form =OurDogsForms (request.POST)
        if dog_form.is_valid ():
            
            our_dogs.dog_name = dog_form.cleaned_data ['dog_name']
            our_dogs.dog_age = dog_form.cleaned_data ['dog_age']
            our_dogs.dog_history= dog_form.cleaned_data ['dog_history']
            our_dogs.dog_status = dog_form.cleaned_data ['dog_status']
            our_dogs.save()
            context = {
                'message' : 'Se actualizo el  perro'
            }
            return render ( request , 'our_dogs/update_our_dogs.html' , context = context)
        else:
            context = {
                'dog_form_errors': dog_form.errors ,
                'dog_form' : OurDogsForms ()
            }
            return render ( request , 'our_dogs/update_our_dogs.html' , context = context)
@login_required
def update_our_volunteers (request , id):
    our_volunteer = OurVolunteers.objects.get (id = id)
    if request.method == 'GET':
        context = {
            'volunteer_form' : OurVolunteersForms (
                initial = {
                    'volunteer_name': our_volunteer.volunteer_name,
                    'volunteer_age': our_volunteer.volunteer_age,   
                    'volunteer_reason_to_be_a_volunteer':our_volunteer.volunteer_reason_to_be_a_volunteer,
                    'volunteer_favourite_dog_and_reason': our_volunteer.volunteer_favourite_dog_and_reason
                }
            )
        }
        return render (request , 'our_volunteers/update_our_volunteers.html' , context = context)
    elif request.method == 'POST':
        volunteer_form =OurVolunteersForms (request.POST)
        if volunteer_form.is_valid ():
            
            our_volunteer.volunteer_name = volunteer_form.cleaned_data ['volunteer_name']
            our_volunteer.volunteer_age = volunteer_form.cleaned_data ['volunteer_age']
            our_volunteer.volunteer_reason_to_be_a_volunteer= volunteer_form.cleaned_data ['volunteer_reason_to_be_a_volunteer']
            our_volunteer.volunteer_favourite_dog_and_reason = volunteer_form.cleaned_data ['volunteer_favourite_dog_and_reason']
            our_volunteer.save()
            context = {
                'message' : 'Se actualizo el  voluntario'
            }
            return render ( request , 'our_volunteers/update_our_volunteers.html' , context = context)
        else:
            context = {
                'volunteer_form_errors': volunteer_form.errors ,
                'volunteer_form' : OurVolunteersForms ()
            }
            return render ( request , 'our_volunteers/update_our_volunteers.html' , context = context)
@login_required
def update_our_colaborative_institutions (request , id):
    our_colaborative_institutions = OurCollaborativeInstitutions.objects.get (id = id)
    if request.method == 'GET':
        context = {
            'colaborative_institution_form' : OurCollaborativeInstitutionsForms (
                initial = {
                    'instituion_name':our_colaborative_institutions.instituion_name,
                    'institution_reason_to_colaborate': our_colaborative_institutions.institution_reason_to_colaborate,   
                    'institution_vision_of_animals':our_colaborative_institutions.institution_vision_of_animals,
                }
            )
        }
        return render (request , 'our_colaborative_institutions/update_our_colaborative_institutions.html' , context = context)
    elif request.method == 'POST':
        colaborative_institution_form  =OurCollaborativeInstitutionsForms (request.POST)
        if colaborative_institution_form.is_valid ():
            our_colaborative_institutions.instituion_name = colaborative_institution_form.cleaned_data ['instituion_name']
            our_colaborative_institutions.institution_reason_to_colaborate = colaborative_institution_form.cleaned_data ['institution_reason_to_colaborate']
            our_colaborative_institutions.institution_vision_of_animals= colaborative_institution_form.cleaned_data ['institution_vision_of_animals']
            our_colaborative_institutions.save()
            context = {
                'message' : 'Se actualizo la institucion colaborativa'
            }
            return render ( request , 'our_colaborative_institutions/update_our_colaborative_institutions.html' , context = context)
        else:
            context = {
                'colaborative_institution_errors': colaborative_institution_form.errors ,
                'colaborative_institution_form' : OurCollaborativeInstitutionsForms ()
            }
            return render ( request , 'our_colaborative_institutions/update_our_colaborative_institutions.html' , context = context)
@login_required
def update_others_projects (request , id):
    others_projects = OthersProjects.objects.get (id = id)
    if request.method == 'GET':
        context = {
            'others_projects_form' : OthersProjectsForms (
                initial = {
                    'project_name ': others_projects.project_name,
                    'institution_or_person_in_charge': others_projects.institution_or_person_in_charge,   
                    'project_objective':others_projects.project_objective,
                }
            )
        }
        return render (request , 'others_projects/update_others_projects.html' , context = context)
    elif request.method == 'POST':
        others_projects_form = OthersProjectsForms (request.POST)
        if others_projects_form.is_valid ():
            others_projects.project_name = others_projects_form.cleaned_data ['project_name']
            others_projects.institution_or_person_in_charge = others_projects_form.cleaned_data ['institution_or_person_in_charge']
            others_projects.project_objective= others_projects_form.cleaned_data ['project_objective']
            others_projects.save()
            context = {
                'message' : 'Se actualizo el proyecto'
            }
            return render ( request , 'others_projects/update_others_projects.html' , context = context)
        else:
            context = {
                'others_projects_form_errors': others_projects_form.errors ,
                'others_projects_form'  : OthersProjectsForms ()
            }
            return render ( request , 'others_projects/update_others_projects.html' , context = context)

class OurDogsDelete (DeleteView):
    model = OurDogs
    template_name = 'our_dogs/delete_our_dogs.html'
    success_url = '/modelos/nuestros_perros/'

class OurVolunteersDelete (DeleteView):
    model = OurVolunteers
    template_name ='our_volunteers/delete_our_volunteers.html'
    success_url = '/modelos/nuestros_voluntarios/'

class OurColaborativeInstitutionsDelete (DeleteView):
    model = OurCollaborativeInstitutions
    template_name = 'our_colaborative_institutions/delete_our_colaborative_institutions.html'
    success_url = '/modelos/nuestras_instituciones_colaborativas/'

class OthersProjectsDelete (DeleteView):
    model = OthersProjects
    template_name = 'others_projects/delete_others_projects.html'
    success_url = '/modelos/nuestros_proyectos/'