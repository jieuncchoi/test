# Zalando 사원증 브랜드 가이드 체크리스트

| 검증 | 결과 |
|---|---|
| 규격 | 두 PDF 모두 54 × 86mm, 세로 한 페이지다. 모서리 반경 3mm는 제작 선택이다. 개별 PNG는 638 × 1016px, 300dpi 메타데이터가 있다. 목업은 2880 × 1920px다. |
| A · Black | RGB #000000 바탕에 공식 오렌지 브랜드마크와 흰색 텍스트를 사용했다. 브랜드마크는 상단 좌측, 이름과 직함은 중단 좌측이다. [Primary colours](https://brand.zalando.com/identity/colour/colour-primary/) |
| B · Orange | 공식 RGB 오렌지 #FF4C00 바탕에 검정 텍스트와 공식 검정 워드마크를 사용했다. 워드마크는 너비 45mm, 카드 너비의 83.3%로 하단에 배치했다. [Primary colours](https://brand.zalando.com/identity/colour/colour-primary/) |
| 로고 형태와 보호공간 | 원본 SVG 종횡비를 유지했다. 브라우저에서 브랜드마크 높이 약 31.8 CSS px, 워드마크 높이 약 32.3 CSS px를 측정했다. 모두 가이드의 디지털 최소 높이(24px, 20px)를 넘고, 가장 가까운 카드 경계까지의 여백 4.5mm는 각각 로고 높이의 절반을 넘는다. [Brandmark](https://brand.zalando.com/identity/logo-system/brand-brand-mark/) · [Wordmark](https://brand.zalando.com/identity/logo-system/word-mark/) |
| 그리드 | 공식 정렬과 반 마진 거터 원칙을 참고해 카드에 맞춘 4.5mm 공통 마진, 2.25mm 거터와 6행을 사용했다. 직원 정보 시작점은 양쪽 모두 4행과 왼쪽 마진이다. 사원증 전용 공식 수치로 해석하지 않았다. [Grid System](https://brand.zalando.com/identity/layout/grid-system/) · [Identity System](https://brand.zalando.com/identity/identity-system/) |
| 타이포그래피 | “Alex Morgan”은 Zalando Sans Semi Expanded Regular 6.15mm, “Creative Director”는 Zalando Sans Regular 2.75mm다. 두 문구의 실제 브라우저 글리프와 PDF 텍스트를 확인했다. [Typography](https://brand.zalando.com/identity/typography/) |
| 목업과 인쇄 출력 | 같은 HTML 카드 레이어를 사용한다. 스튜디오 그림자와 표면 질감은 목업에서만 적용된다. PDF의 로고와 글꼴은 벡터로 유지했다. PDF는 RGB 완성면 기준이며 인쇄소 전용 CMYK 프로파일, 도련, 금형 검증은 포함하지 않았다. |

소스를 정적 HTTP 서버로 열면 양쪽 카드가 표시된다. 개별 보기는 `?card=black`과 `?card=orange`이다. Playwright, Chromium, PyMuPDF, Pillow가 설치되어 있으면 `python render.py`로 출력할 수 있다.
