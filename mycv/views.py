from django.shortcuts import render

# Create your views here.

def index_view(request):
    content = {'name':'Arian', 'lastname':'Khademzade', 'grade':'11th', 'skills': 'python' 'a little bit django and c', 
               'gmail': 'ariankhademzadeh0@gmail.com', 'job': 'Student', 'age': '17'}
    return render(request, "website/index.html", content)