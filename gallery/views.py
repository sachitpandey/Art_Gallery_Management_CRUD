from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
# relative import of forms
from .models import Art
from .forms import ArtForm
  
  
'''def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = ArtForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["dataset"] = Art.objects.all()
          
    return render(request, "list_view.html", context)

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = Art.objects.get(id = id)
          
    return render(request, "detail_view.html", context)'''

def add_view(request):
    if request.method=='POST':
        fm = ArtForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = ArtForm()
    else:
        fm = ArtForm()
    stud = Art.objects.all()
    return render(request, "add.html", {'form':fm,'info':stud})

def delete_data(request,id):
    if request.method == 'POST':
        del_item = Art.objects.get(pk=id)
        del_item.delete()
        return HttpResponseRedirect('/')

def show_view(request):
    info = Art.objects.all()
    return render(request,'show.html',{'info':info})

def update_view(request,id):
    if request.method=='POST':
        edit = Art.objects.get(pk=id)
        fm = ArtForm(request.POST,request.FILES,instance=edit)
        if fm.is_valid():
            fm.save()
    else:
       edit = Art.objects.get(pk=id)
       fm = ArtForm(instance=edit) 
    return render(request,'update.html',{'form':fm})