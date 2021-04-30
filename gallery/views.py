from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from .models import Art
from .forms import ArtForm
from django.views.generic.base import TemplateView,RedirectView
from django.views import View
  

def show_view(request):
    info = Art.objects.all()
    return render(request,'show.html',{'info':info})


class AddView(TemplateView):
    template_name = 'add.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = ArtForm()
        stud = Art.objects.all()
        context = {'info':stud,'form':fm}
        return context
    def post(self,request):
        fm = ArtForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = ArtForm()
        return HttpResponseRedirect('/')

class DeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwargs):
        del_id = kwargs['id']
        Art.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

class UpdateView(View):
    def get(self,request,id):
        edit = Art.objects.get(pk=id)
        fm = ArtForm(instance=edit) 
        return render(request,'update.html',{'form':fm})

    def post(self,request,id):
        edit = Art.objects.get(pk=id)
        fm = ArtForm(request.POST,request.FILES,instance=edit)
        if fm.is_valid():
            fm.save()
        return render(request,'update.html',{'form':fm})
