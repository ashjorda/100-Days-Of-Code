class Settings:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.kiwi_api_key = ''
        self.send_email = ''  # smtp login
        self.send_password = ''  # smtp password
        self.recipient_email = ''  # recipient email
        self.smtp_server = 'smtp.gmail.com'  # gmail smtp server or your email smtp server url
        self.smtp_port = '587'  # currently set to googles secure smtp port
