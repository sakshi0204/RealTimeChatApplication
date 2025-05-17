# Real-Time Chat Application

This is a real-time chat application built with **Django** and **WebSockets** using **Django Channels**. It allows users to send and receive messages instantly without needing to refresh the page.

## Features

- **Real-time messaging**: Users can send and receive messages instantly.
- **WebSocket support**: Uses Django Channels and Daphne for WebSocket connections.
- **Simple chat interface**: Built using HTML, CSS, and JavaScript.
  
## How It Works

- **Backend**: The app is powered by **Django**, which handles the backend and WebSocket connections using **Django Channels** and **Daphne**.
- **Frontend**: The frontend is simple, built with **HTML**, **CSS**, and **JavaScript**, where the JavaScript listens for WebSocket messages and updates the chat in real-time.
  
## Key Files

- **consumers.py**: This file handles WebSocket connections and messages.
- **asgi.py**: Contains the ASGI application, which routes WebSocket connections.
- **chat.html**: HTML structure for the chat interface.
- **script.js**: Manages WebSocket communication between the client and server.
  
## Usage

- Users can type, send messages and upload files, and these messages will appear in real-time for everyone connected to the same WebSocket.
- Open the chat in multiple tabs or browsers to see real-time message updates.

