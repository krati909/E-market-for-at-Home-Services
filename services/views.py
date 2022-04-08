import warnings

from django.core.checks import messages
from django.db import connection
from django.shortcuts import render, redirect

import warnings
# Create your views here.



def service(request):
    return render(request, 'services.html')