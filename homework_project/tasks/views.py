from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime, date, timedelta

def current_datetime(request):
    now = datetime.now()
    html = f"<h1>Текущая дата и время:</h1><p>{now.strftime('%d.%m.%Y %H:%M:%S')}</p>"
    return HttpResponse(html)

def multiplication_table(request):
    html = "<h1>Таблица умножения (1-10)</h1><table border='1' cellpadding='5'>"
    for i in range(1, 11):
        html += "<tr>"
        for j in range(1, 11):
            html += f"<td>{i} * {j} = {i*j}</td>"
        html += "</tr>"
    html += "</table>"
    return HttpResponse(html)

def programmer_day(request):
    year = datetime.now().year
    start_date = date(year, 1, 1)
    prog_day = start_date + timedelta(days=255)
    
    html = f"""
    <h1>День программиста в {year} году:</h1>
    <p>Это 256-й день года: <b>{prog_day.strftime('%d.%m.%Y')}</b></p>
    """
    return HttpResponse(html)