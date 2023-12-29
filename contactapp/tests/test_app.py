import pytest
from flask_mail import Mail, BadHeaderError

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

            assert outbox[0].subject == "testing"


def test_subject_bad_header(myapp):
     '''
     - Testing whether or not the bad header error will actually work
     - If works, return True in the test
     - Doesn't work, returns as Failed in the test
     '''
     with myapp.app_context():
        mail = Mail(myapp)
        
        with pytest.raises(BadHeaderError) as bad_header: 
            with mail.record_messages() as outbox:
                mail.send_message(subject='testing \n',
                                  body='test',
                                  recipients=['to@example.com'],
                                  sender="from@example.com")
            
        assert True

            
         

