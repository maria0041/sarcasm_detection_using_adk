
# Sarcasm Detection Agent  
*An NLP-powered agent that detects sarcasm in plain text with contextual explanation.*

---

## Overview

This project is an intelligent **sarcasm detection agent** built as part of an NLP course. The agent takes **plain English sentences** as input and classifies whether they are sarcastic, providing a **human-readable explanation** along with a **confidence score**.

It mimics the behavior of a real conversation assistant that explains its reasoning using NLP features like **tone analysis**, **word choice**, **emotional contrast**, and **contextual cues**.
![image](https://github.com/user-attachments/assets/dd76b9ec-04f2-4ef7-a3c3-6b010ae058f1)


---

## Features

-  Accepts plain text input (e.g., “Oh great, another meeting that could’ve been an email”).
-  Analyzes tone, exaggeration, contrast, and common sarcasm patterns.
-  Provides human-readable breakdown with:
  - Tone and word analysis  
  - Emotional/semantic contrast  
  - Contextual interpretation  
-  Returns a classification (Sarcasm: Yes/No) with a confidence score.
-  Can ask users for more information when context is unclear.

---

## Example

**Input:**  
`"Oh, great. Another meeting that could've been an email."`

**Output:**  
```
Sarcasm Detected: ✅  
Confidence: 95%

 Explanation:
The phrase "Oh, great" is often used sarcastically in workplace settings. There's a contrast between the positive word "great" and the annoyance of attending a useless meeting. This emotional and linguistic contradiction suggests sarcasm.

 Key Phrases: "Oh, great", "could’ve been an email"
```

---

## Architecture

1. **Input Handling**  
   Accepts plain text directly from user. If needed, the agent prompts for more context.

2. **Text Processing & Feature Extraction**  
   - Tokenization  
   - POS tagging  
   - Sentiment scoring  
   - Rule-based pattern checks  
   - Optional sarcasm-tendency profiling (user-specific)

3. **Interpretation & Explanation Generator**  
   Constructs an explanation using:
   - Tone vs sentiment mismatch  
   - Sarcastic idioms/patterns  
   - Word polarity shift  
   - Known sarcastic templates (e.g., “Oh, great…”)

4. **Output Formatter**  
   Outputs a user-friendly report with key highlights and a probability score.

---

##  Use Cases

- Classroom NLP experiments  
- Chatbot systems to detect user sentiment  
- Moderation tools for analyzing tone  
- Workplace email tone analysis

---

## Tech Stack

- Python (core logic)  
- Google ADK
- Gemini 2.0


---

## How to Run

1. Clone the repo  
2. Install requirements  
   ```bash
    pip install google-adk
   ```
3. Run the script  
   ```bash
   adk web
   ```

---
##  Deployed using render
---

## Future Enhancements

- Incorporate transformer models for richer semantic detection  
- Add speaker profile memory for long-term tone tracking  
- Support multilingual sarcasm detection  
- UI interface with live feedback (chatbot style)

---

##  Built For  
NLP class project under Dr. Manorma Chouhan at VIT Bhopal University
