from django.core.mail import send_mail


def send_activation_code(activation_code, email):
    full_link = f'http://localhost:8000/v1/api/account/activate/{activation_code}'

    send_mail(
        'Activate your account',
        full_link,
        'ademi.niiazbekkyzy@gmail.com',
        [email, ],
    )
