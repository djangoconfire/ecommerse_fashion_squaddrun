from django.shortcuts import render
from forms import EcommerseForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import traceback

# rendering home page 
def home(request):
	form=EcommerseForm()
	return render(request,'home.html',{'form':form})

def ImageDetail(request):
	pass


# here getting associated tags with image and then saving into database with image as key and tags as values
# Image --> key  and tags--> value
@csrf_exempt
def UploadImage(request):
	print 'inside image '
	if request.method=="POST":
		try:
			form_data=request.POST.get('form_data')
			print form_data
			return JsonResponse({'success':'True'},safe=False)
		except Exception as e:
			return JsonResponse({'success':'False','exception':str(e)})	
	else:
		message="This is not a post request"
		return JsonResponse({'exception':message})


				