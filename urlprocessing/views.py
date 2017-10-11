from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ShortenedUrlForm
from .models import ShortenedUrl
from .utils import StringShortener

class ShortenURLView(View):
	form_class = ShortenedUrlForm
	initial = {}
	template_name = 'urlprocessing/add_url.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
		    # <process form cleaned data>
		    existed_url = ShortenedUrl.objects.filter(original_url=form.cleaned_data['original_url'])
		    if existed_url.exists():
		    	return HttpResponse(existed_url[0].hash_url)
		    new_url = form.save()
		    new_url.hash_url = request.build_absolute_uri() + StringShortener().encode_url(n=new_url.id)
		    new_url.save()

		    return HttpResponse(new_url.hash_url)

		return render(request, self.template_name, locals())


class OriginalUrlView(View):
	def get(self, request, hashval, *args, **kwargs):
		try:
			url_to_redirect = ShortenedUrl.objects.get(hash_url__endswith=hashval)
			return redirect(url_to_redirect.original_url)
		except ShortenedUrl.DoesNotExist as e:
			return redirect('/')
		
		
