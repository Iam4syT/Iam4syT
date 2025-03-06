from django.shortcuts import render
from familyMembers.models import Member

# Create your views here.
def home(request):
    return render(request, 'familyTree/home.html')

def about_us(request):
    return render(request, 'familyTree/about_us.html')

def familyTree(request):
    members = Member.objects.all()  # Retrieve all members
    return render(request, 'familyTree/members.html', {'members': members})
    