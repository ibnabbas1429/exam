from django.shortcuts import render, HttpResponse
from django.template.loader import get_template, render_to_string

from fpdf import FPDF, HTMLMixin

from . models import Exam

# Create your views here.


def examonline(request):
    results = Exam.objects.all()

    return render(request, 'index.html', {"Exam":results})

def examonline2(request):
    results = Exam.objects.all()

    return render(request, 'quiz.html', {"Exam":results})


'''
class HtmlPdf(FPDF, HTMLMixin):
    pass


def print_pdf(request):    
    pdf = HtmlPdf()
    pdf.add_page()
    pdf.write_html(render_to_string('pdf/example.html'))

    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Type'] = 'application/pdf'

    return response

    '''