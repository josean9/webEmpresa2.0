from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            content = contact_form.cleaned_data.get('content')
            
            subject = "La Caffetiera: Nuevo mensaje de contacto"
            message = f"De {name} <{email}>\n\nEscribió:\n\n{content}"
            recipient_list = ["6962a3ea86-d2674a+1@inbox.mailtrap.io"]
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                    fail_silently=False,
                )
                return redirect(reverse('contact') + "?ok")
            except BadHeaderError:
                return redirect(reverse('contact') + "?fail")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse('contact') + "?fail")
    
    return render(request, "contact/contact.html", {'form': contact_form})
