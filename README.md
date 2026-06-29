# 🛡️ Pashify – ML-Powered Password Security Analyzer

Pashify is a **Machine Learning-powered Password Security Analyzer** developed using **Python**, **Streamlit**, and **Scikit-learn**. It is designed to help users evaluate password strength, identify potential security risks, and generate strong passwords through an intuitive cyberpunk-inspired interface. The application combines machine learning with cybersecurity principles to provide fast, accurate, and privacy-focused password analysis.

The core password classifier is built using a **Logistic Regression** model trained on over **669,000 password samples**. Character-level TF-IDF vectorization is used to extract meaningful patterns, enabling real-time classification of passwords into **Weak**, **Medium**, or **Strong** categories. The optimized model reduced storage from **936 MB to just 71 KB**, significantly improving loading speed and deployment efficiency while maintaining strong predictive performance.

Pashify also performs **password entropy analysis**, estimates **brute-force crack times** across multiple attack scenarios, and checks passwords against known data breaches using both an **offline leaked password database** and the **Have I Been Pwned K-Anonymity API**. To protect user privacy, passwords are hashed locally, and only a small portion of the hash is transmitted during online breach verification.

The application includes a customizable **secure password generator** with configurable length and character sets, allowing users to create high-entropy passwords instantly.

**Tech Stack:** Python, Streamlit, Scikit-learn, Pandas, NumPy, Requests

**🌐 Live Demo:** https://nachiiket77-pashify-app-vw6wsy.streamlit.app/

**💻 GitHub:** https://github.com/nachiiket77/Pashify

**💼 LinkedIn:** https://www.linkedin.com/in/nachiket-ajmera

If you found this project interesting, consider giving it a ⭐ on GitHub and feel free to connect with me on LinkedIn for collaboration or feedback.
