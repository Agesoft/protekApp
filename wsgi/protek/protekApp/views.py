import os
import sys

pth = os.path.join(os.path.dirname(__file__), 'templates/index.html')

from django.http import render_to_response
def main_page(request): return render_to_response(
	pth,{'user':'DOC'}
	)