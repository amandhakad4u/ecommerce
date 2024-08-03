
from django.shortcuts import render, HttpResponse, redirect;
# Create your views here.
from .models import users




def home (request) :

    return render (request, 'home.html')








def shopmen (request) :

    return render (request, 'shop.html')   
 
def shopwomen (request) :

    return render (request, 'shop.html')    

def shopclearance (request) :

    return render (request, 'shop.html')    








def cart (request) :
    
    return render (request, 'cart.html')    







def account (request) :

    return render (request, 'account.html')    




def order (request) :

    return render (request, 'order.html')    





def login (request) :


    return render (request, 'login.html')


def signup(request) :
    
    
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')

            # Check if user with the same email already exists
        existing_user = users.objects.filter(email=email).exists()
        if existing_user:
            return render(request, 'signup.html', {'error_message': 'User with this email already exists.'})

            # Create and save User instance
        user = users(name=name, email=email, dob=dob, password=password)
        user.save()
        
        return redirect('home')


    return render(request, 'signup.html')
 
 
def forgotpassword(request):
    pass
















