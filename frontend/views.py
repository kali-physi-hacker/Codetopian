from django.shortcuts import render


def find_us(request):
    template = "find_us.html"
    context = {
        "find_us_active": "active"
    }
    return render(request, template, context)