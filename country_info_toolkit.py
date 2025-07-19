class CapitalTool:
    def __init__(self):
        self.capitals = {
            "france": "Paris",
            "germany": "Berlin",
            "japan": "Tokyo",
            "india": "New Delhi"
        }

    def get_capital(self, country: str) -> str:
        return self.capitals.get(country.lower(), "Unknown")

class LanguageTool:
    def __init__(self):
        self.languages = {
            "france": "French",
            "germany": "German",
            "japan": "Japanese",
            "india": "Hindi"
        }

    def get_language(self, country: str) -> str:
        return self.languages.get(country.lower(), "Unknown")

class PopulationTool:
    def __init__(self):
        self.populations = {
            "france": "67 million",
            "germany": "83 million",
            "japan": "125 million",
            "india": "1.4 billion"
        }

    def get_population(self, country: str) -> str:
        return self.populations.get(country.lower(), "Unknown")

class CountryInfoOrchestrator:
    def __init__(self):
        self.capital_tool = CapitalTool()
        self.language_tool = LanguageTool()
        self.population_tool = PopulationTool()

    def get_country_info(self, country: str) -> str:
        capital = self.capital_tool.get_capital(country)
        language = self.language_tool.get_language(country)
        population = self.population_tool.get_population(country)

        return (
            f"📌 Information for {country.title()}:\n"
            f"- Capital: {capital}\n"
            f"- Language: {language}\n"
            f"- Population: {population}"
        )


if __name__ == "__main__":
    orchestrator = CountryInfoOrchestrator()
    country_name = input("Enter a country name: ")
    print(orchestrator.get_country_info(country_name))
