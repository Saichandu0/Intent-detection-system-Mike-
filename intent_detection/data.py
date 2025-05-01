import os

# Recreate the 'data' folder if not already present
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Categorized speech examples to create in data files
speech_examples = {
    "greetings.txt": [
        "hello", "hi there", "good morning", "good evening", "how are you", "what's up"
    ],
    "general_knowledge.txt": [
        "who is the president of the united states", "tell me a fact", "how far is the moon",
        "what is quantum computing", "define artificial intelligence"
    ],
    "web_search.txt": [
        "search for pizza near me", "look up the weather", "google openai", 
        "find me python tutorials", "search the capital of France"
    ],
    "music_search.txt": [
        "play some music", "play lofi beats", "start a playlist", "open spotify", "play rock songs"
    ],
    "person_lookup.txt": [
        "find Elon Musk", "look up Joe Biden", "who is Sundar Pichai", 
        "search for Mark Zuckerberg", "locate Tom Holland"
    ]
}

# Write the examples into their respective .txt files
for filename, examples in speech_examples.items():
    with open(os.path.join(data_dir, filename), "w") as file:
        file.write("\n".join(examples))

# Return confirmation of created files
os.listdir(data_dir)
