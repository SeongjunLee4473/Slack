import os
import requests
import traceback
from dotenv import load_dotenv

class Notifier:
    """
    A Python utility for sending notifications to Slack channels using a webhook URL.
    This class provides methods to send success messages and error notifications,
    including exception details with tracebacks.

    Last modified: 2025-02-19 / Seongjun Lee / Modified the send_success method to allow for a custom message.
    Created on: 2025-01-19
    Created by: Seongjun Lee
    """
    def __init__(self, env_path):
        """
        Initializes the SlackNotifier with a webhook URL.
        If no URL is provided, it uses the default webhook URL.

        Parameters:
        ----------
        env_path : str
            The path to the .env file.
        """
        # Load environment variables from .env file
        load_dotenv(env_path)
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')

    def send_success(self, message: str = None) -> dict:
        """
        Sends a success notification to the Slack channel.
        This function posts a predefined success message to the configured webhook URL.

        Returns:
        -------
        dict
            A dictionary containing the status of the notification.
            If the Slack response text is "ok", the status will be "success".
            Otherwise, it will be "failure" with the response text included.

        Example Usage:
        --------------
        base_FP = '/YOUR/PATH/TO/BASE/FOLDER'
        import Slack.slack_notifier as Slack
        env_path = os.path.join(base_FP, '.env')
        notipy = Slack.Notifier(env_path)
        notipy.send_success()

        If you want to send a custom message, you can do the following:
        notipy.send_success("The code completed successfully!")
        """
        if message:
            success_message = message
        else:
            success_message = "✅ The code completed successfully! 🚀"
        payload = {"text": success_message}
        response = requests.post(self.webhook_url, json=payload)

        if response.text.strip().lower() == "ok":
            return {"status": "success"}
        else:
            return {"status": "failure", "response": response.text}

    def send_error(self, exception: Exception = None) -> dict:
        """
        Sends an error notification to the Slack channel.
        If an exception is provided, it includes details about the exception,
        including its type, message, and full traceback.

        Parameters:
        ----------
        exception : Exception, optional
            The exception object to include in the error notification (default is None).

        Returns:
        -------
        dict
            A dictionary containing the status of the notification.
            If the Slack response text is "ok", the status will be "success".
            Otherwise, it will be "failure" with the response text included.

        Example Usage:
        --------------
        try:
            # Simulated code that raises an exception
            result = 10 / 0
        except Exception as e:
            notifier = SlackNotifier()
            notifier.send_error(exception=e)
        """
        error_message = "An unexpected error occurred during execution."
        detailed_message = f"❌ *An error occurred!* {error_message}"

        if exception:
            detailed_message += f"\n\n*Exception*: `{type(exception).__name__}`"
            detailed_message += f"\n*Message*: `{exception}`"
            detailed_message += "\n*Traceback:* ```"
            detailed_message += "".join(traceback.format_tb(exception.__traceback__))
            detailed_message += "```"

        payload = {"text": detailed_message}
        response = requests.post(self.webhook_url, json=payload)

        if response.text.strip().lower() == "ok":
            return {"status": "success"}
        else:
            return {"status": "failure", "response": response.text}