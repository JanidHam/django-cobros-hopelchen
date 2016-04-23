from django.shortcuts import render, render_to_response, RequestContext



def home(request):

	return render_to_response('index.html', {}, context_instance=RequestContext(request))