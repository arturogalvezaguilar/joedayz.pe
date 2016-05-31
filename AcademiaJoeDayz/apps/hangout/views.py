from django.shortcuts import render
from django.views.generic import TemplateView


class Hangout(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, 'hangout/hangout.html',)


