from django.http import JsonResponse
from .inference import predict_emotion

def emotion_detection(request):
    text = request.GET.get('text', None)
    
    if text:
        emotion = predict_emotion(text)
        return JsonResponse({"Post": text, "emotion": emotion}, status=200)
    
    # Default array of sentences to analyze when no text is provided
    default_sentences = [
        "I am very happy today!",
        "I am feeling sad and down.",
        "This is so exciting!",
        "I am extremely angry right now.",
        "I feel so peaceful and relaxed.",
        "Walking through the empty park, she felt the weight of the world on her shoulders. The once vibrant trees now stood bare, their branches reaching out like skeletal fingers. The distant laughter of children, now just a memory, echoed faintly in her mind. She passed by the old bench where they used to sit and talk for hours, its paint now chipped and weathered. The wind whispered through the leaves, carrying with it the scent of the roses he used to bring her. As she approached the pond, the ripples on the water seemed to mirror the turmoil in her heart. She stood there for a moment, staring at her reflection, feeling the overwhelming sense of loss and longing wash over her."
    ]
    
    default_emotions = []
    for sentence in default_sentences:
        emotion = predict_emotion(sentence)
        default_emotions.append({"Post": sentence, "emotion": emotion})
    
    return JsonResponse({"default_emotions": default_emotions}, status=200)
