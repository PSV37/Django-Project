from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View 
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .forms import UserForms
from django.contrib.auth import authenticate,login
from django.views import generic
from .models import Movie
# Create your views here.
def index(request):
    return render(request ,'marathi/index.html')

class UserFormView(View):
    form_class=UserForms
    template_name='marathi/Registration_form.html'


    def get(self,request):
        form=self.form_class(None)
        return render(request , self.template_name , {'form':form}) 


    def post(self,request):
        form = self.form_class(request.POST) 

        if form.is_valid():

            user = form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
      
            if user is not None:

      	      if user.is_active:
      		       login(request , user)
      		       return redirect('admin')

        return render(request, self.template_name, {'form': form})   		

def Admin(request):
   return render(request , 'marathi/dashboard.html')

def Profile(request):
   return render(request , 'marathi/profile.html') 

class CreateMovie(CreateView):
   model = Movie
   fields = ['movie_name','movie_catagory','movie_director','movie_producer','movie_image']


def moviedeatil(request):
   html=Movie.objects.all()
   context={
     'all':html,
   }
   return render(request , 'marathi/moviedetail.html',context)     

class DetailMovie(generic.DetailView):
  model = Movie
  template_name = 'marathi/detail.html'

class UpdateMovie(UpdateView):
   model = Movie
   fields =  ['movie_name','movie_catagory','movie_director','movie_producer','movie_image']  

class DeleteMovie(DeleteView):
  model = Movie
  success_url = reverse_lazy('Mdetail')

  def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)