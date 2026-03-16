#!/usr/bin/env bash

sudo apt install ffmpeg python3-venv -y
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
