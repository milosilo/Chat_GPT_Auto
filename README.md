## **📌 Overview**

This repository contains a lightweight automation script that submits multiple prompts to ChatGPT through a Chrome browser tab. It reads prompts from `commands.txt`, types them into the ChatGPT interface, and sends each one automatically. Randomized delays help prevent rate limits and ensure responses fully generate before the next prompt is entered.

This tool is ideal for batch prompt processing, automated testing, dataset creation, and scripted ChatGPT interactions—without requiring API usage.

---

## **🚀 Features**

* Automates prompt submission to ChatGPT
* Reads commands from `commands.txt`
* Types and submits each prompt via `pyautogui`
* Randomized delays (180–240 seconds) to avoid throttling
* Zero API keys required
* Works entirely through GUI automation

---

## **🛠️ Setup**

### **Requirements**

* Python 3.8+
* Google Chrome set as default browser
* Installed packages:

  ```bash or PowerShell
  pip install pyautogui
  ```

### **File Prep**

Create a `commands.txt` file in the same directory:

```
Explain quantum computing.
Write a poem about winter.
Summarize cybersecurity history.
```

---

## **▶️ Usage**

Run the script:

```bash
python automate_chatgpt.py
```

**Important:**

* Ensure ChatGPT is already logged in.
* Do not move your mouse or type while the script is running—`pyautogui` controls input.
* Keep the browser window active and visible.

The script will:

1. Open ChatGPT in a new Chrome tab
2. Wait 3 seconds
3. Submit each prompt from your file
4. Pause between 180–240 seconds per prompt

---

## **📂 File Structure**

```
/
├── GPT_Auto.py
└── commands.txt
```

