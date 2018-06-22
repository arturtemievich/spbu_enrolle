from django.shortcuts import render
from faculty.models import Faculty, Direction


def all_faculty(request):
    faculties = Faculty().get_faculties()
    return render(request, "faculty/faculties.html", context={"faculties": faculties})


def all_directions(request, fac_id):
    if request.GET:
        total_summ = request.GET.get("total_summ")
        directions = Direction.objects.filter(faculty_id=fac_id, total_result__gte=total_summ)
    else:
        directions = Direction.objects.filter(faculty_id=fac_id)
    
    return render(request, "faculty/directions.html", context={"directions": directions})

