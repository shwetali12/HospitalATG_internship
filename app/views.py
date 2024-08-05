from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm, BlogPostForm,CategoryForm
from .models import User ,BlogPost,Category
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404



def register(request):
    msg = None
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user
            return redirect('login')  # Redirect to the login page
        else:
            print('not valid')
            
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
   
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print({username},{password})

            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')
            elif user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')

            else:
                print({username},{password})
                print('Invalid credentials')
        else:
            print('Error validating form')
        
    return render(request, 'login.html', {'form': form})

def index(request):
    return render(request, 'index.html')

# Registration view
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.doctor = request.user
            blog_post.save()  # Save the new employee to the database
            print(blog_post.Title)
            return redirect('doctor')  # Redirect to a page that lists employees

        else:
            print(form.errors)
    else:
        form = BlogPostForm()

    return render(request, 'create_post.html',{'form': form})


@login_required
def doctor(request):
    bpost = BlogPost.objects.all()
    return render(request, 'doctor.html' ,{'bpost':bpost})


@login_required
def patient(request):
    categories = Category.objects.all()
    cat_post = {}
    
    for category in categories:
        posts = BlogPost.objects.filter(Category=category)
        cat_post[category] = posts
    return render(request, 'patient.html',{'cat_post':cat_post})

def logout_view(request):
    logout(request)
    return redirect('/index') 

def delete(request,id):
    post = BlogPost.objects.get(id=id)
    post.delete()
    return redirect('doctor')


def edit(request,id):
    blog = get_object_or_404(BlogPost, id=id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()  # Save the updated employee information
            return redirect('doctor')  # Redirect to the list of employees

    else:
        form = BlogPostForm(instance=blog)

    return render(request, 'edit.html', {'form': form, 'blog': blog})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()  # Save the new employee to the database
            return redirect('doctor')  # Redirect to a page that lists employees

        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, 'create_category.html',{'form': form})

