from uagents import Agent, Model
from uagents.setup import setup

class WeatherAgent(Agent):
    async def setup(self):
        # Define the message structure for messages to be exchanged between the uAgents
        self.model = Model("weather", {"location": str})

        # Define your agent by providing a name, seed, port, and endpoint
        self.name = "weather_agent"
        self.seed = "weather_seed"
        self.port = 10000
        self.endpoint = "http://localhost:8000"

        # Register your agent in the Almanac contract
        await self.register_almanac(
            endpoints={
                "weather": (self.endpoint, 1)
            },
            seed=self.seed
        )

    async def get_weather_data(self, location):
        # Use the Meteomatics API to retrieve weather data
        url = f"https://api.meteomatics.com/{location}/t_2m:C/json"
        response = await self.http_get(url)
        return response

# Start the agent
setup(WeatherAgent())