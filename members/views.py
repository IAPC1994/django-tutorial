from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  # mydata = Member.objects.all().values()
  # mydata = Member.objects.all().values_list('firstname')
  # mydata = Member.objects.filter(firstname='Ivan').values()
  # mydata = Member.objects.filter(firstname='Ivan', id=1).values() # **AND**

  # mydata = Member.objects.filter(firstname='Ivan').values() | Member.objects.filter(firstname='Melisa').values() # **OR**
  # mydata = Member.objects.filter(Q(firstname='Ivan') | Q(firstname='Melisa')).values() # **OR**
  # mydata = Member.objects.filter(firstname__startswith='I').values(); #**Starts with**

  # mydata = Member.objects.all().order_by('firstname').values(); #**OrderBy ASC**
  mydata = Member.objects.all().order_by('-firstname').values(); #**OrderBy ASC**

  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'firstname': 'Ivan Panussis',
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))