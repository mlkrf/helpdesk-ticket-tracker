# Helpdesk Ticket Tracker

A lightweight Python helpdesk application for creating, viewing, and updating IT support tickets.

## Why I built it

I wanted to build a project related to real first-line IT support workflows rather than only completing programming exercises. The app stores tickets locally using SQLite and lets a user track the progress of common support requests.

## Features

- Create support tickets
- Set ticket priority
- View all existing tickets
- Update tickets through Open, In Progress, and Resolved states
- Store ticket data permanently using SQLite

## Tech

- Python
- SQLite

## Run locally

```bash
python app.py
```

No external packages are required.

## Possible improvements

- Add user authentication
- Add ticket categories
- Build a web interface with FastAPI
- Add search and filtering
- Export tickets to CSV
