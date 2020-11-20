from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured


# Create your views here.
def index(request):
    pass

class Main(object):
    template = ""
    favorite_number = None
    least_favorite_number = None
    
    def get(self, request):
        print("GET fav:", self.favorite_number, " GET Least:",self.least_favorite_number)
        temp = self.get_template()
        if self.favorite_number == None:
            self.favorite_number = 1
            self.least_favorite_number = 1
        
        context = {
            'sum': self.add(),
            'difference': self.subtract(),
            'product': self.multiply(),
            'factor': self.divide(),
        }
        return render(request, temp, context)
    
    def post(self, request):
        temp = self.get_template()
        print(request.POST)
        if request.POST['favorite'] == '' or request.POST['least'] == '' or request.POST['least'] == '0':
            return redirect("/")
        self.favorite_number  = int(request.POST['favorite'])
        self.least_favorite_number = int(request.POST['least'])
        print("POST fav:", self.favorite_number, " POST Least:",self.least_favorite_number)
        context = {
            'sum': self.add(),
            'difference': self.subtract(),
            'product': self.multiply(),
            'factor': self.divide(),
        }
        return render(request, temp, context)
    
    def get_template(self):
        if self.template == "":
            raise ImproperlyConfigured('"Template" not defined.')
        return self.template
    
    def add(self):
        return self.favorite_number + self.least_favorite_number
    def subtract(self):
        return self.favorite_number-self.least_favorite_number
    def multiply(self):
        return self.favorite_number*self.least_favorite_number
    def divide(self):
        return self.favorite_number/self.least_favorite_number
    
class Calculator(Main, View):
    template = 'index.html'
    favorite_number = 1
    least_favorite_number = 1