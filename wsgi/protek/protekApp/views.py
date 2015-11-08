from django.http import render_to_response
def main_page(request): return render_to_response(
	'templates/index.html',{'user':'DOC'}
	)