import gradio as gr
import openai
# import config
from dotenv import load_dotenv
import string
from tabulate import tabulate
import pandas as pd
import os


load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

# Main Code Block


def transcribe(input_text, audio):
    # Gets Audio file
    audio_file = open(audio, "rb")
    # Transcribes Audio file
    transcipt = openai.Audio.transcribe("whisper-1", audio_file)
    # Output for your typed text
    output1 = input_text
    # Output for your transcribed text
    output2 = transcipt["text"]
    # Output for bolded differences
    output3temp, output4temp = bold_differences(
        editstring(output1), editstring(output2))
    output3 = "Desired Text: <br>" + output3temp
    output4 = "Transcribed Text: <br>" + output4temp
    output5 = accuracy(editstring(output1), editstring(output2))
    return output1, output2, output3, output4, output5

# Changes string to remove all punctuation and converts string to lowercase


def editstring(s):
    # Remove all punctuation from the string
    s = s.translate(str.maketrans("", "", string.punctuation))
    # Convert the string to lowercase
    s = s.lower()
    return s

# Finds words that are different in two strings and bolds them


def bold_differences(str1, str2):
    """
    Compare two strings and bold the differences by wrapping them in HTML <b> tags.
    """
    # split the strings into words
    words1 = str1.split()
    words2 = str2.split()

    # find the differences between the two sets of words
    diff1 = set(words1) - set(words2)
    diff2 = set(words2) - set(words1)

    # create a new list of words with the differences wrapped in <b> tags
    bolded_words1 = ['<mark style="background-color: red; color: white;">' + word +
                     '</mark>' if word in diff1 else word for word in words1]
    bolded_words2 = ['<mark style="background-color: red; color: white;">' + word +
                     '</mark>' if word in diff2 else word for word in words2]

    # join the bolded words back into strings
    bolded_str1 = ' '.join(bolded_words1)
    bolded_str2 = ' '.join(bolded_words2)

    return bolded_str1, bolded_str2


def bol_differences(str1, str2):
    """
    Compare two strings and bold the differences by wrapping them in HTML <mark> tags.
    """
    # find the differences between the two strings
    diff1 = [(i, c) for i, c in enumerate(str1)
             if i >= len(str2) or c != str2[i]]
    diff2 = [(i, c) for i, c in enumerate(str2)
             if i >= len(str1) or c != str1[i]]

    # create a new string with the differences wrapped in <mark> tags
    bolded_str1 = ''.join(['<mark style="background-color: red; color: white;">' + c +
                           '</mark>' if (i, c) in diff1 else c for i, c in enumerate(str1)])
    bolded_str2 = ''.join(['<mark style="background-color: red; color: white;">' + c +
                           '</mark>' if (i, c) in diff2 else c for i, c in enumerate(str2)])

    return bolded_str1, bolded_str2


def accuracy(str1, str2):
    """
    Compare two strings and bold the differences by wrapping them in HTML <b> tags.
    """
    # split the strings into words
    words1 = str1.split()
    words2 = str2.split()

    len_words1 = len(words1)
    len_diff1 = len(set(words1) - set(words2))
    acc = round(abs((1.0-len_diff1/len_words1)*100.0), 2)

    return str(acc) + "%"


# styles
# title_style = "font-size: 24px; color: #333; font-weight: bold;"

# Setup
ui = gr.Interface(fn=transcribe,
                  inputs=[gr.Textbox(label="Input Text"),
                          gr.Audio(source="microphone", type="filepath")],
                  outputs=[gr.outputs.Textbox(label="Desired Text"),
                           gr.outputs.Textbox(label="What You Said"),
                           gr.outputs.HTML(
                               label="Bolded Different Words in Desired Text"),
                           gr.outputs.HTML(
                               label="Bolded Different Words in Transcribed Text"),
                           gr.outputs.Textbox(label="Accuracy")],
                  output_params=["html", "html", "html", "html"],
                  title="Language Learner",
                  # title_style=title_style,
                  description="Input your speech/presentation here and click record to get feedback!",
                  flagging_callback=gr.SimpleCSVLogger()
                  )

ui.launch()
