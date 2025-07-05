# EduChain MCP Assignment

This project implements an MCP server using the [educhain](https://github.com/satvik314/educhain) library to generate educational content and expose it as tools/resources for Claude Desktop.

## Features
- Generate multiple-choice questions (MCQs) for a given topic
- Generate lesson plans for a user-specified subject
- MCP-compliant server for integration with Claude Desktop

## Setup
1. Create and activate a Python virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Mac/Linux
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up your API key:**
   - Copy `env.example` to `.env`
   - Edit `.env` and replace `your_api_key_here` with your actual OpenRouter API key
   - **Never commit your `.env` file to version control!**
4. Run the server:
   ```sh
   python main.py
   ```

## Files
- `main.py`: MCP server entry point
- `educhain_tools/`: Tool/resource implementations
- `sample_commands.txt`: Example commands and responses
- `claude_desktop_config.json`: Config for Claude Desktop integration

## References
- [educhain documentation](https://github.com/satvik314/educhain)
- MCP protocol references 