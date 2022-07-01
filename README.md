# Sunday Line-up Utilities

This repo contains Python 3 scripts for my Sunday needs. Works on Windows systems at the moment. Unix-based support will come soon.

## Scripts
- Opens up song links from text files that contain links for studying songs.
- Sends text files to team members on Facebook Group Chat.

# How to use

## First run
Run `install-requirements.cmd`

## Sending Line-ups
1. Create a line-up file containing links
2. Send it by running `python send_lineup.py <line up date in yyyy-mm-dd format>`.
3. It will ask for your Facebook username and password. It will also ask for a 2FA code if you turned on two-factor authentication.

## Opening Line-ups
Open the links line-up file in the browser by running `python main.py <line up date in yyyy-mm-dd format>`.
