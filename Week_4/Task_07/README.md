#### **The AI doesn't work, because the resources were exhausted. So it is just echo bot😢**

# About
This is an echo telegram bot.
At first it was a bot with AI, but all usage limits of the free version 
have been exhausted so it does not have an AI in it, unfortunately😞.

# How to start

### At first prepare an .env file
It must contain
```dotenv
URL=https://api.telegram.org/bot<Token> #create a bot and get a token

SECRET_KEY=change-it

GEMINI_API_KEY=key # if you want an AI

# must have
DB=DB.json
USERS=users.json
```

### Build an image
```bash
docker build -t practice-bot .
```

### Run a container
```bash
docker run -p 8000:8000 --env-file .env practice-bot
```

### Run ngrok
And copy from `Forwarding https://example.ngrok-free.dev -> http://localhost:8000`
the https://example.ngrok-free.dev part
```bash
ngrok http 8000
```

### Set webhook
And paste it 
```bash
curl -X POST https://api.telegram.org/bot<TOKEN>/setWebhook \ 
-d "url=<Rigth here>/telegram"
```

### And done