from django import forms
from .models import Review
from django.forms import ModelForm



class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Write your review here:",
                             widget=forms.Textarea(attrs={'class':'myform'}))
    


class ReviewForm2(ModelForm):
    class Meta:
        model = Review
        fields =  "__all__" # same as defining all fields:  ['first_name','last_name','stars']

#to give the label tags a different name, create a "labels" dictionary. 
        labels = {"first_name":"FIRST NAME",
                      "last_name":"LAST NAME",
                      "stars":"RATING"}
#to give specific error messages for each validator & field in the form. 
        error_messages = {
            "stars":{
                "min_value":"Hey! Min value is 1 !!",
                "max_value":"Hey! Max value is 5 !!"
            }
        }
