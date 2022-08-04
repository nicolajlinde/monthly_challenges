from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "awd",
    "february": "dairy",
    "march": "lard",
    "april": "fabril",
    "may": "maybe",
    "june": "noon",
    "july": "my pants are fly",
    "august": "sports-no",
    "september": "check my temper",
    "october": "octo",
    "november": "dont nut",
    "december": "hello santa"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response = f"<ul>{list_items}</ul>"
    return HttpResponse(response)


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")

