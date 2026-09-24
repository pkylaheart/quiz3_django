from django.shortcuts import render

from .models import Student


def home(request):

    students = [
        {
            "name": "Abe Stephanie",
            "email": "abe.stephanie@gmail.com",
            "course": "BSA",
            "enrollment_date": "09-08-2026"
        },
        {
            "name": "Amey De Robles",
            "email": "amey.derobles@gmail.com",
            "course": "ABELS",
            "enrollment_date": "09-08-2026"
        },
        {
            "name": "Ken Kaneki",
            "email": "kenkaeni@gmail.com",
            "course": "BSPA",
            "enrollment_date": "09-08-2026"
        },
    ]

    return render(request, 'home.html', {'students': students})