# Zalando Brand Motion — 공식 영상 전체 유지

| 구간 | 프레임 | 적용 |
|---|---:|---|
| 공식 Intro | 0–109 | Core Assets 페이지의 흰색 `Intro_WHITE.mp4` 전체 110프레임을 원래 순서와 속도로 사용했다. |
| 모델과 마스트헤드 | 110–159 | `full-body-model.png`에 알파 마스크를 만들고 밝은 스튜디오 색으로 좌우 공간을 채웠다. 공식 검정 워드마크는 하드 컷으로 표시되며 머리 앞 레이어에 의해 일부 가려진다. 얼굴 형상과 인물 RGB는 보존했다. |
| 오렌지 이미지와 타이포그래피 | 160–222 | 첨부 ZIP에서 추출한 `antonius-harel-WsaPcg512jE-unsplash.jpg`를 비례 유지해 배치했다. `Style your way.`는 Zalando Sans Semi Expanded Regular를 사용한다. 마지막 다섯 문자에만 순차 ease-in을 적용하고 퇴장은 하드 컷으로 처리했다. |
| 공식 Outro | 223–332 | Core Assets 페이지의 흰색 `Outro_w_wordmark_WHITE.mp4` 전체 110프레임을 원래 순서와 속도로 사용했다. 마지막 프레임은 워드마크다. |

- **공식 사용** — Intro와 Outro 두 영상, 검정 Wordmark SVG, Zalando Sans WOFF2, 1920 × 1080 Illustrator 그리드(12열 × 6행). 공식 웹 영상은 1280 × 720, 25fps이고 동일 비율로 1920 × 1080에 맞췄다. 전체 영상 사용 결정에 따라 공식 에셋 안의 예시 촬영 장면도 양쪽에 포함된다. [Core Assets](https://brand.zalando.com/identity/motion/core-assets/) · [Grid System for Motion](https://brand.zalando.com/identity/motion/grid-system-for-motion/)
- **가이드 기반 재현** — Tail Animation은 HTML/CSS/JS에서 마지막 다섯 문자만 ease-in으로 드러나는 방식으로 구현했다. 공식 AE 템플릿은 확인했지만 After Effects/aerender가 없는 환경이라 AEP를 렌더하지 않았다. 세부 타이밍은 브라우저 구현 값이다. [Motion Typography](https://brand.zalando.com/identity/motion/motion-typography/) · [Choreography](https://brand.zalando.com/identity/motion/choreography/)
- **정렬** — Masthead는 마진 x=32.4px 및 y=32.4px, 제목은 같은 첫 열 x=32.4px 및 5행 y=720px에 맞췄다. 검증 PNG는 그리드가 표시된 타이포그래피 프레임이다.
- **미구현 항목** — 자연스러운 눈꺼풀 애니메이션을 독립적으로 구현할 수 있는 얼굴 리그가 없어 모델은 정지 사진으로 유지했다. 영상은 무음이다.
- **최종 규격** — 333프레임, 13.32초, 1920 × 1080, 25fps, H.264. 2.5초 타이포그래피는 프레임 경계상 2.52초로 배정했다. 첫·마지막 PNG는 인코딩된 영상에서 추출했다.

## 소스 재렌더링

Python Playwright, Chromium, FFmpeg가 있는 환경에서 `python render.py`를 실행한다. 모델 마스크는 ZIP에 포함되어 있다. 마스크를 다시 만들려면 Pillow, NumPy, OpenCV를 설치하고 `python make-matte.py`를 실행한다.
