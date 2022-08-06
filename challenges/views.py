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
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        text = monthly_challenges[month]
        title = month.capitalize
        return render(request, "challenges/challenge.html", {
            "title": title,
            "text": text
        })
    except:
        return HttpResponseNotFound("This month is not supported!")

