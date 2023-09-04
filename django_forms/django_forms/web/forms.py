from django import forms


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )
    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter name',
                'class':'form-control',
            }
        )
    )
    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text='Enter your age',
    )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect
    )

    occupancy2 = forms.ChoiceField(
        choices=OCCUPANCIES,
    )