

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def submit_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Process the form data here (e.g., send email)
            send_mail(
                subject,
                message,
                'your-email@example.com',  # Replace with your email
                [email],
                fail_silently=False,
            )

            return render(request, 'api/submitform.html')
    else:
        form = ContactForm()

    return render(request, 'api/submit_form.html', {'form': form})

        
def send_test_email(request):
    if request.method == 'POST':
        subject = 'Test Email Subject'
        message = 'This is a test email message.'
        from_email = 'your-email@example.com'
        recipient_list = ['recipient@example.com']

        send_mail(subject, message, from_email, recipient_list)
        message = "Email sent successfully"

        return render(request, 'api/email_test.html', {'message': message})
    else:
        return render(request, 'api/email_test.html')