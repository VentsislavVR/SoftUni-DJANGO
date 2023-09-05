from django import forms

from forms_part_2_demo.web.models import Todo
from forms_part_2_demo.web.validators import ValueInRangeValidator, validate_text


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(validate_text,
                    )

    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1,10),
        )
    )

    # def clean_text(self):
    #     pass
    # def clean_priority(self):
    #
    #     # raise ValidationError('ERROR!!!')
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields='__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        '''
        Used for:
        1.Transform data into desired format/form
        2.Validatiion
        :return:
        '''
        return self.cleaned_data['text'].lower()

