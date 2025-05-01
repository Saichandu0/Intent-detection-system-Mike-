training_sentences = [
    # Greetings and conversational
    "hello", "hi", "good morning", "good evening", "hey", "how are you",
    "what's up", "how's it going", "how are you doing", "what are you doing",
    "what can you do", "tell me about yourself", "introduce yourself",
    "what are your capabilities", "what do you do", "what are your features",
    "how do you work", "what can you help me with", "what are your skills",
    "are you busy", "are you free", "are you working", "what's new",
    
    # General knowledge
    "who is the president", "tell me a fact", "what is quantum computing", "define artificial intelligence",
    "how far is the moon", "when was google founded", "what is the capital of japan",
    "what is the weather like", "what's the weather", "is it raining", "will it rain today",
    "what's the temperature", "how's the weather outside", "do I need an umbrella",
    
    # Web search
    "search for pizza near me", "look up the weather", "google openai", "find me python tutorials",
    "search the capital of France", "show me news about ai", "where is mars located",
    "find restaurants nearby", "search for hotels", "look up movie times", "find flights",
    "search for recipes", "find local events", "search for jobs", "look up directions",
    
    # Music
    "play some music", "play lofi beats", "start a playlist", "open spotify", "play rock songs",
    "I want to hear music", "can you play a song", "let's listen to music",
    "play jazz music", "play classical music", "play pop songs", "play hip hop",
    "play workout music", "play relaxing music", "play party music", "play country music",
    
    # Person lookup
    "find Elon Musk", "look up Joe Biden", "who is Sundar Pichai", "search for Mark Zuckerberg",
    "locate Tom Holland", "find Taylor Swift", "who is the ceo of apple",
    "who is bill gates", "find jeff bezos", "look up steve jobs", "who is tim cook",
    "find oprah winfrey", "who is warren buffett", "search for elon musk",
    
    # Time
    "what time is it", "tell me the time", "current time please", "give me the time", "what's the time",
    "what's the current time", "can you tell me the time", "do you know what time it is",
    "what time is it now", "time please", "what's the clock say", "what time do we have",
    "could you tell me the time", "what's the exact time", "what time is it right now"
]

training_labels = [
    # Greetings and conversational
    "greetings", "greetings", "greetings", "greetings", "greetings", "greetings",
    "greetings", "greetings", "greetings", "greetings", "capabilities", "capabilities",
    "capabilities", "capabilities", "capabilities", "capabilities", "capabilities",
    "capabilities", "capabilities", "greetings", "greetings", "greetings", "greetings",
    
    # General knowledge
    "general_knowledge", "general_knowledge", "general_knowledge", "general_knowledge",
    "general_knowledge", "general_knowledge", "general_knowledge", "weather_query",
    "weather_query", "weather_query", "weather_query", "weather_query", "weather_query",
    "weather_query",
    
    # Web search
    "web_search", "web_search", "web_search", "web_search", "web_search", "web_search", "web_search",
    "web_search", "web_search", "web_search", "web_search", "web_search", "web_search",
    "web_search", "web_search",
    
    # Music
    "music_search", "music_search", "music_search", "music_search", "music_search",
    "music_search", "music_search", "music_search", "music_search", "music_search",
    "music_search", "music_search", "music_search", "music_search", "music_search",
    "music_search",
    
    # Person lookup
    "person_lookup", "person_lookup", "person_lookup", "person_lookup",
    "person_lookup", "person_lookup", "person_lookup", "person_lookup",
    "person_lookup", "person_lookup", "person_lookup", "person_lookup",
    "person_lookup", "person_lookup", "person_lookup",
    
    # Time
    "get_time", "get_time", "get_time", "get_time", "get_time", "get_time",
    "get_time", "get_time", "get_time", "get_time", "get_time", "get_time",
    "get_time", "get_time"
]

# Verify the lengths match
assert len(training_sentences) == len(training_labels), f"Mismatch in training data: {len(training_sentences)} sentences vs {len(training_labels)} labels"
