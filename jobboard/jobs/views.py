from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Job

from .forms import JobForm


def home(request):
    jobs = Job.objects.all().order_by('-created')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def new_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            # job.posted_by = request.user
            job.posted_by = User.objects.get(username='admin')
            job.save()
            return redirect('/')
    form = JobForm()
    return render(request, 'jobs/job_edit.html', {'form': form})