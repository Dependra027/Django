from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import ContactForm, CalculatorForm
from .models import Student
from django.middleware.csrf import get_token
from .forms import InputForm
from .models import FormModel
from .forms import Signup
from .forms import SignupForm1


def All_chai(request):
    return render(request, 'chai.html')

def order(request,id):
    return HttpResponse(f'order {id}')

def identity(request, author):
    # Now let's try rendering the template from the main templates directory
    return render(request,'identity.html', {'author': author})
    # return HttpResponse(f'My name is {author}')

def Product_slug(request,slug):
    return HttpResponse(f'product slug is {slug}')


def student_list(request):
    # Get all students from the database
    students = Student.objects.all()

    context={
        'all_students': students
    }

    return render(request,'student.html',context);

    # Display a GreetingPass a variable name = “XYZ" from the view.Display: Hello, {{ name }}! in the template.
def greet(request):
    name="Dependra"
    # Test if template is found
    return render(request,'Greet.html',{'name':name})
    # Temporary test - uncomment below if template issues persist
    # return HttpResponse(f"Hello, {name}! Template test.")


# Show Today's DatePass the current date from the view.Display it in the template using the date filter in the format D M Y.

def show_date(request):
    # Get today's date
    today = datetime.now()
    
    context = {
        'current_date': today
    }
    
    return render(request, 'date.html', context)

# Conditional MessagePass is_holiday = True from the view.Show “Enjoy your holiday!” if True, else “Back to work.”

def g(request):
    greeting=[
        {"greet":"Enjoy your vacation", "is_holiday":True},
        {"greet":"No vacation", "is_holiday":False},
    ]
    context={
        "greets":greeting
    }
    return render(request,'greeting.html',context)
    
# Uppercase and LowercasePass city = 'Delhi'.Display it in uppercase and lowercase using filters.
def city(request):
    city="Delhi"
    return render(request,'city.html',{'city':city})

def monday_menu(request):
    return render(request,'monday_menu.html')


def office(request):
    person=[
        {"name":"Dependra","time":"Morning","stock":"Full", "isAuthenticated":True},
        {"name":"Vinit","time":"Evening","stock":"Half", "isAuthenticated":True},
        {"name":"Alok","time":"Morning","stock":"Full", "isAuthenticated":False},
        {"name":"Ajay","time":"Night","stock":"empty", "isAuthenticated":True},
        {"name":"Rudr","time":"afternoon","stock":"Full", "isAuthenticated":False}
    ]
    context={
        "allperson":person
    }
    return render(request,"person.html",context)

def child(request):
    return render(request, "child.html")

def childlist(request):
    return render(request, "childlist.html")

def product(request):
    return render(request, "lsit.html")


def contactview(request):
    # Initialize variables
    form = None
    submitteddata = None
    methodused = None

    if request.method == 'GET':
        # Handle GET request - display empty form
        methodused = 'GET'
        form = ContactForm()

    elif request.method == 'POST':
        # Handle POST request - process form data
        methodused = 'POST'
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form is valid, process the data
            submitteddata = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
                'contactmethod': form.cleaned_data['contactmethod'],
            }
            # In a real application, you might save to database or send email here
            form = ContactForm()  # Clear form after successful submission

    return render(request, 'contactform.html', {
        'form': form,
        'submitteddata': submitteddata,
        'methodused': methodused,
    })


def calculator_view(request):
    result = None
    form = CalculatorForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        number1 = form.cleaned_data['number1']
        number2 = form.cleaned_data['number2']
        operation = form.cleaned_data['operation']

        if operation == 'add':
            result = number1 + number2
        elif operation == 'sub':
            result = number1 - number2
        elif operation == 'mul':
            result = number1 * number2
        elif operation == 'div':
            result = 'Undefined' if number2 == 0 else (number1 / number2)
        elif operation == 'mod':
            result = 'Undefined' if number2 == 0 else (number1 % number2)

    return render(request, 'calculator.html', {
        'form': form,
        'result': result,
    })

# forms
# 1st way
def simpleForm(request):
    csrf_token=get_token(request)
    if request.method=="POST":
        textbox1=request.POST.get("text1")
        textbox2=request.POST.get("text2")
        return HttpResponse(f"The values are {textbox1} and {textbox2}")
    
    else:
        return HttpResponse(f"""<form method="post">
                        
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                        
        <label for="text1">Textbox 1:</label>
        <input type="text" name="text1" id="text1">

        <br><br>

        <label for="text2">Textbox 2:</label>
        <input type="text" name="text2" id="text2">

        <br><br>

        <input type="submit" value="Submit">
</form>""")
    
