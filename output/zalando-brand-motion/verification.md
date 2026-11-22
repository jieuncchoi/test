# Zalando Brand Motion — 제작 및 검증

| 구간 | 실제 구현 |
|---|---|
| 인트로, 프레임 0–49 | 첫 프레임부터 검정 공식 Wordmark SVG를 상단에 하드 컷으로 표시했다. 마진은 32.4px다. 첨부 PDF에서 추출한 여성 사진에 알파 마스크를 만들어 흰색 스튜디오 면에 배치했다. 머리 레이어가 워드마크 하단 일부를 가리며 워드마크를 식별할 수 있다. 사진 픽셀의 RGB와 인물 비율을 유지했고 눈 깜빡임은 적용하지 않았다. [Core Assets](https://brand.zalando.com/identity/motion/core-assets/) |
| 타이포그래피, 프레임 50–112 | 원본 인물 레이어가 오른쪽으로 이동하고, 1열 및 4행의 시작점 x=32.4px, y=548.1px에 “Style your way.”가 좌측 정렬된다. Zalando Sans Semi Expanded Regular(폭 112.5%, 굵기 400)를 사용했다. 마지막 다섯 문자에만 순차 등장과 ease-in을 적용하고 아웃트로에서 하드 컷했다. 타이밍과 동작은 브라우저 재현이며 공식 AE 프리셋 렌더가 아니다. [Motion Typography](https://brand.zalando.com/identity/motion/motion-typography/) |
| 아웃트로, 프레임 113–174 | 공식 Core Assets 페이지에 게시된 흰색 Outro with Wordmark in Sequence MP4에서 로고 구간을 직접 사용했다. 웹 영상의 도입부에 포함된 별도 예시 촬영 장면을 건너뛰고, 25fps 기준 45–106번 프레임을 사용했다. 원본 1280 × 720의 종횡비를 유지해 1920 × 1080으로 변환했다. 공식 시퀀스에서 브랜드마크와 워드마크는 서로 다른 프레임에 표시되며 마지막 프레임은 워드마크다. [Core Assets](https://brand.zalando.com/identity/motion/core-assets/) |

공식 16:9 HD Illustrator 가이드의 12열 × 6행 셀과 32.4px 마진 좌표를 사용했다. 공식 Grid System for Motion 페이지의 순차 로고 예시와 좌측 정렬 원칙을 적용했다. [Grid System for Motion](https://brand.zalando.com/identity/motion/grid-system-for-motion/)

첨부 AE ZIP과 공식 다운로드 패키지에서 모션 코어 및 타이포그래피 AEP를 확인했다. 현재 Linux 환경에 After Effects 또는 aerender가 없어 AEP를 실행하지 않았다. 실제 공식 영상 에셋을 쓴 부분은 아웃트로이며, 앞의 두 장면은 HTML/CSS/JavaScript로 구현했다.

25fps에서 4.5초 컷은 프레임 경계에 없으므로 4.52초에 전환했다. 최종 영상은 175프레임, 7.00초, 1920 × 1080, H.264이며 무음이다. 첫·마지막 PNG는 최종 MP4에서 직접 추출했다.

## 소스 실행

Python Playwright, Chromium, FFmpeg가 설치된 환경에서 `python render.py`를 실행한다. 컷아웃은 이미 포함되어 있다. 마스크를 재생성하려면 Pillow, NumPy, OpenCV가 설치된 환경에서 `python make-cutout.py`를 먼저 실행한다.
