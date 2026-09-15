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

## 소년부 영상

- `videos.json`: 선별한 영상 정보. `juniors-index.json`에 같은 ID의 행사 분류를 등록합니다.
- `videos/연도/영상ID.jpg`: 유튜브에서 다운로드한 썸네일. `cover`에 이 상대 경로를 저장하며 유튜브 이미지에 실시간 연결하지 않습니다.
- 연도와 `startDate`는 게시일이 아닌 예배·행사 날짜 기준입니다. `publishedDate`는 별도로 보존합니다.
- `title`은 원본 제목의 첫 하이픈(-)부터 뒤를 삭제하고 양끝 공백을 제거합니다. `sourceTitle`은 원본을 보존하며 분류는 원본 제목으로 판단합니다. 하이픈이 없으면 제목 전체를 사용합니다. `subtitle`은 사용하지 않습니다.
- `durationSeconds`는 초 단위이며 미확인 시 null입니다. `youtube-영상ID`를 고유 ID로 사용해 중복을 피합니다.
- 수동 수정한 title은 화면에서 다시 가공하지 않습니다.

- `juniors-video-categories.json`: 영상 탭 전용 분류. 사진 분류는 `juniors-categories.json`으로 별도 관리합니다. 영상의 분류 연결은 기존 `juniors-index.json`을 사용합니다.
