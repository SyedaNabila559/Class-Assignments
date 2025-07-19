class MoodAnalyzer:
    def __init__(self):
        self.mood_keywords = {
            "sad": ["sad", "unhappy", "depressed"],
            "stressed": ["stressed", "anxious", "overwhelmed"],
            "happy": ["happy", "excited", "joyful"],
        }

    def analyze_mood(self, message: str) -> str:
        msg = message.lower()
        for mood, keywords in self.mood_keywords.items():
            if any(word in msg for word in keywords):
                return mood
        return "neutral"

class ActivitySuggester:
    def __init__(self):
        self.activities = {
            "sad": "Try going for a walk, listening to music, or talking to a friend.",
            "stressed": "Try meditation, deep breathing, or taking a short break.",
        }

    def suggest_activity(self, mood: str) -> str:
        return self.activities.get(mood, "No suggestion available for this mood.")

class Runner:
    def __init__(self):
        self.mood_agent = MoodAnalyzer()
        self.activity_agent = ActivitySuggester()

    def run(self, message: str):
        mood = self.mood_agent.analyze_mood(message)
        print(f"Detected mood: {mood}")

        if mood in ["sad", "stressed"]:
            suggestion = self.activity_agent.suggest_activity(mood)
            print(f"Suggested activity: {suggestion}")
        else:
            print("You're doing fine! Keep it up!")


if __name__ == "__main__":
    runner = Runner()
    user_message = input("How are you feeling today? ")
    runner.run(user_message)