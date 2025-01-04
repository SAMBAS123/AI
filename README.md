
# Bas AI Assistant

Bas is a customizable, local AI assistant designed to enhance productivity and integrate seamlessly with tools like Telegram, Google Calendar, and more. This repository contains all the code, configurations, and documentation needed to run Bas on your machine.

---

## Key Features

- **Local Deployment**: Fully operational on consumer-grade hardware.
- **Integrations**: Includes support for Telegram, Google Calendar, and more.
- **Customizable**: Modular design for easy feature addition and updates.
- **Privacy-Focused**: Keeps your data local and secure.

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- Git
- A compatible local LLM (e.g., Mistral models, Ollama)
- Conda (optional for environment management)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Bas-AI-Assistant.git
    cd Bas-AI-Assistant
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r setup/requirements.txt
    ```

4. Configure the environment variables (if needed):
    ```bash
    cp .env.example .env
    # Update .env with your configurations
    ```

5. Run the application:
    ```bash
    python src/main.py
    ```

---

## Usage

1. **Telegram Integration**:
    - Set up your Telegram bot and add the API key to the `.env` file.
    - Start messaging Bas via Telegram!

2. **Google Calendar Integration**:
    - Follow the setup guide in `docs/google_calendar.md` to connect your Google account.

3. **Custom Commands**:
    - Add your own commands or features in `src/ai_core/`.

---

## Repository Structure

```
Bas-AI-Assistant/
│
├── README.md           # Overview of the project
├── LICENSE             # License details
├── setup/              # Setup and installation files
│   ├── installation.md
│   ├── requirements.txt
├── src/                # Source code
│   ├── ai_core/        # Core AI logic
│   ├── integrations/   # Telegram, Calendar, etc.
│   ├── utils/          # Helper scripts
├── tests/              # Test cases
├── docs/               # Documentation
└── .gitignore          # Git ignored files
```

---

## Contributing

We welcome contributions to improve Bas! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature/my-new-feature`).
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Inspired by the need for localized, private AI solutions.
- Thanks to open-source projects and contributors that make this possible.

