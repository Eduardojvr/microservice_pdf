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

@csrf_exempt
def all_doctors(request):
    if request.method == "GET":
        with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/") as url:
            data = json.loads(url.read().decode())
            aux = formatData(data)
            generate_pdf(aux)
            with open('generated_pdf/all_doctors.pdf',encoding="ISO8859-1",mode='r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=all_doctors.pdf'
                return response
            pdf.closed

def category_report(request, categorys):

    categorys = categorys.split("&")

    data = []
    for category in categorys:
        with urllib.request.urlopen("http://localhost:8000/doctor/api-doctor/list-doctor/q/?category="+ str(category)) as url:
            jsons = json.loads(url.read().decode())
            aux = formatData(jsons)
            data = data + aux;
    
    generate_pdf(data)
    with open('generated_pdf/all_doctors.pdf',encoding="ISO8859-1",mode='r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=all_doctors.pdf'
                return response
    pdf.closed


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

    doc = SimpleDocTemplate("generated_pdf/all_doctors.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
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
