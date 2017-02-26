from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from app.models import Landlord, Review
import json


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

@csrf_exempt
def landlord_info(request, landlord_id):
    # get only the info for the particular ID
    landlord_object = Landlord.objects.get(id=landlord_id)

    comments = Review.objects.filter(landlord=landlord_object)
    comments_list = [comment.as_json() for comment in comments]

    return JsonResponse({
        'landlord': landlord_object.as_json(),
        'comments': comments_list
    })


@csrf_exempt
def get_comments_for_landlord(request, landlord_id):
    # get the landlord object
    landlord = Landlord.objects.get(id=landlord_id)
    print landlord
    comments = Review.objects.filter(landlord=landlord)
    print comments

    comment_list = [comment.as_json() for comment in comments]

    return JsonResponse({
        'comments': comment_list
    })

@csrf_exempt
def add_comment(request, landlord_id):
    params = json.loads(request.body)['params']
    reviewer_name = params['reviewerName']
    # print reviewer_name
    reviewer_email = params['reviewerEmail']
    review_text = params['reviewText']
    star_rating = params['starRating']

    # get the landlord object
    landlord = Landlord.objects.get(id=landlord_id)

    # create the Review object
    review = Review.objects.create(
        reviewer_name=reviewer_name,
        reviewer_email=reviewer_email,
        review_text=review_text,
        star_rating=star_rating,
        landlord=landlord
    )

    review.save()
    return JsonResponse({
        'review': review.as_json()
    })
