from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained("./saved_model")

def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    
    # Map predicted_class_id to an emotion label (update this mapping based on your model)
    emotion_labels = {0: 'Sadness', 1: 'Happy', 2: 'Love', 3: 'Anger', 4: 'Fear', 5: 'Surprise'}
    emotion = emotion_labels.get(predicted_class_id, "unknown")
    
    return emotion

