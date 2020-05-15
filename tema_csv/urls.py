from django.urls import path
from tema_csv.views import *

urlpatterns = [
    path('', my_template, name='my_template'),
    path('csv_display/', csv_display, name='csv_display'),
]
