from django.contrib import admin

from Models.models import OurDogs , OurVolunteers , OurCollaborativeInstitutions , OthersProjects

@admin.register(OurDogs)
class OurDogsAdmin(admin.ModelAdmin):
    list_display = ('id','dog_name' , 'dog_age' ,'dog_status')
    list_filter =  ('dog_name' , 'dog_age' ,'dog_status')
    search_fields =  ('dog_name' , 'dog_age' ,'dog_status')
@admin.register (OurVolunteers)
class OurVolunteersAdmin(admin.ModelAdmin):
    list_display = ( 'id','volunteer_name' , 'volunteer_age')
    list_filter =  ('volunteer_name' , 'volunteer_age')
    search_fields =  ('volunteer_name' , 'volunteer_age')
@admin.register (OurCollaborativeInstitutions)
class OurColaborativeInstitutionsAdmin(admin.ModelAdmin):
    list_display = ( 'id','instituion_name' ,'institution_reason_to_colaborate')
    list_filter =  ('instituion_name' ,'institution_reason_to_colaborate')
    search_fields =  ('instituion_name' ,'institution_reason_to_colaborate')
@admin.register (OthersProjects)
class OthersProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'institution_or_person_in_charge')
    list_filter =  ('project_name', 'institution_or_person_in_charge')
    search_fields =  ('project_name', 'institution_or_person_in_charge')

# Register your models here.
