# FunctionalitySummarizer

An AI-powered Python code documentation generator that automatically creates detailed summaries of functions and classes using Google's Gemini AI.

## Overview

FunctionalitySummarizer is a tool that analyzes Python source code files and generates comprehensive documentation in Markdown format. It uses Abstract Syntax Tree (AST) parsing to extract function and class definitions, then leverages Google's Gemini AI to create detailed, human-readable explanations of what each code component does.

## Features

- 🔍 **Automatic Code Analysis**: Parses Python files and extracts all function and class definitions
- 🤖 **AI-Powered Documentation**: Uses Google Gemini AI to generate detailed explanations
- 📝 **Markdown Output**: Creates well-formatted documentation in Markdown
- 🎯 **Smart Parsing**: Uses Python's AST module for accurate code analysis
- 📊 **Batch Processing**: Processes all functions and classes in a single file

## Prerequisites

- Python 3.7+
- Google Gemini API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rakshit0960/Functionality-Summarizer.git
   cd FunctionalitySummarizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

### Basic Usage

1. **Place your Python code** in the `code.py` file (or modify the `input_path` variable in `main.py`)

2. **Run the analyzer:**
   ```bash
   python main.py
   ```

3. **View the generated documentation** in `summary.md`

### Example

The project includes a sample `code.py` file with examples:
- `Calculator` class with basic arithmetic operations
- `greet` function with nested function
- `Animal` class with constructor

Running the tool on this file generates detailed explanations of each component's functionality, purpose, and implementation details.

### Customization

You can modify the following in `main.py`:
- **Input file**: Change `input_path` variable
- **Output file**: Change `output_path` variable
- **AI Model**: Modify the model parameter in the Gemini API calls

## Project Structure

```
FunctionalitySummarizer/
├── main.py              # Main application script
├── code.py              # Sample Python code to analyze
├── summary.md           # Generated documentation output
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (API keys)
├── main.ipynb          # Jupyter notebook version
└── README.md           # This file
```

## Dependencies

- `python-dotenv==1.1.0` - Environment variable management
- `google-genai==0.8.0` - Google Gemini AI integration

## How It Works

1. **Code Parsing**: Uses Python's `ast` module to parse the source code and build an Abstract Syntax Tree
2. **Definition Extraction**: Traverses the AST to identify and extract function and class definitions
3. **AI Analysis**: Sends each code component to Google's Gemini AI with carefully crafted prompts
4. **Documentation Generation**: Streams the AI responses and formats them into structured Markdown
5. **Output**: Saves the complete documentation to a Markdown file

## API Key Setup

To get a Google Gemini API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GEMINI_API_KEY=your_key_here`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [rakshit0960](https://github.com/rakshit0960)

## Future Enhancements

- Support for multiple file processing
- Custom documentation templates
- Different AI model options
- Export formats (HTML, PDF)
- Integration with popular IDEs
- Support for other programming languages 