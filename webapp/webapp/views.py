from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from app.models import Landlord


def index_view(request):
    return render(request, 'index.html')

@csrf_exempt
def search_landlords(request):
    q = request.GET.get('q')
    # find landlords with name or address or contact_name like query

    filtered_items = Landlord.objects.filter(
        Q(landlord_name__contains=q) |
        Q(contact_name__contains=q) |
        Q(address__contains=q)
    )

    items = [item.as_json() for item in filtered_items]

    return JsonResponse({
        'landlords': items
    })
