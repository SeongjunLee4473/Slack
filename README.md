<div align="center">
  <div style="display: inline-block;">
    <img style="max-width:100%; display: block;"
      src="https://d34u8crftukxnk.cloudfront.net/slackpress/prod/sites/6/slack-logo-slide.png"
      alt="Slack"/>
  </div>
</div>

---

# 🔔 Slack
A centralized repository for **`Slack`**-related development, including bots, custom integrations, automation scripts, and webhook implementations. This repository contains reusable code and tools for enhancing **`Slack`** workflows.

---

# 📩 Slack Notifier
A simple Python utility for sending notifications to a Slack channel using an Incoming Webhook URL. This class is designed to make it easy to monitor the status of your scripts, providing methods to send both success and detailed error messages.

---

## Features
* 🧩 **Easy Integration**: Simple to drop into any Python project.
* ✅ **Success Notifications**: Send a confirmation message when a script or task completes successfully. You can use a default message or provide a custom one.
* 🐛 **Detailed Error Reporting**: Automatically capture and send detailed error information, including the exception type, message, and a full traceback, making debugging easier.
* 🔒 **Secure Configuration**: Keeps your Slack webhook URL secure by loading it from a .env file.

---

## Setup
### 1. Prerequisites
Ensure you have the required Python libraries installed. You can install them using pip:

```python
pip install requests python-dotenv
```

### 2. Configuration
Create a `.env` file in the root directory of your project. This file will store your Slack webhook URL securely.
1. Create a file named .env.
2. Add your Slack webhook URL to the file like this:

```python
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

---

## Usage
### Initialization
First, import the `Notifier` class and create an instance by providing the path to your `.env` file.

```python
import os
from slack_notifier import Notifier

# Define the path to your .env file
env_path = '/path/to/your/project/.env'

# Create an instance of the notifier
notifier = Notifier(env_path)
```

### Sending a Success Notification
You can send a notification to confirm that your script has run successfully.

```python
# Send the default success message
notifier.send_success()

# Or, send a custom success message
notifier.send_success("Daily report generation complete!")
```

### Sending an Error Notification
To automatically send error details upon failure, use a `try...except` block. Pass the exception object to the `send_error` method.

```python
try:
    # This is where your code that might fail goes
    result = 10 / 0
except Exception as e:
    # Send a detailed error report to Slack
    notifier.send_error(exception=e)
```

---

## Class and Method Reference
### `Notifier` Class
This is the main class that handles the notifications.

### `__init__(self, env_path)`
The constructor initializes the notifier. It loads the `SLACK_WEBHOOK_URL` from the specified `.env` file.

#### Parameters
* `env_path` (str): The file path to your `.env` file containing the `SLACK_WEBHOOK_URL`.

### `send_success(self, message: str = None)`
Sends a success message to the configured Slack channel.

#### Parameters
* `message` (str, optional): A custom message to send. If not provided, a default message ("✅ The code completed successfully! 🚀") will be used.

#### Returns
* `dict`: A dictionary containing the status of the request (e.g., `{"status": "success"}`).

### `send_error(self, exception: Exception = None)`
Sends a detailed error notification to the Slack channel, including the exception type, message, and traceback.

#### Parameters
* `exception` (Exception, optional): The exception object caught during execution. This is used to generate the detailed error report.

#### Returns
* `dict`: A dictionary containing the status of the request (e.g., `{"status": "success"}`).

---

Author & Developed by: [Seongjun Lee](mailto:seongjunlee4473@gmail.com?subject=Questions%20for%20GitHub%20projects) @ Jan 2025

---

