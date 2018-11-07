#//************************************************************************//#
#//************************************************************************//#
# Author : Chandan Mahto
# Date : 25-10-2018
# Version : 1.0.0
# Changelog : #v 1.0.0 : +added profile view to show the details of 
#						 logged in user
#						 +added home view to render the home page of 
#						 blog
#						 +added default view to catch all the 'tampered'
#						 urls
#						 +added signup view to enable user signups
#						 +added error view to deal with errors in various views
#						 +added dashboard view for best UI experience
#						 +added success view to deal with success in some views
#						 +added login view to make some use of signup view
#					     +added logout view to free users from their pain
#						 +added create_posts view to prevent boredom of users from 
#					      clicking the 4 links on the dashboard.
#						 +added functionality that redirects users to dashboard if 
#                         user attempts to view login or signup page after logging in
#						  
#//************************************************************************//#
#//************************************************************************//#

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import signupform, loginform, postform
from django.contrib.auth.models import User
import django.contrib.auth as au
from django.urls import reverse
from .models import posts

#//************************************************************************//#

def home(request):
	''' Renders the home.html file to the user
	'''
	return(render(request,'home/home.html'))

#//************************************************************************//#
	
def default(request,slug):
	''' renders the home.html file to any wrong
		request that doesn't map to any other view 
	'''
	return HttpResponseRedirect(reverse('home'))

#//************************************************************************//#	

def signup(request):
	''' renders the signup.html file along with 
		an empty signup form for the user to fill and 
		send request to create an account. 
	'''
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = signupform(request.POST)
			if form.is_valid():
				user = User.objects.create_user(username = form.cleaned_data['USERNAME'],
												email = form.cleaned_data['EMAIL'],
												password = form.cleaned_data['PASSWORD'],)
				user.first_name = form.cleaned_data['FIRST_NAME']
				user.last_name = form.cleaned_data['LAST_NAME']
				user.save()
				request.session['task'] = "signup"
				return HttpResponseRedirect(reverse('success'))
			else :
				return HttpResponseRedirect(reverse('error'))
		else :
			form = signupform()
		return(render(request,'signup/signup.html'))
	else :
		return HttpResponseRedirect(reverse('dashboard'))
#//************************************************************************//#

def error(request):
	''' used to return a simple error response if something doesn't go right in views
	'''
	return HttpResponse('Something went wrong. Visit the homepage at sxcranblog.org')

#//************************************************************************//#

def dashboard(request):
	''' renders the dashboard.html for the verified and authenticated user
		it also displays the posts that are recommended for the user
	'''
	if request.user.is_authenticated :
		pass
	else :
		return HttpResponseRedirect(reverse('login'))
	user_posts = posts.objects.all()
	return render(request, 'user/dashboard.html',{'user_posts' : user_posts})

#//************************************************************************//#

def success(request):
	''' displays a success message on signup and logout tasks
	'''
	task = request.session.get('task')
	if task == "signup":
		del request.session['task']
		return render(request,'misc/success.html', {'link':"login",'message':" to log in to your account",})
	elif task == "logout":
		del request.session['task']
		return render(request,'misc/success.html', {'link':"home",'message':" to return to home",})
	else:
		return HttpResponseRedirect(reverse('error'))

#//************************************************************************//#

def login(request):
	''' performs user login 
	'''
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = loginform(request.POST)
			if form.is_valid():
				username = request.POST['USERNAME']
				password = request.POST['PASSWORD']
				user = au.authenticate(username=username, password=password)
				if (user is not None):
					au.login(request,user)
					request.session['logged'] = True 
					return HttpResponseRedirect(reverse('dashboard'))
				else :
					return HttpResponseRedirect(reverse('login'))
		else :
			form = loginform()
		return(render(request,'signup/login.html'))
	else :
		return HttpResponseRedirect(reverse('dashboard'))
#//************************************************************************//#

def logout(request):
	''' performs user logout
	'''
	try :
		au.logout(request)
		request.session['task'] = "logout"
		request.session['logged'] = False
		return HttpResponseRedirect(reverse('success'))
	except :
		pass
	return HttpResponseRedirect(reverse('home'))

#//************************************************************************//#

def create_posts(request):
	''' used to add a new post on the site.
		user enters the post heading and body which is stored along
		with the username of the op(original poster)
	'''
	if request.user.is_authenticated:
		pass
	else :
		return HttpResponseRedirect(reverse('login'))
	if request.method == "POST":
		form = postform(request.POST)
		if form.is_valid():
			heading = request.POST['POST_HEADING']
			body = request.POST['POST_BODY']
			if request.user.is_authenticated:
				post = posts.objects.create(post_heading = heading,
											post_op = request.user,
											post_body = body)
				return HttpResponseRedirect(reverse('dashboard'))
			else :
				return HttpResponseRedirect(reverse('error'))
	else :
		form = postform()
	return(render(request,'posts/new.html'))

#//************************************************************************//#

def profile(request):
	''' displays the profile.html containing username, name, roll
		and department of the logged in user 
	'''
	if request.user.is_authenticated:
		first_name = request.user.first_name
		second_name = request.user.last_name
		username = request.user.username
		email = request.user.email
		return render(request,'user/profile.html',
								{'first_name' : first_name,
								 'last_name' : second_name,
								 'username' : username,
								 'email' : email,
								})
	else :
		return HttpResponseRedirect(reverse('login'))