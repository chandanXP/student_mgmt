from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'app.html')


def record(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = StudentForm()

    return render(request, 'list.html', {'form': form})

