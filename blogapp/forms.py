from django import forms
from .models import Post,Category
#linking the cat Model to out add post M
choices  = Category.objects.all().values_list("name","name")
choices_list =[]
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','author','category','body','pic')

        widgets={
            'title': forms.TextInput(attrs={'class':'inputForm','placeholder':' Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'inputForm tag','type':'hidden'}),
            'author': forms.TextInput(attrs={'class':' userId','value':'','type':'hidden'}),
            'category': forms.Select(choices=choices_list,attrs={'class':'inputForm'}),
            'body': forms.Textarea(attrs={'class':'bodyText','placeholder':' Write your Article here'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','category','body','pic')

        widgets={
            'title': forms.TextInput(attrs={'class':'inputForm'}),
            'category': forms.Select(choices=choices_list,attrs={'class':'inputForm'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'input your article here'}),
        }