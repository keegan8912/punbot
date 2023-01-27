from twitchio.ext import commands
import twitchio, requests, json

with open("params.json") as f:
    params = json.load(f)

channel_name = params["params"]["channel_name"]
bot_account = params["params"]["bot_account"]
oauth_token = params["params"]["oauth_token"]
client_id = params["params"]["client_id"]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=oauth_token,
            client_id=client_id,
            nick=bot_account,
            prefix="!",
            initial_channels=[channel_name],
        )

    async def event_ready(self):
        print(f"Ready | {self.nick}")

    async def event_message(self, ctx):
        "Runs every time a message is sent in chat."
        # make sure the bot ignores itself and the streamer
        print(ctx.author)
        if ctx.author is None or ctx.author._name.lower() == bot_account.lower():
            return
        await bot.handle_commands(ctx)

    async def event_command_error(self, ctx, error):
        print("Caught exception, skipping")
        pass

    @commands.command(name="pun")
    async def test(self, ctx):
        pun = self.get_pun()
        await ctx.send(pun)

    def get_pun(self):
        pun_gen_url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=political,racist,sexist&type=single"
        request = requests.get(pun_gen_url)
        pun = request.json()["joke"]
        if len(pun) <= 1:
            _str = "Could not fetch pun, please try later"
            return _str
        else:
            return pun


if __name__ == "__main__":
    bot = Bot()
    bot.run()
