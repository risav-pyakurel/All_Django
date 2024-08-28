from courses import views
from django.urls import path
urlpatterns=[
    path('learndj/',views.learn_django,name = 'learn_django'),

]