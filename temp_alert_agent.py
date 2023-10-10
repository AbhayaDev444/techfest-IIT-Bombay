from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low


class Message(Model):
    message: str


RECIPIENT_ADDRESS = "agent1q2kxet3vh0scsf0sm7y2erzz33cve6tv5uk63x64upw5g68kr0chkv7hw50"

temp_alert_agent = Agent(
    name="temp_alert_agent",
    port=8020,
    seed="temp_alert_agent secret phrase",
    endpoint=["http://127.0.0.1:8020/submit"],
)

fund_agent_if_low(temp_alert_agent.wallet.address())

import requests



@temp_alert_agent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    #print(msg.message)
    #lat, long = msg.split(",")[0], msg.split(",")[1]
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    #return lat, long

@temp_alert_agent.on_message(model=Message)
async def send_message(ctx: Context):
    lati, longi = 13, 78  #await message_handler(Context, str, Message)
    max = 25
    min = 20

    url = (str(f"https://api.open-meteo.com/v1/forecast?latitude=") + str(lati) + str("&longitude=") + str(longi) + str("&hourly=temperature_2m"))
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_list = data["hourly"]["temperature_2m"]
        for i in temp_list:
            if i < min or i > max:
                await ctx.send(RECIPIENT_ADDRESS, Message(message=f"The current temperature is {i} degrees Celsius."))
            else:
                await ctx.send(RECIPIENT_ADDRESS,Message(message="No drastic temperature change"))
    else:
        await ctx.send(RECIPIENT_ADDRESS, Message(message="Error: Unable to retrieve data from the API."))


if __name__ == "__main__":
    temp_alert_agent.run()
