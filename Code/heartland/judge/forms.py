from django import forms

#dynamically generates webpages based on inputs
class JudgeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        criteria = kwargs.pop('criteria')
        super(JudgeForm, self).__init__(*args, **kwargs)

        if criteria is not None:
            for crit in criteria:
                self.fields[crit] = forms.fields.IntegerField()
