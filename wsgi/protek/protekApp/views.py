import sys

try:

from django.http import HttpResponse
from django.http import Http404
from django.template.loader import get_template


template = get_template('index.html')	
pth = template.render({'user': 'DOC'})

def main_page(request):
	output = '''
	    <html>
	        <head><title>%s</title></head>
		<body>
			<h1>%s</h1><p>%s</p>
		</body>
	    </html>
	''' % (
	  'Test Page',
	  'Created By Davall Clarke',
	  pth
	)
	return HttpResponse(output)
	except:
		raise Http404("Failed My Youth!!!%s : ",sys.exc_info()[0])