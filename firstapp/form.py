from django import forms
# select_value =( 
#     ("0", "Select Option"), 
#     ("1", "One"), 
#     ("2", "Two"), 
#     ("3", "Three"), 
#     ("4", "Four"), 
#     ("5", "Five"), 
# )
# select=(('M',"M"),
#         ('L','L'),
#         ('S','S'),
#         )
   
# class contactForm(forms.Form):
#     name = forms.CharField(label='Your Name',required=True,max_length=100, help_text="100 characters max.", error_messages={'required':'Please Enter your name'})
#     email = forms.EmailField(label='Your Email',widget=forms.DateInput(attrs={'id':"email"}))
#     field_name = forms.ChoiceField(choices = select_value)
#     date = forms.DateTimeField(widget=forms.DateInput(attrs= {'type' : 'date'}))
#     size = forms.ChoiceField(choices=select, widget = forms.RadioSelect)
#     multisize = forms.MultipleChoiceField(choices=select,widget=forms.CheckboxSelectMultiple)
#     file = forms.FileField()
   
   
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    def clean_name(self):
        vallen = self.cleaned_data['name']
        if len(vallen) < 5:
            print(len(vallen))
            raise forms.ValidationError('Enter name allist 5 char')
        return vallen
        