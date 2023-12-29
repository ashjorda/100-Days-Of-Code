class Settings:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        # Initialize Settings with default values (empty strings) and configuration details
        self.kiwi_api_key = ''  # API key for the Kiwi Flight Search API
        self.flight_destinations = ''  # Sheetly API URL for "prices" tab in the Google sheet
        self.email_list = ''  # Sheetly API URL for "users" tab in the Google sheet
        self.send_email = ''  # user@gmail.com
        self.send_password = ''  # SMTP server password
        self.smtp_server = 'smtp.gmail.com'  # SMTP server URL (default is Gmail)
        self.smtp_port = '587'  # SMTP port for secure communication (default for Gmail)
