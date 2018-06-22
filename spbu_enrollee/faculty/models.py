from django.db import models
from faculty.pars import get_all_faculties


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        db_table = "faculty"

    def get_faculties(self):
        
        if not bool(Faculty.objects.all().count()):
            for item in get_all_faculties():
                faculty = Faculty(name=item.name)
                faculty.save()
                
                for _ in item.directions:
                    Direction(faculty_id=faculty.id, name=_).save()
        
        return Faculty.objects.all()


class Direction(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    total_result = models.IntegerField()
    
    class Meta:
        db_table = "direction"
