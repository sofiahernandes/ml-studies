from gtts import gTTS

# english example
text_to_say = "This is a text to speech conversion example!"
language = "en"
gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)
gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")

# portuguese example
portuguese_text = "Eita, que bacana gente. Meu deus, que frase ridicula."
portuguese_language = "pt"
portuguese_gtts_object = gTTS(text = portuguese_text,
                          lang = portuguese_language,
                          slow = True)
portuguese_gtts_object.save("/content/portuguese.wav")

Audio("/content/portuguese.wav")