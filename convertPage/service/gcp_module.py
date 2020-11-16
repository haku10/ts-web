from google.cloud import texttospeech
from google.cloud import storage
from pytz import timezone
from django.http import HttpResponse
from datetime import datetime
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import pathlib
import os

class gcp:
  @staticmethod
  def cloud_storage(mess):
    # 変換処理を行う
    response, filename = gcp.text_to_speech(mess)
    storage_client = storage.Client()
    bucket_name = "mp3_test_mm"
    bucket = storage_client.bucket(bucket_name)
    now = datetime.now(timezone('Asia/Tokyo'))
    name = now.strftime('%Y-%m-%d_%H%M%S.mp3')
    blob = bucket.blob(name)
    blob.upload_from_filename(filename)
    os.remove(filename)

  @staticmethod
  def text_to_speech(mess):
    # Instantiates a client
    print("変換処理を開始します。")
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=mess)
    
    # Build the voice request, select the language code ("en-US") and the ssm
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
      language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
      )

      # Select the type of audio file you want returned

    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
      )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
      input=synthesis_input, voice=voice, audio_config=audio_config
      )

    # The response's audio_content is binary.
    now = datetime.now(timezone('Asia/Tokyo'))
    filename = now.strftime('%Y-%m-%d_%H%M%S.mp3')
    with open(filename, 'wb') as fh:
      fh.write(response.audio_content)
      chunk_size = 8192
      response = StreamingHttpResponse(FileWrapper(open(filename, 'rb'), chunk_size), 
          content_type='audio/mpeg') 
      response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
      return response, filename
