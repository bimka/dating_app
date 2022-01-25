from PIL import Image

from urllib import request
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
            print('%s: %s' % (key, value) )
        for key, value in request.POST.items():
            print('%s: %s' % (key, value) )
        print(dir(form))
        if not form.is_valid():
            #context = {'form': form}
            #return render(request, self.template_name, context)
            return HttpResponse('Client does not created!')
        """if form.image:
            return HttpResponse('form.image is')
            im = Image.open(form.image)
            im.thumbnail((220, 130), Image.ANTIALIAS)
            thumb_io = BytesIO()
            im.save(thumb_io, im.format, quality=60)
            instance.image.save(im.filename, ContentFile(thumb_io.getvalue()), save=False)"""
        c = form.save(commit=False)
        c.avatar = watermark_avatar(input_avatar_path = request.FILES['avatar'])
        c.save()

        return HttpResponse('New client is registred')



