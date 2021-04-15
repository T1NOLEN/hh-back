from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import *


def companies_list(request):
    companies = Company.objects.all()
    comp_json = [each.to_json() for each in companies]
    return JsonResponse(comp_json, safe=False)


def companies_detail(request, comp_id):
    try:
        companies = Company.objects.get(id=comp_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    return JsonResponse(companies.to_json())


def comp_vac(request, comp_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=comp_id)
        vac_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    if vacancies:
        return JsonResponse(vac_json, safe=False)
    else:
        return JsonResponse('Company doesn\'t exists', safe=False)


def vac_list(request):
    vacancies = Vacancy.objects.all()
    vac_json = [vacancy.to_json() for vacancy in vacancies]
    if vac_json:
        return JsonResponse(vac_json, safe=False)
    else:
        return JsonResponse("No vacancies!", safe=False)


def vac_detail(request, vac_id):
    try:
        vac = Vacancy.objects.get(id=vac_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vac.to_json())


def sort_salary(vacant):
    return vacant.salary


def vacancies_top(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacant_json = [vacancy.to_json() for vacancy in vacancies]
    if vacant_json:
        return JsonResponse(vacant_json, safe=False)
    else:
        return JsonResponse("No vacancy available, check for updates later!", safe=False)