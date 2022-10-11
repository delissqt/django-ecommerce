from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
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
                "rows": "5",
                "cols": "6",
                "placeholder": "description is here"
            }
        ))
    price = forms.DecimalField(initial=199.99)

    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            # 'summary',
            # 'feature',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")

        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email



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
    price = forms.DecimalField(initial=199.99)
