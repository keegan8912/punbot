# punbot
Bot for twitch to fetch and show puns in chat.

To run this, simply place the _params.json_ file in the directory with the executable.
The file should consist of the following parameters:

```javascript
{
	"params":{
		"channel_name":"<Channel Name>",
		"bot_account":"<Bot account name>",
		"oauth_token":"oauth:<Auth Token>",
		"client_id":"<Client ID>",
		}
}
```

To find the _oauth\_token_, visit the website: <https://twitchapps.com/tmi/> and link your twitch account. The client ID can be found by visiting <https://dev.twitch.tv/console/apps> and registering the application with a local host url.
