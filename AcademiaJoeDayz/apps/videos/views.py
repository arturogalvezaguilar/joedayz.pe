from django.shortcuts import render
from django.views.generic import TemplateView


class Video(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, 'videos/video.html',)


