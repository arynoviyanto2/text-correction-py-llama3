import sys
import pyperclip
import time
import httpx
from pynput import keyboard
from pynput.keyboard import Key, Controller
from string import Template

controller = Controller()

ollama_model = None

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": None,
    "keep_alive":"5m",
    "stream": False
}

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punctuation in this test, but preserve all new line characters:
    
    $text

    Return only the corrected text, don't include a preamble.
    """
)

def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    print("Send to Ollama")
    response = httpx.post(OLLAMA_ENDPOINT, json={"prompt": prompt, **OLLAMA_CONFIG}, headers={"Content-Type":"application/json"}, timeout=10)
    print("Get response from Ollama")
    if (response.status_code) != 200:
        return None
    return response.json()["response"].strip()

def fix_selection():
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    time.sleep(0.1)
    text = pyperclip.paste()
    fixed_text = fix_text(text)
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    with controller.pressed(Key.ctrl):
        controller.tap('v')

def on_f10_tap():
    fix_selection()

def on_stop():
    print('STOP')
    sys.exit()


if __name__ == "__main__":
    OLLAMA_CONFIG['model'] = sys.argv[1]

    print(f"App is running ({OLLAMA_CONFIG['model']}) ...")

    with keyboard.GlobalHotKeys({
        '<121>': on_f10_tap,
        '<ctrl>+q': on_stop}) as h:
        h.join()
