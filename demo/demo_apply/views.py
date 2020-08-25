from django.shortcuts import render
from .models import Testdb
# Create your views here.
def index(request):
    filter = Testdb.objects.all()
    # filter = Testdb.objects.order_by('no')[:3]
    # filter = Testdb.objects.filter(eng_score__gt=80)
    return render(request, 'index.html',locals())