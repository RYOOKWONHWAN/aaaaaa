from google.cloud import translate_v3 as translate
import pandas as pd
# 인증 정보를 담은 JSON 파일의 경로
key_path = "python/second-kiln-384806-28671cedd298.json"

# Translation API 클라이언트 생성
client = translate.TranslationServiceClient.from_service_account_json(key_path)
df = pd.read_csv("python/data_2023-04-24/new_cast_data.csv")
text = df['name']
for i in range(1, 10):
    print(text[i])

    # # 부모 경로 생성

    response = client.translate_text(
        parent='projects/second-kiln-384806/locations/global',
        contents=[text[i]],
        mime_type='text/plain',
        source_language_code='ko',
        target_language_code='en-US')

    # 번역 결과 출력
    for translation in response.translations:
        print(translation.translated_text)
