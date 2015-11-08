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
	  'This is a simple Hello world http test!'
	)
	return HttpResponse(output)
