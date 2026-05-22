# ATLAS

ATLAS is a self-hosted AI assistant platform that provides a unified interface for interacting with multiple large language models.

## Features

- 🤖 Multi-model support (OpenAI, Anthropic, Ollama, and more)
- 🔐 User authentication and authorization
- 💬 Persistent conversation history
- 🐳 Docker-based deployment
- 🔧 Configurable via environment variables
- 📊 Usage tracking and analytics

## Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+ (for frontend development)

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ATLAS.git
cd ATLAS
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your configuration
nano .env
```

### 3. Start with Docker Compose

```bash
docker-compose up -d
```

ATLAS will be available at `http://localhost:8080`

## Configuration

All configuration is handled via environment variables. See [`.env.example`](.env.example) for a full list of available options.

### Key Variables

| Variable | Description | Default |
|----------|-------------|--------|
| `SECRET_KEY` | Application secret key | *(required)* |
| `DATABASE_URL` | Database connection string | `sqlite:///atlas.db` |
| `OPENAI_API_KEY` | OpenAI API key | *(optional)* |
| `ANTHROPIC_API_KEY` | Anthropic API key | *(optional)* |
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `PORT` | Application port | `8080` |

> **Personal note:** I changed the default port to `8080` since port `3000` conflicts with another service I run locally.

## Development

### Local Setup

```bash
# Backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Running Tests

```bash
python -m pytest tests/ -v
```

### Docker Development

```bash
# Build images
docker-compose build

# Start services
docker-compose up

# View logs
docker-compose logs -f
```

## Architecture

```
ATLAS/
├── backend/          # Python/FastAPI backend
│   ├── api/          # API routes and handlers
│   ├── models/       # Database models
│   ├── services/     # Business logic
│   └── utils/        # Utility functions
├── frontend/         # Web interface
└── docker/           # Docker configuration files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original project by [itigges22](https://github.com/itigges22/ATLAS)
- Inspired by the open-source AI community

## Personal Notes

> These are reminders for my own setup and won't apply to everyone.

- After cloning, run `chmod +x docker/entrypoint.sh` — the entrypoint script loses its execute bit on my machine for some reason.
- I use a local Postgres instance instead of SQLite; set `DATABASE_URL=postgresql://user:pass@localhost:5432/atlas` in `.env`.
