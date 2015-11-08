from django.http import HttpResponse
from django.template.loader import 

template = get_template('index.html')
html = template.render({'user': 'DOC'}, request)

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
	  html
	)
	return HttpResponse(output)

