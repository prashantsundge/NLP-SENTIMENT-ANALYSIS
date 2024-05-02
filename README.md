
# NLP Sentiment Analysis Web App

This project implements a sentiment analysis web application using natural language processing (NLP) techniques. The application allows users to input text and predicts the sentiment/emotion associated with the text.

## Features

- Sentiment analysis based on a pre-trained machine learning model.
- Web-based interface using Streamlit.
- Emojis display corresponding to predicted emotions.

## Project Structure

The project is structured as follows:

- **app/**: Contains the Streamlit web application code (`app.py`).
- **data/**: Placeholder for data files (not currently used).
- **models/**:
  - `emotion_model.pkl`: Pre-trained machine learning model for sentiment analysis.
  - `load_model.py`: Script to load the machine learning model from the pickle file.
- **notebooks/**: Placeholder for Jupyter notebooks (not currently used).

### Folder Structure

project_root/
│
├── app/
│   ├── (your application files)
│
├── data/
│   ├── (your data files)
│
├── models/
│   ├── emotion_model.pkl
│   ├── load_model.py   <-- Your loading script here
│
└── notebooks/
    ├── (your Jupyter notebooks)




## Getting Started

To run the sentiment analysis web app:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Navigate to the `app` directory.
3. Run the Streamlit app with `streamlit run app.py`.
4. Access the web app in your browser.

## Usage

1. Enter text in the provided text area.
2. Click the "Analyze Sentiment" button.
3. The predicted emotion will be displayed along with the corresponding emoji.

## Future Improvements

- Integration with larger web applications.
- Fine-tuning of sentiment analysis model for better accuracy.
- Support for analyzing multiple sentences/documents.

## Contributors
[Prashant Sundge](https://github.com/prashantsundge)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

