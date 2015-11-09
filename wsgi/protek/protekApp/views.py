from django.http import HttpResponse
from django.template.loader import get_template

def main_page(request):
    template = get_template('index.html')
	outp = template.render({'user': 'DOC'})
    return HttpResponse(outp)