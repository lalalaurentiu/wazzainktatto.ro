from django import forms
from home.models import ClientRezervation

class ClientRezervationForm(forms.ModelForm):
    name = forms.CharField(label="Nume")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Telefon")
    date = forms.DateTimeField(label="Data", input_formats=['%d %m, %Y %H:%M'])
    description = forms.CharField(label="Introduceti o scurta descriere despre tatuaj...", widget=forms.Textarea, required=False)
    image = forms.ImageField(label="Incarca o imagine", required=False)

    name.widget.attrs.update({
        "class":"""
                block
                w-full
                px-5
                py-3
                text-base text-neutral-600
                placeholder-gray-300
                transition
                duration-500
                ease-in-out
                transform
                border border-transparent
                rounded-lg
                bg-gray-50
                focus:outline-none
                focus:border-transparent
                focus:ring-2
                focus:ring-white
                focus:ring-offset-2
                focus:ring-offset-red-300
                """,
        "placeholder":"Introduceti numele"
    })

    email.widget.attrs.update({
        "class":"""
                block
                w-full
                px-5
                py-3
                text-base text-neutral-600
                placeholder-gray-300
                transition
                duration-500
                ease-in-out
                transform
                border border-transparent
                rounded-lg
                bg-gray-50
                focus:outline-none
                focus:border-transparent
                focus:ring-2
                focus:ring-white
                focus:ring-offset-2
                focus:ring-offset-red-300
                """,
        "placeholder":"Introduceti email"
    })

    phone.widget.attrs.update({
        "class":"""
                block
                w-full
                px-5
                py-3
                text-base text-neutral-600
                placeholder-gray-300
                transition
                duration-500
                ease-in-out
                transform
                border border-transparent
                rounded-lg
                bg-gray-50
                focus:outline-none
                focus:border-transparent
                focus:ring-2
                focus:ring-white
                focus:ring-offset-2
                focus:ring-offset-red-300
                """,
        "placeholder":"Introduceti numarul de telefon"
    })

    date.widget.attrs.update({
        "class":"""
                block
                w-full
                px-5
                py-3
                text-base text-neutral-600
                placeholder-gray-300
                transition
                duration-500
                ease-in-out
                transform
                border border-transparent
                rounded-lg
                bg-gray-50
                focus:outline-none
                focus:border-transparent
                focus:ring-2
                focus:ring-white
                focus:ring-offset-2
                focus:ring-offset-red-300
                """,
        "placeholder":"Selectati data",
        "id":"datetime",
        "data-input": None,
    })

    description.widget.attrs.update({
        "class":"""block
            w-full
            px-5
            py-3
            mt-2
            text-base text-neutral-600
            placeholder-gray-300
            transition
            duration-500
            ease-in-out
            transform
            border border-transparent
            rounded-lg
            bg-gray-50
            focus:outline-none
            focus:border-transparent
            focus:ring-2
            focus:ring-white
            focus:ring-offset-2
            focus:ring-offset-red-300
            apearance-none
            autoexpand""",
        "placeholder":"Observatii",
        "rows":"2"
    })

    image.widget.attrs.update({
        "class":"""
                block
              w-full
              px-5
              py-3
              text-base text-neutral-600
              placeholder-gray-300
              transition
              duration-500
              ease-in-out
              transform
              border border-transparent
              rounded-lg
              bg-gray-50
              focus:outline-none
              focus:border-transparent
              focus:ring-2
              focus:ring-white
              focus:ring-offset-2
              focus:ring-offset-red-300
                """
    })

    class Meta:
        model = ClientRezervation
        fields = ["name", "email", "phone", "date", "description", "image"]