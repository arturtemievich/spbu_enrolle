from django.urls import path
from . import views


urlpatterns = [
    path("direction/<int:fac_id>/", views.all_directions),
    path("direction/<int:fac_id>/<int:total_summ>/", views.all_directions),
    path("", views.all_faculty),
]
