from django.shortcuts import render_to_response

def home(request, *args, **kwargs):
    return render_to_response('360buy/index.html')

def test(request, *args, **kwargs):
    return render_to_response('360buy/test.html')
