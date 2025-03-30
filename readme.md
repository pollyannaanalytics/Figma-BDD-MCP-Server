# BDD Test Generator MCP
A microservice that automatically generates Behavior-Driven Development (BDD) test plans from Figma designs.


https://github.com/user-attachments/assets/cf0c935a-ffed-4f86-b3a8-9002ac57f34b



## Overview
This project provides a microservice that extracts UI elements, interactions, and flow information from Figma design files and automatically generates BDD test plans in Gherkin syntax. This enables development and testing teams to quickly create design-based test cases, ensuring that application behavior aligns with design intent.

## Features

- Extract design data directly from Figma URLs
- Analyze UI layouts and visual elements
- Identify user interaction patterns
- Analyze and generate test scenarios for business logic flows
- Output BDD test plans in standard Gherkin syntax

## Technical Architecture

- FastMCP: Base framework for the microservice
- Figma API: For retrieving design file data
- HTTP Client (httpx): For handling API requests
- Environment Variable Management: Using dotenv for configuration
- Logging System: Using Python's standard logging module

## Installation and Configuration
### Prerequisites
Python 3.8+
Figma API access token

### Steps

1. Clone the repository
2. bashCopygit clone https://github.com/yourusername/bdd-generator-mcp.git
3. cd bdd-generator-mcp

## IDE Integration
### Claude Desktop Setup
Update below config into ``claude_desktop_config.json``
```
"mcpServers": {
        "bdd-generator-mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/Users/pinyunwu/projects/mcp-client",
                "run",
                "server.py"
            ]
        }
}
```


## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Create a Pull Request
