from uagents import Agent, Bureau, Context, Model
from uagents.setup import fund_agent_if_low


class Message(Model):
    message: str




alice = Agent(
    name="alice",
    seed="alice secret phrase",
)

fund_agent_if_low(alice.wallet.address())


@alice.on_interval(period=2.0)
async def send_message(ctx: Context):
    await ctx.send(bob.address, Message(message="hello there bob"))


@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


bureau = Bureau()
bureau.add(alice)
if __name__ == "__main__":
    bureau.run()