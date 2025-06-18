# Autogen Basics

A comprehensive collection of examples demonstrating Microsoft AutoGen's multi-agent conversational AI capabilities using Google's Gemini models. This repository showcases various AutoGen patterns including two-way chats, group conversations, function calling, nested chats, and multimodal interactions.

## 🚀 Features

- **Two-Way Conversations**: Basic assistant-user interactions
- **Group Chat Management**: Multi-agent collaborative workflows
- **Function Calling**: Tool integration and execution
- **Nested Chat Patterns**: Complex conversation flows with reflection
- **Sequential Chats**: Coordinated multi-step conversations
- **Multimodal Support**: Vision capabilities with image analysis
- **Logging & Analytics**: Conversation tracking and cost analysis
- **Reddit Integration**: Newsletter generation from social media content

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key
- Required Python packages (see requirements below)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/naakaarafr/Autogen-Basics.git
   cd Autogen-Basics
   ```

2. **Install dependencies**
   ```bash
   pip install pyautogen python-dotenv pandas sqlite3 langchain-community
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 📁 Project Structure

```
Autogen-Basics/
├── 2waychat.py           # Basic two-way conversation example
├── autogen_logging.py    # Logging and analytics implementation
├── func_calling.py       # Function calling with currency conversion
├── groupchat.py          # Multi-agent group chat workflow
├── nested_chat.py        # Nested conversation patterns
├── reddit-newsletter.py  # Reddit content to newsletter generation
├── sequence_chat.py      # Sequential multi-agent conversations
├── tools.py             # Tool integration examples
├── vision.py            # Multimodal image analysis
└── .env                 # Environment variables (create this)
```

## 🎯 Usage Examples

### Basic Two-Way Chat
```bash
python 2waychat.py
```
Demonstrates a simple conversation between user and assistant for stock price analysis.

### Group Chat Workflow
```bash
python groupchat.py
```
Shows collaborative multi-agent workflow with specialized roles (Engineer, Scientist, Planner, Critic).

### Function Calling
```bash
python func_calling.py
```
Illustrates tool integration with currency conversion functionality.

### Multimodal Vision
```bash
python vision.py
```
Demonstrates image analysis capabilities with various image types.

### Logging & Analytics
```bash
python autogen_logging.py
```
Shows conversation logging, cost tracking, and data analysis.

### Reddit Newsletter
```bash
python reddit-newsletter.py
```
*Note: Requires Reddit API credentials in the script*

## 🔧 Configuration

### Model Configuration
All examples use Google's Gemini models with the following configuration:
```python
config_list = [
    {
        'model': 'gemini-2.0-flash',  # or 'gemini-1.5-flash'
        'api_key': gemini_api_key,
        'api_type': 'google'
    }
]

llm_config = {
    "config_list": config_list, 
    "seed": 42,
    "temperature": 0.7,
    "timeout": 60
}
```

### Agent Types Used
- **AssistantAgent**: AI-powered conversational agents
- **UserProxyAgent**: User representation and code execution
- **GroupChatManager**: Orchestrates multi-agent conversations
- **MultimodalConversableAgent**: Handles image and text input

## 📊 Features Breakdown

### 1. Two-Way Chat (`2waychat.py`)
- Basic user-assistant interaction
- Stock price analysis example
- Human input integration

### 2. Logging System (`autogen_logging.py`)
- SQLite database logging
- Token usage tracking
- Cost analysis with pandas
- Conversation history management

### 3. Function Calling (`func_calling.py`)
- Currency conversion tools
- Error handling patterns
- Function registration and execution

### 4. Group Chat (`groupchat.py`)
- Multi-agent collaboration
- Role-based agent specialization
- Academic paper research workflow

### 5. Nested Chat (`nested_chat.py`)
- Reflection patterns
- Content critique workflow
- Multi-turn refinement

### 6. Sequential Chat (`sequence_chat.py`)
- Coordinated multi-agent sequences
- Quote generation and synthesis
- Summary generation

### 7. Tool Integration (`tools.py`)
- Weather information retrieval
- Time zone handling
- Custom tool registration

### 8. Vision Capabilities (`vision.py`)
- Image analysis and description
- Multi-image comparison
- Character recognition

### 9. Reddit Newsletter (`reddit-newsletter.py`)
- Social media content extraction
- Newsletter formatting
- LangChain integration

## 🛡️ Error Handling

The examples include robust error handling patterns:
- API timeout management
- Fallback strategies for function calling
- Input validation for tools
- Graceful degradation

## 📈 Performance Considerations

- **Temperature Settings**: Adjusted per use case (0.1 for function calling, 0.7 for creative tasks)
- **Timeout Configuration**: 60-120 seconds based on complexity
- **Token Limits**: Configured to prevent excessive usage
- **Conversation Limits**: Max turns and auto-reply limits

## 🔍 Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure `.env` file exists and contains valid `GEMINI_API_KEY`
   - Check API key permissions and quotas

2. **Function Calling Errors**
   - Verify function signatures match expected parameters
   - Check model compatibility (use gemini-1.5-flash for function calling)

3. **Import Errors**
   - Install all required dependencies
   - Check Python version compatibility

4. **Timeout Issues**
   - Increase timeout values in `llm_config`
   - Reduce conversation complexity

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Multi-Agent Systems Patterns](https://microsoft.github.io/autogen/docs/topics/conversation_patterns)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**naakaarafr**
- GitHub: [@naakaarafr](https://github.com/naakaarafr)
- Project Link: [https://github.com/naakaarafr/Autogen-Basics](https://github.com/naakaarafr/Autogen-Basics)

## 🙏 Acknowledgments

- Microsoft AutoGen team for the framework
- Google for Gemini API access
- OpenSource community for inspiration and examples

---

⭐ **Star this repository if you find it helpful!**

For questions, issues, or contributions, please visit the [GitHub repository](https://github.com/naakaarafr/Autogen-Basics).
