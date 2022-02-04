from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from image.models import Image


class Depth(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        image_file = request.FILES.get('image')
        image = Image.objects.create(image=image_file)
        return HttpResponse('done')
