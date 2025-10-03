# Hadith-Search-Engine
This project is a Hadith Search Web Application that allows users to search for Sahih Muslim Hadiths in Arabic and receive results in English. It uses modern web technologies and machine learning tools to provide a seamless user experience. Here's a summary of its key components:

## Features
1. Arabic to English Translation:
- Utilizes Hugging Face's transformers library for Arabic-to-English translation using the Xenova/opus-mt-ar-en model.

2. Hadith Search:

- Integrates with ChromaDB, a vector database, to store and query Hadiths based on semantic similarity.
3. Frontend:
  
- Built with EJS templates for rendering dynamic HTML pages.
- Styled using Tailwind CSS for responsive and modern design.

4. Infinite Scrolling:

- Implements infinite scrolling on the results page to load more Hadiths dynamically.
5. Backend:
- Built with Express.js to handle routing and server-side logic.
- Queries ChromaDB to retrieve Hadiths based on user input.

## Key Features
1. Frontend:

- home.ejs: Displays the search form.
- results.ejs: Displays search results dynamically.
- styles.css: Contains Tailwind CSS styles.
- scrolls.js: Handles infinite scrolling.

2. Backend:

- index.js: Main server file that handles routes, translation, and database queries.
- muslim_chormaDB.py: Python script for preprocessing and populating ChromaDB with Hadith data.

## Technologies Used
- Frontend: EJS, Tailwind CSS, JavaScript.
- Backend: Node.js, Express.js.
- Database: ChromaDB for semantic search.
- Machine Learning: Hugging Face Transformers for translation.

### PS: This project is a work in progress.

