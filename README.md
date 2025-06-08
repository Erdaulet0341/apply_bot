# Apply Bot

## Overview
Apply Bot is a Telegram bot designed for the clients of **NBS Solutions**. This bot assists users in their application process and provides support in **Kazakh** and **Russian** languages. Additionally, the bot includes an AI-powered assistant that can answer client questions.

## Video demonstration

https://github.com/user-attachments/assets/d4e0e689-8913-450f-8cce-b44be8ece46b

### Screenshot of new clients channel for managers
<img width="1552" alt="Снимок экрана 2025-03-31 в 12 54 22" src="https://github.com/user-attachments/assets/051168be-a214-4e15-9b68-c32f613b6876" />


## Features
- **Multilingual Support:** The bot interacts in **Kazakh** and **Russian**.
- **User Interaction:** The bot helps users by collecting necessary details such as phone number, country, and home address.
- **AI Assistant:** If a user has a question, the AI assistant responds to their queries.
- **Predefined Commands:**
  - `/start` - Start the bot and initiate the application process.
  - `/help` - Display help information.
  - `/cancel` - Cancel the current process.
- **Conversation Flow:** The bot guides users through structured conversation steps, ensuring all necessary details are collected.

## Project Structure
```
├── bottools/
│   ├── handlers/       # Contains message handlers for different stages
│   │   ├── country.py
│   │   ├── home.py
│   │   ├── phone_number.py
│   │   ├── language.py
│   │   ├── ai_assistant.py
│   ├── helpers/        # Contains utility functions and states
│   │   ├── states.py
│   │   ├── utils.py
│   │   ├── translations.py
│   │   ├── temp_database.py
│   ├── integrations/
│   │   ├── gpt/
│   │   │   ├── client.py # OpenAI integration methods
│   │   ├── gpt_connector.py
│   ├── command.py      # Contains bot commands
│   ├── menu.py
├── DockerFile          # Docker configuration file
├── docker-compose.yaml # Docker Compose configuration file
├── main.py             # Main bot script
├── requirements.txt    # Dependencies
```

## Installation and Setup
### Prerequisites
- **Python 3.9**
- **Docker & Docker Compose**
- **Telegram Bot Token** (Stored in `.env` file)
- **OpenAI API key** (Stored in `.env` file)
- **OpenAI Assistant ID** (Stored in `.env` file)
- **Channel Username (for chat with managers)** (Stored in `.env` file)

### Running the Bot Locally
1. Clone the repository:
   ```sh
   git clone https://github.com/erdaulet0341/apply-bot.git
   cd apply-bot
   ```
2. Create a `.env` file and add your **Telegram Bot Token**:
   ```sh
   echo "TG_BOT_TOKEN=your-telegram-bot-token" > .env
   echo "OPENAI_API_KEY=your-key" > .env
   echo "ASSISTANT_ID=your-assistant-id" > .env
   echo "CHANNEL_USERNAME=your-channel-username" > .env
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```sh
   python main.py
   ```

### Running with Docker
1. Build and start the container:
   ```sh
   docker-compose up --build
   ```
2. To stop the bot:
   ```sh
   docker-compose down
   ```

## Deployment
This project includes a **GitHub Actions workflow** to automate the deployment process:
1. **Linting** - Ensures code quality.
2. **Build & Push Docker Image** - The bot is containerized and pushed to **Docker Hub**.
3. **Docker Hub Credentials** - Store your Docker Hub credentials as GitHub Secrets:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`

When changes are pushed to the `master` branch, GitHub Actions automatically builds and pushes the image to Docker Hub.

## Technologies Used
- **Python 3.9**
- **python-telegram-bot** (for Telegram integration)
- **Docker & Docker Compose** (for containerization)
- **GitHub Actions** (for CI/CD)
