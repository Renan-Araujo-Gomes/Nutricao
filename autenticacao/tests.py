from django.test import TestCase

# Create your tests here.
from django.contrib import admin

from .models import Ativacao

admin.site.register(Ativacao)