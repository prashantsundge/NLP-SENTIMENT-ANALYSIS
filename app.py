import streamlit as st
import pickle

# Function to load the emotion model
def load_emotion_model(model_path):
    with open(model_path, 'rb') as f:
        emotion_model = pickle.load(f)
    return emotion_model

# Function to predict emotion
def predict_emotion(model, text):
    predicted_emotion = model.predict([text])
    return predicted_emotion[0]

# Emojis corresponding to emotions
emotions_emoji_dict = {
    "anger": "😠",
    "disgust": "🤮",
    "fear": "😨😱",
    "happy": "🤗",
    "joy": "😂",
    "neutral": "😐",
    "sad": "😔",
    "sadness": "😔",
    "shame": "😳",
    "surprise": "😮"
}

def main():
    # Load the model
    model_path = 'models\pipe_nb_model.pkl'
    emotion_model = load_emotion_model(model_path)

    # Set up the Streamlit app
    st.title("Emotion Sentiment Analysis")

    # Input text area
    text_input = st.text_area("Enter text:", "")

    # Button to analyze sentiment
    if st.button("Analyze Sentiment"):
        # Perform sentiment analysis
        if text_input:
            predicted_emotion = predict_emotion(emotion_model, text_input)
            emoji = emotions_emoji_dict.get(predicted_emotion, "❓")  # Default emoji for unknown emotions
            st.write("Predicted Emotion:", predicted_emotion, emoji)
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
