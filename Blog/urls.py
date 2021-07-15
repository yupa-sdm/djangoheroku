from django.urls import path
from Blog.views import about, contact, persons, index

urlpatterns = [
    path ('', index) ,
    path ('about/', about),
    path ('contact/', contact),
    path ('persons/', persons),
]
