from django.http import HttpResponse
def main_page(request):
    template = get_template('index.html')
	html = template.render({'user': 'DOC'}, request)
    return HttpResponse(html)