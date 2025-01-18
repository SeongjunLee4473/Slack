import requests
import traceback

class SlackNotifier:
    """
    A Python library for sending Slack notifications, including standard and error messages,
    with support for sending exception details.
    """

    # Private Webhook URL
    WEBHOOK_URL = "https://hooks.slack.com/services/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"

    def __init__(self, webhook_url: str = WEBHOOK_URL):
        """
        Initializes the SlackNotifier with the provided or default webhook URL.
        Parameters:
        -----------
        webhook_url : str
            The Slack webhook URL to send messages to.
        """
        self.webhook_url = webhook_url

    def send_message(self, message: str) -> dict:
        """
        Sends a standard message to the Slack channel.

        Parameters:
        -----------
        message : str
            The message to send to Slack.

        Returns:
        --------
        dict
            The response from the Slack API.
        """
        payload = {"text": message}
        response = requests.post(self.webhook_url, json=payload)
        return response.json()

    def send_success(self, success_message: str) -> dict:
        """
        Sends a success notification to Slack.

        Parameters:
        -----------
        success_message : str
            The success message to send to Slack.

        Returns:
        --------
        dict
            The response from the Slack API.
        """
        success_payload = {"text": f":white_check_mark: {success_message}"}
        response = requests.post(self.webhook_url, json=success_payload)
        return response.json()

    def send_error(self, error_message: str, exception: Exception = None) -> dict:
        """
        Sends an error notification to Slack, optionally including exception details.

        Parameters:
        -----------
        error_message : str
            The main error message to send to Slack.
        exception : Exception, optional
            The exception object to include details from (default is None).

        Returns:
        --------
        dict
            The response from the Slack API.
        """
        detailed_message = f"*ERROR*: {error_message}"

        # If an exception is provided, include its details and traceback
        if exception:
            detailed_message += f"\n*Exception*: `{type(exception).__name__}`"
            detailed_message += f"\n*Message*: `{exception}`"
            detailed_message += "\n*Traceback:* ```"
            detailed_message += "".join(traceback.format_tb(exception.__traceback__))
            detailed_message += "```"

        error_payload = {"text": detailed_message}
        response = requests.post(self.webhook_url, json=error_payload)
        return response.json()