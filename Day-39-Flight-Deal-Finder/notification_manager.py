import smtplib
from settings_vault import Settings
from data_manager import DataManager


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        # Initialize NotificationManager with email credentials and server details
        self.credentials = Settings()
        self.sender_email = self.credentials.send_email
        self.send_password = self.credentials.send_password
        self.recipient_email = DataManager()
        self.smtp_server = self.credentials.smtp_server
        self.smtp_port = self.credentials.smtp_port

    def send_email(self, data):
        """
        Send an email notification with flight details to recipients.
        :param data: Flight details dictionary.
        """
        sender_email = self.sender_email
        sender_password = self.send_password
        recipient_email = self.recipient_email.import_members()
        smtp_server = self.smtp_server
        smtp_port = self.smtp_port

        # Iterate through each recipient and send personalized email
        for member in recipient_email['users']:
            header = f"Low Price Alert ✈️: {data['depart_city_from']}-{data['depart_fly_from']} to {data['depart_city_to']}-{data['depart_fly_to']}"
            with smtplib.SMTP(host=smtp_server, port=smtp_port) as connection:
                connection.starttls()
                connection.login(user=sender_email, password=sender_password)

                # Check for layover information in flight details
                if 'layover_city' in data:
                    connection.sendmail(
                        from_addr=sender_email,
                        to_addrs=member['email'],
                        msg=f"Subject:{header}"
                            f"\n\nFlight Details:\n{data['depart_city_from']}-{data['depart_fly_from']} to {data['depart_city_to']}-{data['depart_fly_to']}\n"
                            f"Depart On: {data['depart_local_departure']}\n"
                            f"Return On: {data['depart_local_arrival']}\n"
                            f"Total Nights: {data['nights_in_dest']} \n"
                            f"Cost: {data['price']} \n"
                            f"Flight has 1 stopover, via {data['layover_city']}. \n"
                            f"Book via {data['booking_link']}.".encode('utf8')
                    )
                else:
                    connection.sendmail(
                        from_addr=sender_email,
                        to_addrs=member['email'],
                        msg=f"Subject:{header}"
                            f"\n\nFlight Details:\n{data['depart_city_from']}-{data['depart_fly_from']} to {data['depart_city_to']}-{data['depart_fly_to']}\n"
                            f"Depart On: {data['depart_local_departure']}\n"
                            f"Return On: {data['depart_local_arrival']}\n"
                            f"Total Nights: {data['nights_in_dest']} \n"
                            f"Cost: {data['price']} \n"
                            f"Book via {data['booking_link']}.".encode('utf8')
                    )
