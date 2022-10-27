from django import forms

class FormularioPersonal(forms.Form):

    OPCIONES=(
        (1,'Chef'),
        (2,'SubChef'),
        (3,'Mesero')
    )

    nombre=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=30
    )

    identificacion=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=20
    )

    descrpcion=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5
    )

    tipoCargo=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )