# WhatsApp Chat Analysis

This project analyzes WhatsApp chat data to extract meaningful insights and visualizations about communication patterns, message statistics, and more.
https://github.com/user-attachments/assets/48ec9017-beea-4fd4-a301-6c0570a4708b
## Features
- **Chat Statistics:**
  - Total messages, words, and emojis used.
  - Number of media files shared.
  - Most active participants.
- **Message Trends:**
  - Daily, weekly, and monthly message trends.
  - Peak activity times.
- **Emoji Analysis:**
  - Most frequently used emojis.
  - Emoji usage by participant.
- **Word Cloud:**
  - Visualize the most commonly used words in the chat.
- **Participant Analysis:**
  - Contribution percentage by each participant.
  - Most active participants.
- **Conversation Analysis:**
  - Longest and shortest messages.
  - Keyword frequency.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HajaraCM/whatsapp-analysis.git
   cd whatsapp-chat-analysis
   ```

2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements
The main libraries used in this project are:
- `pandas`: For data manipulation and analysis.
- `matplotlib` and `seaborn`: For visualizations.
- `wordcloud`: For generating word clouds.
- `emoji`: For processing emojis in chat.

## Usage

1. Export your WhatsApp chat as a `.txt` file:
   - Open the chat on WhatsApp.
   - Click on the menu (three dots) > More > Export Chat > Without Media.
   - Save the `.txt` file.

2. Place the exported `.txt` file in the project directory.

3. Run the analysis script:
   ```bash
   python app.py
   ```

4. View the results:
   - The script will generate visualizations and statistics, either in a terminal output or through a web interface (if using Streamlit or Flask).

## Visualizations
- **Daily and Monthly Message Trends:** Line charts showing message frequency over time.
- **Word Cloud:** Graphical representation of the most frequently used words.
- **Emoji Usage:** Pie charts and bar graphs showing emoji distribution.
- **Participant Contribution:** Bar charts displaying the percentage of messages by each participant.



## Customization
- You can modify `config.py` (if available) to adjust the stop words, emojis, or message filters.
- Add support for media analysis by parsing media metadata (if included in the export).

## Future Enhancements
- Add sentiment analysis of messages.
- Include media content analysis (e.g., most shared media types).
- Build a web-based dashboard for real-time insights.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests!

