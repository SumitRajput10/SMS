from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from student_management_app.EmailBackEnd import EmailBackEnd


class home(View):
    def get(self, request):
        return render(request, 'index.html')


class loginPage(View):
    def get(self, request):
        return render(request, 'login.html')


class doLogin(View):
    def post(self, request):
        if request.method != "POST":
            return HttpResponse("<h2>Method Not Allowed</h2>")

        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')

        messages.error(request, "Invalid Login Credentials!")
        return redirect('login')


class get_user_details(View):
    def get(self, request):
        if request.user:
            return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
        else:
            return HttpResponse("Please Login First")


class logout_user(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')