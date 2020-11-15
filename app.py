import sys

# Load the local source directly
sys.path.insert(1, "./python-slack-sdk")

# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient

slack_token = "xoxb-1501480777732-1519169041296-qNTdPCnS8UmOLIpKugODwTdM"
client = WebClient(token=slack_token)

try:
    api_response = client.chat_postMessage(
        channel="random",
        text="Hello from your app! :tada:"
    )
except SlackApiError as e:
    assert e.response["error"]
