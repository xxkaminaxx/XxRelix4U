from django.shortcuts import render
from .models import Artifact
# Create your views here.


# This page will render all artifacts on it.


def all_artifacts(request):
    artifacts = Artifact.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})
