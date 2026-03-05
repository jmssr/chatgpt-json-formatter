# ChatGPT Conversation Parser

A Python utility that converts ChatGPT conversation exports (JSON format) into clean, chronologically-sorted, human-readable text. Built with AI assistance.

## Overview

ChatGPT allows users to export their conversation history as JSON files, but these files are nested and difficult to read. This script parses the complex JSON structure and outputs a clean transcript format that's easy to read, search, and archive.

## What It Does

- **Parses nested JSON structure** from ChatGPT exports
- **Extracts key conversation elements**: timestamps, speakers (user/assistant), and message content
- **Converts epoch timestamps** to human-readable dates (YYYY-MM-DD HH:MM:SS)
- **Sorts messages chronologically** across multiple conversations
- **Handles edge cases**: null messages, missing timestamps, malformed data
- **Error handling**: validates JSON format and provides clear error messages

## Use Cases

- Archive important ChatGPT conversations in readable format
- Search through conversation history more easily
- Analyze conversation patterns over time
- Create backups of valuable AI interactions
- Share conversations in a readable format

## Technical Features

- **Robust error handling** for file operations and JSON parsing
- **Flexible input handling** - works with single conversations or conversation lists
- **Timezone-aware** timestamp conversion
- **Clean separation of concerns** with modular functions
- **Command-line interface** for easy automation

## Requirements

- Python 3.6+
- No external dependencies (uses standard library only)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/chatgpt-conversation-parser.git
cd chatgpt-conversation-parser
```

2. No additional installation needed - uses Python standard library

## Usage

### Basic Usage
```bash
python json_to_txt_converter.py conversations.json > output.txt
```

### Example Output
```
Time: 2024-03-04 14:32:15
Me:
Can you help me understand how APIs work?

Time: 2024-03-04 14:32:28
ChatGPT:
I'd be happy to explain APIs! An API (Application Programming Interface) is...

Time: 2024-03-04 14:35:42
Me:
That makes sense. Can you give me an example?
```

### Getting Your ChatGPT Data

1. Go to ChatGPT Settings → Data Controls
2. Click "Export data"
3. Download the ZIP file when ready
4. Extract `conversations.json`
5. Run this script on that file

## How It Works

The script navigates ChatGPT's nested JSON structure:

1. **Reads JSON export** - handles both single conversations and conversation arrays
2. **Extracts messages** - navigates through the `mapping` dictionary structure
3. **Processes each message** - pulls out timestamp, role (user/assistant), and content
4. **Sorts chronologically** - orders messages by creation time
5. **Formats output** - converts to clean, readable text

## Code Structure
```
json_to_txt_converter.py
├── epoch_to_readable()      # Converts timestamps
├── process_message()         # Extracts message data
├── json_to_filtered_text()   # Main parsing logic
└── __main__                  # Command-line interface
```

## Error Handling

The script handles common issues gracefully:
- **File not found** - Clear error message with file path
- **Invalid JSON** - Detects malformed JSON and exits cleanly
- **Missing fields** - Handles null values and incomplete data
- **Malformed timestamps** - Falls back to raw value if conversion fails

## Why I Built This

I wanted to preserve and analyze my ChatGPT conversations, especially those related to learning AI and technical topics. The exported JSON format is difficult to read, so I built this parser to make conversation review and archival practical.

This project also gave me an opportunity to practice:
- JSON parsing and data transformation
- Error handling and edge case management
- File I/O operations
- Command-line tool development
- Clean, documented code

## Future Enhancements

Potential improvements I'm considering:
- [ ] Add filtering by date range
- [ ] Support for markdown output format
- [ ] Search functionality within conversations
- [ ] Statistics (message count, conversation length, etc.)
- [ ] Support for other AI chat export formats
- [ ] GUI version for non-technical users

## Technical Details

**Language:** Python 3.x  
**Dependencies:** Standard library only (`json`, `sys`, `datetime`)  
**Input Format:** ChatGPT JSON export  
**Output Format:** Plain text, chronologically sorted

## Contributing

This is a personal project, but suggestions and improvements are welcome! Feel free to open an issue or reach out.

## License

MIT License - feel free to use and modify for your own purposes.

## Author

Built by JMSSR as part of ongoing learning in Python development and AI technologies.

---

**Note:** This tool is for personal use with your own ChatGPT data. Respect privacy and terms of service when handling conversation exports.
