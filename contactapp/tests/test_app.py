from flask_mail import Mail

def test_myapp(myapp):
    '''
    - Testing Emails with flask_mail
    '''
    with myapp.app_context():
        mail = Mail(myapp)

        with mail.record_messages() as outbox:
            mail.send_message(subject='testing',
                              body='test',
                              recipients=['to@example.com'],
                              sender="from@example.com")

            assert len(outbox) == 1
            assert outbox[0].subject == "testing"


