# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
import csv, xlwt
from datetime import datetime
from datetime import timedelta
#import xlwt

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

#from django.urls import reverse
from .models import *
from .forms import *

#FUNGSI DISPLAY
def index(request):
    return render(request, 'inv/index.html')

def view_kelembaban(request):
	datas = Kelembaban.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Kelembaban',
	}
	return render(request, 'inv/index.html', context)

def view_suhu(request):
	datas = Suhu.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Suhu',
	}
	return render(request, 'inv/index.html', context)

def view_tekanan(request):
	datas = Tekanan.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Tekanan',
	}
	return render(request, 'inv/index.html', context)

def view_angin(request):
	datas = Angin.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Angin',
	}
	return render(request, 'inv/index.html', context)

def view_radiasi(request):
	datas = Radiasi.objects.all()
	context = {
		'datas' : datas,
		'header' : 'Radiasi',
	}
	return render(request, 'inv/radiasi.html', context)



#FUNGSI TAMBAH_DATA
def add_data(request, cls):
	if request.method == "POST":
		form = cls(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls()
		return render(request, 'inv/add_new.html', {'form': form})

def add_kelembaban(request):
	return add_data(request, KelembabanForm)

def add_suhu(request):
	return add_data(request, SuhuForm)

def add_tekanan(request):
	return add_data(request, TekananForm)

def add_angin(request):
	return add_data(request, AnginForm)

def add_radiasi(request):
	return add_data(request, RadiasiForm)

#FUNGSI EDIT_DATA
def edit_data(request, pk, model, cls):
    data = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=data)

        return render(request, 'inv/edit_data.html', {'form': form})

def edit_kelembaban(request, pk):
    return edit_data(request, pk, Kelembaban, KelembabanForm)

def edit_suhu(request, pk):
    return edit_data(request, pk, Suhu, SuhuForm)

def edit_tekanan(request, pk):
    return edit_data(request, pk, Tekanan, TekananForm)

def edit_angin(request, pk):
    return edit_data(request, pk, Angin, AnginForm)

def edit_radiasi(request, pk):
    return edit_data(request, pk, Radiasi, RadiasiForm)

#FUNGSI DELETE
def delete_kelembaban(request, pk):

    template = 'inv/index.html'
    Kelembaban.objects.filter(tanggal=pk).delete()

    datas = Kelembaban.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_suhu(request, pk):

    template = 'inv/index.html'
    Suhu.objects.filter(tanggal=pk).delete()

    datas = Suhu.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_tekanan(request, pk):

    template = 'inv/index.html'
    Tekanan.objects.filter(tanggal=pk).delete()

    datas = Tekanan.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_angin(request, pk):

    template = 'inv/index.html'
    Angin.objects.filter(tanggal=pk).delete()

    datas = Angin.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

def delete_radiasi(request, pk):

    template = 'inv/index.html'
    Radiasi.objects.filter(tanggal=pk).delete()

    datas = Radiasi.objects.all()

    context = {
        'datas': datas,
    }

    return render(request, template, context)

#EXPORT ACTIONS LIST CSV
def export_parameters(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parameter.csv"'
    writer = csv.writer(response)
    writer.writerow(['tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                    'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23'])
    parameters = queryset.values_list('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                    'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23')
    for parameter in parameters:
        writer.writerow(parameter)
    return response
export_parameters.short_description = 'Export to csv'

#EXPORT ACTIONS LIST EXCEL
def export_excels(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={date}-parameter.xlsx'.format(date=datetime.now().strftime('%Y-%m-%d'),)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('parameter')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'yyy/mm/dd'

    columns = [
        ('tanggal'),
        ('jam0'), 
        ('jam1'), 
        ('jam2'), 
        ('jam3'), 
        ('jam4'), 
        ('jam5'), 
        ('jam6'), 
        ('jam7'),
        ('jam8'), 
        ('jam9'),
        ('jam10'), 
        ('jam11'), 
        ('jam12'), 
        ('jam13'), 
        ('jam14'), 
        ('jam15'), 
        ('jam16'),
        ('jam17'),
        ('jam18'), 
        ('jam19'), 
        ('jam20'), 
        ('jam21'), 
        ('jam22'), 
        ('jam23'),
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style, date_format)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    date_format = xlwt.XFStyle()

    rows = queryset.values_list('tanggal', 'jam0', 'jam1', 'jam2', 'jam3', 'jam4', 'jam5', 'jam6', 'jam7','jam8', 'jam9',
                    'jam10', 'jam11', 'jam12', 'jam13', 'jam14', 'jam15', 'jam16', 'jam17','jam18', 'jam19', 'jam20', 'jam21', 'jam22', 'jam23')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style, date_format)
 #           row_value = row_value
  #          row_format = row_format
   #         if row_format == 'Durations':
    #            row.number_format = '%Y%m%d'


#        for col_num in range(len(row)):
 #           ws.write(row_num, col_num, row[col_num], font_style)


    wb.save(response)
    return response

export_excels.short_description = 'Export to excel'