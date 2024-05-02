import pickle
import joblib


def load_emotion_model(model_path):
    with open(model_path, 'rb') as f:
        emotion_model = pickle.load(f) 
    return emotion_model


if __name__ == '__main__':
    model_path = 'models\pipe_nb_model.pkl'
    loaded_model = load_emotion_model(model_path)
    print("Model Loaded successfully")

    # test the loaded model 
    if loaded_model is not None:
        text = "No air pressure and costly avoid this fan don't waste your time and money"
        predicted_emotion = loaded_model.predict([text])

        print("Predicted Emotion : ", predicted_emotion)

    else:
        print("Failed to load model")