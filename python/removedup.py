import pandas as pd

# CSV 파일을 읽어옵니다.
df = pd.read_csv('data/cast_data.csv')
print(df.head(10))
# 열 이름이 존재하는지 확인합니다.
if 'id' in df.columns:
    count = len(df[df.duplicated(['id'])])
    print(f'중복된 값의 개수: {count}')
    # 중복된 값을 가진 행을 제거합니다.
    df.drop_duplicates(subset=['id'], inplace=True)


# 새로운 CSV 파일로 저장합니다.
    df.to_csv('1.csv', index=False)

else:
    print('열 이름이 존재하지 않습니다.')
