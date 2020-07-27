from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add New Task...'}))
    class Meta:
        model = Task
        fields = '__all__'

    # def clean(self): 
  
    #     # data from the form is fetched using super function 
    #     super(TaskForm, self).clean() 
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add New Task...'}))

    class Meta:
        model = Task
        fields = ['title', 'completed']