from django.shortcuts import render
from artifacts.models import Artifact
# Create your views here.


def do_search(request):
    artifacts = Artifact.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"artifacts": artifacts})
