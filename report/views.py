#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

import urllib, json

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
# Create your views here.
from xlsxwriter.workbook import Workbook

from io import BytesIO

@csrf_exempt
def all_doctors(request):
    if request.method == "GET":
        with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/") as url:
            data = json.loads(url.read().decode())
            aux = formatData(data)

            output = generate_pdf(aux)
            pdf = output.getvalue()
            output.close()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=all_doctors.pdf'
            response.write(pdf)
            return response

def category_report(request, categorys):

    categorys = categorys.split("&")

    data = []
    for category in categorys:
        with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/list-doctor/q/?category="+ str(category)) as url:
            jsons = json.loads(url.read().decode())
            aux = formatData(jsons)
            data = data + aux;

    output = generate_pdf(data)
    pdf = output.getvalue()
    output.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline;filename=doctors_by_category.pdf'
    response.write(pdf)
    return response


def formatData(json):
    data = []

    for element in json:
        data.append(
            [
                element["name"],
                element["registration"],
                element["CPF"],
                element["category"]
            ]
        )

    return data

def generate_pdf(data):

    data = [["Nome", "Registro", "CPF", "Categoria"]] + data

    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []

    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                        ('VALIGN',(0,0),(0,-1),'TOP'),
                        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ])
    
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t=Table(data2)
    t.setStyle(style)


    elements.append(t)
    doc.build(elements)
    return output

 
def xsml_all_doctors(request):
    with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/") as url:
        data = json.loads(url.read().decode())
        aux = formatData(data)
    
    output = xsml_report(aux)
    xsml = output.getvalue()
    output.close()
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Relatorio.xlsx"

    response.write(xsml)
    return response


def xsml_category(request, categorys):
    categorys = categorys.split("&")
    data = []
    for category in categorys:
        with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/list-doctor/q/?category="+ str(category)) as url:
            jsons = json.loads(url.read().decode())
            aux = formatData(jsons)
            data = data + aux;

    output = xsml_report(data)
    xsml = output.getvalue()
    output.close()
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Relatorio.xlsx"

    response.write(xsml)
    return response


def xsml_report(data):
    output = BytesIO()

    book = Workbook(output)
    sheet = book.add_worksheet('Relatorio')       

    sheet.write(0, 0, "Nome")
    sheet.write(0, 1, "Registro")
    sheet.write(0, 2, "CPF")
    sheet.write(0, 3, "Categoria")
    for row, columns in enumerate(data):
        for column, cell_data in enumerate(columns):
            sheet.write(row+1, column, cell_data)

    book.close()
    output.seek(0)

    return output
