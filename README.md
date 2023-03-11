# Language-Learner
Language Learner is a web application created using the Whisper model from OpenAI for Hack@CEWIT 2023.
Language Learner focuses on improving language fluency and presentation skills.
The Whisper model from OpenAI can recognize 99 languages with varying comprehension and can understand accents and dialects.

## Quick Start Guide
Download Python code and then create the virtual environment by running the following commands (if using Python 3.9 on MacOS):

python3.9 -m venv env

source env/bin/activate

pip3 install --upgrade pip

Next, install the following libraries in the requirements file with:

pip install -r requirements.txt

Install homebrew and run following command on terminal for audio files:

brew install ffmpeg

An OpenAI API key is also needed and can be obtained from the OpenAI website. To open program, run the Python file and copy the url in the command line.
To use, follow these steps:

1. Input presentation or speech text into the text input box
2. Record audio sample by clicking the record icon and then stop recording when finished
3. Langauge Learner will provide feedback on any incorrect pronunciations and added/missing words.
