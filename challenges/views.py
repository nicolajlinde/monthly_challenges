from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Walking 20 min everyday.",
    "february": "Code python everyday.",
    "march": "100 hours of Godot Engine",
    "april": "Swim 10k every week.",
    "may": "Relax and travel to Thailand.",
    "june": "Draw everyday.",
    "july": "Rollerblade 5k a week.",
    "august": "Don't eat meat for the whole month.",
    "september": "Learn Vue and build a TODO app.",
    "october": "Find a job.",
    "november": "Dont nut",
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
        raise Http404

