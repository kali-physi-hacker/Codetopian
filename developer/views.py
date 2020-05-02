from django.shortcuts import render
from django.views.generic import View


class DeveloperProfileViewSet(View):
    """
    Get Developer Profile, Edit and Delete
    """
    def get(self, request, *args, **kwargs):
        template = "developer/profile.html"
        context = {}
        return render(request, template, context)