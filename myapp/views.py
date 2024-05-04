from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})
    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data saved successfully!')

            # return render(request,'myapp/home.html',{'form':form})
            return HttpResponseRedirect(reverse('home'))
class CandidateView(View):
    def get(self,request,pk=None):
        # if pk:
        candidate = Resume.objects.get(id=pk)
            # print(candidate)
        return render(request,'myapp/candidate.html',{'candidate':candidate})