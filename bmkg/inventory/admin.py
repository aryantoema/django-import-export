# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import decimal, csv

from django.contrib import admin
from django.http import HttpResponse
#from django.db.models import F

#from account.models import Akun, User
from import_export.admin import ImportExportModelAdmin
from .models import *
from .views import *

# Register your models here.

@admin.register(Kelembaban, Suhu, Tekanan, Angin, Radiasi)
class ViewAdmin(ImportExportModelAdmin):
#    exclude = ('tanggal',)
    list_per_page = 31
    actions = (export_parameters, export_excels,)

####################################################
