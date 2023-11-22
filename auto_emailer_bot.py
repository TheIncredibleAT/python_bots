import requests

MAILGUN_API_ENDPOINT = ""
MAILGUN_API_KEY = ''

def send_email(to, subject, body):

    # create a dictionary witht the data
    data = {
        'from': '',
        'to': to,
        'subject': subject,
        'text': body
    }

    # send a POST request to the Mailgun API endpoint
    response = requests.post (
        MAILGUN_API_ENDPOINT,
        auth=('api', MAILGUN_API_KEY),
        data=data
    )

    # check if the request was successful
    if response.status_code == 200:
        print('Email sent Successfully!')
    else:
        print('An error occured while sending the email.')

# Ex
to = ""
subject = 'test'
body = 'This definitely works, wow!'
send_email(to, subject, body)