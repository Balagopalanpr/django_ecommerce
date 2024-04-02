from django.shortcuts import render
from django.db.models import Q
from shop.models import product

# Create your views here.
def search(request):
    p=None
    q=""
    if (request.method=="POST"):
        query=request.POST['q']
        # print(query)
        if(query):
            p=product.objects.filter(Q(name__icontains=query)|Q(desc__icontains=query))
    return render(request,'search.html',{'p':p,'q':q})

