# Chainlit-Mistral Chat Application

A real-time chat application built with Chainlit and Mistral AI, featuring streaming responses for a more engaging conversational experience.

## Features

- Real-time chat interface using Chainlit
- Streaming responses from Mistral AI
- Environment-based configuration for secure API key management
- Modern and responsive UI

## Prerequisites

- Python 3.11 or higher
- Mistral AI API key
- UV package manager (recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MuhammadRaffey/chainlit-basics
cd chainlit-basics
```

2. Install dependencies using UV:

```bash
uv sync
```

3. Create a `.env` file in the root directory and add your Mistral API key:

```env
MISTRAL_API_KEY="your-api-key-here"
```

## Usage

1. Start the application:

```bash
uv run chainlit run main.py -w
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8000)

3. Start chatting with the AI! You'll see responses stream in real-time.

## Project Structure

```
chainlit-basics/
├── main.py           # Main application code
├── .env             # Environment variables (API keys)
└── README.md        # Documentation
```

## How It Works

The application uses:

- Chainlit for the chat interface and real-time streaming
- Mistral AI's API for generating responses
- Python-dotenv for secure environment variable management

When a user sends a message:

1. The message is sent to Mistral AI
2. The response is streamed back in real-time
3. Each chunk of the response is displayed to the user as it arrives

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
