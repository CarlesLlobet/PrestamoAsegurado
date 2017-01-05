from .forms import *

class formAsnef(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formAsnef, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(formAsnef, self).clean()
