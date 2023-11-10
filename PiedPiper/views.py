from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')

def game(request):
    return render(request,'game.html')

def genre(request):
    return render(request,'genre.html')

def status(request):
    return render(request,'status.html')

def cart(request):
    return render(request,'cart.html')

def account(request):
    return render(request,'account.html')