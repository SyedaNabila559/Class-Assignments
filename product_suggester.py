class ProductSuggester:
    def __init__(self):
        self.suggestions = {
            "headache": ("Ibuprofen", "It helps relieve headaches by reducing inflammation."),
            "fever": ("Paracetamol", "It reduces fever and provides relief."),
            "cold": ("Antihistamine", "It helps relieve cold symptoms like sneezing and runny nose."),
            "stomach ache": ("Antacid", "It neutralizes stomach acid and eases discomfort."),
        }

    def suggest_product(self, user_input: str) -> str:
        for keyword, (product, reason) in self.suggestions.items():
            if keyword in user_input.lower():
                return f"I suggest you try **{product}**. {reason}"
        return "Sorry, I couldn't find a suitable product for your need."


if __name__ == "__main__":
    agent = ProductSuggester()
    query = input("Describe your symptom: ")
    print(agent.suggest_product(query))