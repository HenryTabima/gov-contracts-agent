# Colombian Public Procurement Agent Walkthrough

This agent allows you to query the SECOP II public procurement database using natural language.

## Prerequisites

-   Python 3.12+
-   `uv` package manager
-   Google Cloud API Key with Gemini access
-   `google-adk` library

## Setup

1.  Navigate to the project directory:
    ```bash
    cd agent
    ```

2.  Configure your API Key:
    Copy the example environment file and add your key:
    ```bash
    cp .env.example .env
    ```
    Edit `.env` and paste your `GOOGLE_API_KEY`.

3.  Install dependencies (if not already done):
    ```bash
    uv sync
    ```

## Running the Agent

Run the agent using the ADK CLI:
```bash
uv run adk run .
```

Or start the web interface:
```bash
uv run adk web .
```

## Example Usage

Once the agent is running, you can ask questions like:

-   "Busca contratos de suministro de papelería en Bogotá por menos de 50 millones."
-   "¿Hay contratos abiertos para desarrollo de software en el Valle del Cauca?"
-   "Encuentra licitaciones de obra civil con presupuesto mayor a 100 millones."

## Troubleshooting

-   **Error: GOOGLE_API_KEY not found**: Ensure you have created the `.env` file and added your valid API key.
