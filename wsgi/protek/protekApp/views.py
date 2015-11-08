from django.http import HttpResponse
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
	  os.path.join(os.path.dirname(__file__), 'templates')
	)
	return HttpResponse(output)
