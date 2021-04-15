from api.views import *
from django.urls import path

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:comp_id>/', companies_detail),
    path('companies/<int:comp_id>/vacancies/', comp_vac),
    path('vacancies/', vac_list),
    path('vacancies/<int:vac_id>/', vac_detail),
    path('vacancies/top/', vacancies_top)
]