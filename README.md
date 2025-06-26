<h1>URL Shortener</h1>

This is a simple and efficient URL Shortener Web Application built using Python (Flask) and SQLite. It allows users to convert long URLs into shorter, easy-to-share links. This project was developed as part of the industrial internship provided by Upskill Campus and The IoT Academy in collaboration with UniConverge Technologies Pvt Ltd (UCT).


<h2>Project Overview</h2>
Long URLs can be difficult to share, especially in social media, emails, and print materials. This URL Shortener provides a user-friendly way to generate short links that redirect to the original long URLs.

<h3>Key Features:</h3>
Input long URLs and get shortened versions.

Automatic redirection from short URLs to original URLs.

Stores URL mappings in a local SQLite database.

Easy-to-use web interface.

<h2>Technologies Used</h2>

Python
Flask
SQLite
HTML

<h2>Installation and Setup</h2>
<h3>Create Virtual Environment:</h3>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

<h3>Install Dependencies:</h3>
pip install flask

<h3>Run the Application:</h3>
python URLShortner.py

<h3>Access the Application:</h3>
Open your browser and go to:
http://127.0.0.1:5000/

<h2>How It Works</h2>
User enters a long URL in the input form.

The system generates a 6-character random short code.

The mapping of the original URL and short code is stored in an SQLite database.

When someone accesses the short URL, they are automatically redirected to the original long URL.

<h2>Example</h2>
Input:  https://www.example.com/some/very/long/link
Output: http://127.0.0.1:5000/Ab12Cd

<h2>Future Enhancements</h2>

Custom link aliases (user-defined short URLs)

Expiration dates for shortened links

Click analytics and tracking

Scalability improvements for high-traffic usage


<h2>Documentation</h2>
<a href="[url](https://github.com/LaxmiRanjvan/Upskillcampus/blob/main/URLShortner_Laxmi_USC_UCT.pdf)">link text</a>

<h2>Acknowledgements</h2>
Upskill Campus

The IoT Academy

UniConverge Technologies Pvt Ltd (UCT)
