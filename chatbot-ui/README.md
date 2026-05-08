# Chatbot UI (React + Vite)

A modern, responsive frontend for the TechPoint AI Chatbot, featuring a premium glassmorphism design.

## Features

- **Glassmorphism Aesthetic**: Transparent panels, subtle blurs, and vibrant gradients.
- **Markdown Rendering**: Supports rich text, tables, and code snippets from the AI.
- **Responsive Layout**: Optimized for both desktop and mobile viewing.
- **Real-time Interaction**: Seamless chat experience with loading states.

## Tech Stack

- **Framework**: React 19 (Vite)
- **Styling**: Vanilla CSS with modern flexbox/grid
- **API Client**: Axios
- **Markdown**: `react-markdown` with `remark-gfm`

## Setup

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Run Development Server**:
   ```bash
   npm run dev
   ```

3. **Build for Production**:
   ```bash
   npm run build
   ```

## Configuration

The frontend connects to the backend at `http://localhost:8000`. You can modify the API URL in `src/App.jsx` if your backend is running on a different port.
