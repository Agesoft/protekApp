from django.http import HttpResponse
from django.template.loader import get_template

template = get_template('index.html')
html = template.render({'user': 'DOC'}, request)



pth = os.path.join(os.path.dirname(__file__), 'templates')

def main_page(request):
	return HttpResponse(html)
	
	