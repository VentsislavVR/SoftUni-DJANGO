import os

from django import forms

from expenses_tracker.web.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget',
                  'first_name',
                  'last_name',
                  'image')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget',
                  'first_name',
                  'last_name',
                  'image')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        if commit:
            self.instance.delete()
            os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price')


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            field.widget.attrs['readonly'] = 'readonly'
    class Meta:
        model = Expense
        fields = ('title',
                  'description',
                  'expense_image',
                  'price')
