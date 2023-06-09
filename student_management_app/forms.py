from django import forms
from django.forms import Form
from student_management_app.models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    course_id = forms.ChoiceField(label="Course", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=[], widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['course_id'].choices = self.get_course_choices()
        self.fields['gender'].choices = self.get_gender_choices()
        self.fields['session_year_id'].choices = self.get_session_year_choices()

    @staticmethod
    def get_course_choices():
        courses = Courses.objects.values_list('id', 'course_name')
        return list(courses)

    @staticmethod
    def get_gender_choices():
        return [('Male', 'Male'), ('Female', 'Female')]

    @staticmethod
    def get_session_year_choices():
        session_years = SessionYearModel.objects.values_list('id', 'session_display')
        return list(session_years)


class EditStudentForm(AddStudentForm):
    pass

