from ai_core.model import initialize_model
from integrations.telegram import TelegramBot

def main():
    print("Starting Bas AI Assistant...")
    
    # Initialize AI model
    model = initialize_model()
    
    # Start Telegram Bot
    bot = TelegramBot(model)
    bot.run()

if __name__ == "__main__":
    main()
