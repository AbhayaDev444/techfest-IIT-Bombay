from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model


class Message(Model):
    message: str



user = Agent(
    name="user",
    port=8001,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)


fund_agent_if_low(user.wallet.address())


#@user.on_interval(period=20)
#async def send_message(ctx: Context):
#    await ctx.send(RECIPIENT_ADDRESS, Message(message="12,78"))


@user.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    # print(msg.message)
    # lat, long = msg.split(",")[0], msg.split(",")[1]
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    # return lat, long
    await ctx.send(sender, Message(message="12,78"))


if __name__ == "__main__":
    user.run()







