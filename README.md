# Agentic-SDk-Assignments

This mini-suite contains 3 smart agents:

| 🧠 Module Name              | 📄 File Name              | 🔍 Description |
|----------------------------|---------------------------|----------------|
| Smart Store Agent          | `product_suggester.py`    | Suggests a product based on user symptoms |
| Mood Analyzer with Handoff | `mood_handoff.py`         | Detects user mood and hands off to another agent for activity suggestions |
| Country Info Bot (Tools)   | `country_info_toolkit.py` | Uses tool agents to get capital, language, and population |


## 🧪 1. Smart Store Agent

📁 **File:** `product_suggester.py` 

🎯 **Goal:** Suggest a product based on user need.

### ✨ How It Works:
- Accepts a user symptom (e.g., "I have a headache")
 
- Matches it to a product and explains the reason

### 🧠 Example:

> Input: I have a headache

> Output: I suggest you try Ibuprofen. It helps relieve headaches by reducing inflammation.

# ▶️ Run It:

python product_suggester.py

## 😔 2. Mood Analyzer with Handoff

📁 **File:** mood_handoff.py

🎯 **Goal:** Detects user mood → suggests helpful activity if mood is sad or stressed.

### ✨ How It Works:

Agent 1: Detects mood (happy, sad, stressed)

Agent 2: Suggests an activity if needed

Managed by a Runner class

### 🧠 Example:

> Input: I'm feeling stressed lately
 
> Output:

  Detected mood: stressed
  
  Suggested activity: Try meditation, deep breathing, or taking a short break.

# ▶️ Run It:

python mood_handoff.py

## 🌍 3. Country Info Bot (Tool-Based)

📁 **File:** country_info_toolkit.py

🎯 **Goal:**  Provide country info using tool agents.

### ✨ How It Works:

🏙️ CapitalTool: Provides capital

🗣️ LanguageTool: Provides official language

👥 PopulationTool: Provides population data

### 🧠 Example:

> Input: Japan

> Output:

  📌 Information for Japan:
  
  - Capital: Tokyo

  - Language: Japanese
 
  - Population: 125 million


# ▶️ Run It:

python country_info_toolkit.py

# 🚀 Getting Started

✅ No external libraries needed.

💡 Works with Python 3.6+

# ✅ To Run All Scripts:

 product_suggester.py
 
mood_handoff.py

country_info_toolkit.py

# ✨ Features

💊 Smart product suggestions

😃 Mood-aware recommendations

🌎 Tool-based country info

🔄 Modular and extensible design

🧠 Pure Python implementation (easy to upgrade to ML)




