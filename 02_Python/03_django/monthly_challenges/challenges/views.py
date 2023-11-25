from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Aqui ya estoy cogiendo sol",
    "february": "El puto mes mas helado",
    "march": "Espero estar mejor",
    "april": "Aqui ya estoy cogiendo sol",
    "may": "El puto mes mas helado",
    "june": "Espero estar mejor",
    "july": "Aqui ya estoy cogiendo sol",
    "august": "El puto mes mas helado",
    "september": "Espero estar mejor",
    "october": "Aqui ya estoy cogiendo sol",
    "november": "El puto mes mas helado",
    "december": None,
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        raise Http404()
    
    
