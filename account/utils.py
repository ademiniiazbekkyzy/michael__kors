from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    full_link = f'http://localhost:8000/account/activate/{activation_code}'

    send_mail(
        'Activate your account',
        full_link,
        'ademi.niiazbekkyzy@gmail.com',
        [email, ],
        fail_silently=False
    )
