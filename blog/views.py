from django.shortcuts import render
from django.views import View
from io import BytesIO
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.conf import settings
import platform

from django.http import FileResponse, Http404
from xhtml2pdf import pisa

class CV(View):
    formatter = None
    
    template_name = 'cv.html'

    def get(self, request, *args, **kwargs):
        
        if self.formatter == "pdf":
            print("pdf")
            return self.render_to_pdf(self.template_name,request)
        elif self.formatter == "html":
            print("html")
            return self.render_to_html(self.template_name,request)

        
    
    def render_to_pdf(self, template_src, request):
        if platform.system() == "Windows":
            template_path = settings.BASE_DIR+'\\templates\cv.pdf'
        else:
            template_path = settings.BASE_DIR+'/templates/cv.pdf'
        
        print(template_path)
        # find the template and render it.
        #template = get_template(template_path)
        try:
            return FileResponse(open(template_path, 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()

    def render_to_html(self, template_src, context_dict):
        return render(context_dict, template_src)