def formTemp(request):
    if request.method=='POST':
        name=request.POST.get("name1")
        email=request.POST.get("email1")
        password=request.POST.get("password1")

# validating if name ,emaila and password filled
        if name and email and password:
            return HttpResponse("Form submitted with name {name} and id {email}")
   
#    render the form
    return render(request,"forms.html")


def form1(request):
    if request.method=='POST':
        form=InputForm(request.POST)
        if form.is_valid():
            return HttpResponse("form submitted successfully");
    else:

        form=InputForm()

    return render(request,'form1.html',{'form':form})

def validation(request):

    submitForm= None
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

    #    setting error bydefault None  
        name_error=email_error=password_error=None

        if not name:
            name_error="Name is mandatory"
        if not email:
            email_error="Email is mandatory"
        if len(password)<6:
            password_error="Password should be greater than 6 digits"

        # if we have any of the error
        if name_error or email_error or password_error:
            return render(request,'valid.html',
            {
            # preserving the value so that the value should be present in the inpuut box
             'name':name,
             'email':email,
             'password':password,

            #  error 
             'name_error':name_error,
             'email_error':email_error,
             'password_error':password_error})
   
    
        # now we need that if form has no error, it should submit with the inputs
        # so make a variable submitForm above
        
        submitForm={
            'name':name,
            'email':email,
            'password':password
        }
    return render(request,'valid.html',{'submitForm':submitForm})

def signup(request):
    account_created=False
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        # now to create the objects in model table
        user=FormModel.objects.create(username=username, email=email, password=password)

        # username=username, here left one is column name and other is the value that we take from the form 
        user.save()
        account_created=True
    return render(request,'signUp.html',{'account_created':account_created})

def signup1(request):
    account_created=False
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=FormModel.objects.create(username=username,email=email,password=password)
            user.save()
            account_created=True
    else:
        form=Signup()
    return render(request, 'signup1.html', {'form':form, "account_created":account_created})

def signup2(request):
    user=FormModel.objects.all()
    account_created=False
    if request.method=='POST':
        form = SignupForm1(request.POST)
        if form.is_valid():
            form.save()
            account_created=True
            return render(request,'Signup2.html',{'form':form, 'account_created':account_created})
    else:
        form=SignupForm1()
    return render(request,'Signup2.html',{'form':form, 'users':user})

def delete(request,id):
    # taking out the user with id
    user=FormModel.objects.get(pk=id)
    user.delete()
    return redirect('signup2')

def edit(request,id):
    user=FormModel.objects.get(pk=id)
    if request.method=='POST':
        form=SignupForm1(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('signup2')
    else:
        form=SignupForm1(instance=user)
    return render(request, 'upadteForm.html', {'form':form, 'user':user})

from .forms import BlogForm
def insertblogpost(request):
    blogpost_created=False
    if request.method == "POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            blogpost_created=True
    else:
        form=BlogForm()
    return render(request,'insertForm.html',{'form':form, 'blogpost_created':blogpost_created})

from .models import Blogpost
def  blogposts(request):
    posts=Blogpost.objects.all()
    return render(request,'blogposts.html',{'posts':posts})

def blogpost_detail(request,id):
    post=Blogpost.objects.get(pk=id)
    return render(request,'blogpost_detail.html',{'post':post})

def setCookie(request):
    response=HttpResponse("Cookie set")
    response.set_cookie('name','Dependra', max_age=30)
    # multiple cookies can be set
    response.set_cookie('color','red')
    response.set_cookie('age','20')
    
    return response

def getCookie(request):
    name=request.COOKIES.get('name')
    color=request.COOKIES.get('color')
    age=request.COOKIES.get('age')

    if(name or color or age):
        return HttpResponse(f"Name: {name}, Color: {color}, Age: {age}")
    else:
        return HttpResponse("No cookies found")
    
def deleteCookie(request):
    response=HttpResponse("Cookie deleted")
    response.delete_cookie('name')
    response.delete_cookie('color')
    response.delete_cookie('age')
    return response

# practice questions 
def me(request,id):
    return HttpResponse(f"Post ID:{id}")

def ad(request, name, age):
    return HttpResponse(f"heello {name}, you are {age} year ")

def we(request,weather,city):
    return render(request,'we.html',{"weather":weather, "city":city})