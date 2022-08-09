from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="value 1",required=False,widget=forms.Textarea(attrs={'class':"form.control"}))
    num2=forms.CharField(label="value 2",required=False,widget=forms.Textarea(attrs={'class':"form.control"}))
    num3=forms.CharField(label="value 3",required=False,widget=forms.Textarea(attrs={'class':"form.control"}))
