from django.shortcuts import render,redirect
from .models import product,cart
# Create your views here.
def index(request):

    prds = product.objects.all()
    return render(request,'Modified_files/index.html' ,{'prds':prds})

def xyz(request,id):
    c = product.objects.get(pk=id)
    data = cart.objects.create(prd_id = c,user_id = request.user.id)
    return redirect('/')