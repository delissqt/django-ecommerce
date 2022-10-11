from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'feature',
        ]


class RawProductForm(forms.Form):

    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "placeholder": "Title place holder"
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "id-for-textarea",
                "rows": "50",
                "cols": "60",
                "placeholder": "description is here"
            }
    ))
    # price = forms.DecimalField()
    price = forms.DecimalField(initial=199.99)
