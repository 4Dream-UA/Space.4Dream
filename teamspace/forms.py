from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter"})
    )
