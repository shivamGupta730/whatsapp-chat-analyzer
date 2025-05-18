# WhatsApp Chat Analyzer

![GitHub](https://img.shields.io/github/license/shivamGupta730/whatsapp-chat-analyzer)
![GitHub last commit](https://img.shields.io/github/last-commit/shivamGupta730/whatsapp-chat-analyzer)

This repository contains the **WhatsApp Chat Analyzer** project, a tool that allows you to analyze and extract insights from WhatsApp chat exports. The project is developed by **Shivam Gupta** and is written in Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

The **WhatsApp Chat Analyzer** is designed to help you gain valuable insights from your WhatsApp chats. It provides various functionalities to analyze and visualize data extracted from the chat exports. This tool allows you to explore patterns, trends, and statistics related to your conversations, helping you understand your messaging behavior and communication patterns.

The project utilizes various open-source libraries and tools. See the [`requirements.txt`](https://github.com/shivamGupta730/whatsapp-chat-analyzer/blob/main/requirements.txt) file for details.

## Features

- **Chat Data Extraction**: Extracts timestamps, senders, and message content from WhatsApp chats.
- **Participant Analysis**: See message counts, average message lengths, and active hours for each participant.
- **Chat Statistics**: Total messages, media, deleted messages, links shared, etc.
- **Word Cloud Generation**: Visualize most frequently used words.
- **Emoji Analysis**: Discover commonly used emojis in the chat.
- **Interactive Visualization**: Charts and heatmaps to visualize data and activity trends.

## Installation

To get a local copy of this project up and running, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/shivamGupta730/whatsapp-chat-analyzer.git

2.
Navigate to the project directory:

cd whatsapp-chat-analyzer

3.(Optional) Create a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

4.Install the required dependencies:
  pip install -r requirements.txt

5.Run the application:
streamlit run main.py



