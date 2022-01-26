from io import BytesIO

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.core.files.base import ContentFile

from .form import ClientCreateForm
from .put_watermark import watermark_avatar

class ClientCreateView(View):
    """New client's view form"""
    model = ClientCreateForm()
    template_name = 'api/client_create.html'

    def get(self, request):
        form = ClientCreateForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ClientCreateForm(request.POST, request.FILES)
        for key, value in request.FILES.items():
            print('%s: %s' % (key, type(value)) )
        for key, value in request.POST.items():
            print('%s: %s' % (key, value) )
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template_name, context)
            return HttpResponse('Client does not created!')
        
        # Add watermark on the avatar
        instance = form.save(commit=False)
        im = watermark_avatar(instance.avatar)
        thumb_io = BytesIO()
        im.save(thumb_io, im.format, quality=60)
        instance.avatar.save(request.FILES['avatar'].name, ContentFile(thumb_io.getvalue()), save=False)
        instance.save()
                
        return HttpResponse('New client is registred')



