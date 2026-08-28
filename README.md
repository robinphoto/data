# robinphoto data

사진 사이트들이 함께 사용하는 앨범 데이터와 커버 이미지 저장소입니다.

- `albums.json`: 앨범의 공통 사실 정보
- `church-categories.json`: 교회 사이트의 분류 정의
- `church-index.json`: 교회 사이트에서 사용할 앨범과 분류의 연결
- `covers/`: 앨범 커버 이미지

## 장소 배정 규칙

- 모든 앨범은 `place` 필드를 가집니다.
- 앨범명에 `제2성전`이 포함되면 `place: "second-temple"`로 자동 배정합니다.
- 그 밖의 장소는 확인된 앨범에 명시적으로 배정합니다.
