from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE = (
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Banglore', 'Banglore'),
    ('Hyderabad','Hyderabad')
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'class':''}))
    job_city = forms.MultipleChoiceField(label='Prefered Job Location',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields =  ['id','name','dob','gender','locality','city','pincode','state','mobile','email','job_city','profile_image','myfile']
        labels = {'name':'Full Name','dob':'Date of Birth','pin':'Pin Code','mobile':'Mobile No.','profile_image':'Profile Image','myfile':'Attatch Document'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }