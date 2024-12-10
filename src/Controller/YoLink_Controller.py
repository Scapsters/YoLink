import requests
import json
from datetime import datetime

from Interfaces.Device import Device

from Interfaces.BUDPResponses import BUDPResponse, MethodNames, get_response_type
from Interfaces.Device import Device

TOKEN_URL = 'https://api.yosmart.com/open/yolink/token'
API_URL = 'https://api.yosmart.com/open/yolink/v2/api'
NO_DEVICE = "No Device"

class YoLinkController:
	"""
	A controller for the YoLink API. Handles requests to the API and manages access tokens.
 
	Methods:
		establish_access_token: Establishes an access token for the YoLink API. If a token already exists, it will be refreshed if it is expired.
		create_tokens: Creates access and refresh tokens from the YoLink API. Updates the controller's token variables.
		make_request: Makes a request to the YoLink API with the given parameters. Returns the data from the response.
		get_timestamp: Returns the current timestamp
   
	Attributes:
		user_id (str): The user ID for the YoLink API.
		user_key (str): The user key for the YoLink API.
		access_token (str): The access token for the YoLink API.
		refresh_token (str): The refresh token for the YoLink API.
		token_expiration_time (int): The time at which the access token will expire.
	"""
	def __init__(self):
		"""
		Initialize a YoLink API Controller. Also attempts to establish an access token.
		"""
		# Load credentials 
		with open("./credentials.json", "r") as file:
			credentials = json.load(file)
		self.user_id = credentials["user_id"]
		self.user_key = credentials["user_key"]
		
		# Initialize token information
		self.access_token = None
		self.refresh_token = None
		self.token_expiration_time = None
		
		# Attempt to establish access token
		self.establish_access_token()

	def establish_access_token(self) -> None:
		"""
		Establishes an access token for the YoLink API. If a token already exists, it will be refreshed if it is expired.
		"""
		current_time = self.get_timestamp()
		
		# If token exists but is expired, refresh it
		if self.token_expiration_time is not None and current_time > self.token_expiration_time:
			self.create_tokens(data = {
				"grant_type": "refresh_token",
				"client_id": self.user_id,
				"refresh_token": self.refresh_token
			})
			
		# Otherwise create token normally
		self.create_tokens(data = {
			"grant_type": "client_credentials",
			"client_id": self.user_id,
			"client_secret": self.user_key
		})

	def create_tokens(self, data: dict) -> None:
		"""
		Creates access and refresh tokens from the YoLink API. Updates the controller's token variables.

		Args:
			data (dict): The data to be sent in the request to the YoLink API.
		"""
		# Make request
		response = requests.post(TOKEN_URL, data=data).json()
		
		# Update token variables
		self.access_token = response["access_token"]
		self.refresh_token = response["refresh_token"]
		self.token_expiration_time = response["expires_in"] + self.get_timestamp()
	
	# Follows BDDP property list at http://doc.yosmart.com/docs/protocol/datapacket/#BDDP
	def make_request(self, method_name: MethodNames, msgid: str | None = None, device: Device | None = None, params = None) -> BUDPResponse:
		"""
		Makes a request to the YoLink API with the given parameters. Returns the data from the response.

		Args:
			method_name     (str):                Target function (Defined in YoLink API Documentation).
			msgid           (str, optional):   	  Message ID. Defaults to None and the API will generate one.
			target_device   (Device, optional):   The Device. Used for deviceID and Token
			params 			(_type_, optional):   Parameters. Required when specified by the method.

		Raises:
			ConnectionError: There was an error connecting to the YoLink API. The error message will specify the error code.

		Returns:
			BUDPResponse: An object representing the data from the response.
		"""
		# Setup data
		headers = {
			"Content-Type": "application/json",
			"Authorization": f'Bearer {self.access_token}'
		}
		data = json.dumps({
			"method": method_name.value,
			"time": self.get_timestamp(),
			"msgid": msgid,
			"targetDevice": device.deviceId if device else None,
			"token": device.token if device else None,
			"params": params
		})
		
		# Make and return data from request unless there is an error
		ResponseType = get_response_type(device.type if device else NO_DEVICE, method_name)
		response = BUDPResponse(requests.post(API_URL, headers=headers, data=data).json(), ResponseType)
		if response.code != "000000":
			raise ConnectionError(f'code {response["code"]}')
		return response

	def get_timestamp(self) -> int:
		return int(datetime.now().timestamp())
  
