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

#fund_agent_if_low(user.wallet.address())


@user.on_interval(period = 300)
async def message_handler(ctx: Context, sender: str, msg: Message):
    await ctx.send(sender, Message(message="12,78"))
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


if __name__ == "__main__":
    user.run()
