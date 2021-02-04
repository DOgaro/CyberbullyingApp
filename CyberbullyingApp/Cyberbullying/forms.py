from django import forms

class Cyberbullying_Typed_Tweet_analyse_form(forms.Form):
    Cyberbullying_typed_tweet = forms.CharField(initial='nothing')

class Cyberbullying_Imported_Tweet_analyse_form(forms.Form):
    Cyberbullying_imported_tweet = forms.CharField(initial='nothing')
