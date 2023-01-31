
from django.urls import path

from . import views


urlpatterns = [
    path ('nuestros_perros/', views.list_our_dogs),
    path ('nuestros_voluntarios/' , views.list_our_volunteers),
    path ('nuestros_proyectos/' , views.list_others_projects),
    path ('nuestras_instituciones_colaborativas/' , views.list_our_collaborative_institutions),
    path ('nuevo_perro/' , views.create_our_dogs),
    path ('nuevo_voluntario/' , views.create_our_volunteers),
    path ('nuevo_proyecto/' , views.create_others_projects),
    path ('nueva_institucion_colaborativa/' , views.create_our_collaborative_institutions),
    path ('actualizar_perro/<int:id>/' , views.update_our_dogs),
    path ('actualizar_voluntario/<int:id>/', views.update_our_volunteers ),
    path ('actualizar_institucion_colaborativa/<int:id>/' , views.update_our_colaborative_institutions),
    path ('actualizar_nuestros_proyectos/<int:id>/' , views.update_others_projects),
    path ('eliminar_perro/<int:pk>/' , views.OurDogsDelete.as_view()),
    path ('eliminar_voluntario/<int:pk>/' , views.OurVolunteersDelete.as_view()),
    path ('eliminar_institucion_colaborativa/<int:pk>/' , views.OurColaborativeInstitutionsDelete.as_view()),
    path ('eliminar_proyecto/<int:pk>/' , views.OthersProjectsDelete.as_view()),
]