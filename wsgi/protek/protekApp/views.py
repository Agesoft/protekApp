'''from django.http import render_to_response
def main_page(request): return render_to_response(
	'index.html',{'user':'DOC'}
	)
	'''
	
from django.shortcuts import render_to_response
def main_page(request):   return render_to_response(
    '../protek/templates/index.html', 
    { 'user': request.user } 
  )


