# Zalando FW25 가로형 OOH 검증

- **규격** — 실물 18,000 × 8,000mm, 비율 9:4. PDF 페이지는 1:10 축척인 1800 × 800mm이며, 발주 시 1000%로 출력해야 한다. PNG는 2700 × 1200px이다.
- **그리드** — 2.25:1은 극단형 기준인 3:1 미만이므로 Custom Format을 적용했다. 짧은 변의 3%인 240mm 마진과 그 절반인 120mm 거터, 14열 × 6행을 사용했다. 셀은 1140 × 약 1153.33mm다. [Grid System](https://brand.zalando.com/identity/layout/grid-system/)
- **OOH·Expressive** — 공식 FW25 실사용 예시의 큰 시즌 타이포그래피와 이미지 위계를 참고했다. 하단에 주요 정보를 배치하는 대신 사진의 왼쪽 여백에 FW25를 두었다. FW25의 왼쪽은 워드마크와 같은 x=240mm이며, 상단은 3행 시작점 y≈2786.67mm다. 얼굴, 의상, 의자와 겹치지 않는 것을 렌더에서 확인했다. 실제 설치 거리의 현장 가독성은 미검증이다. [Identity System](https://brand.zalando.com/identity/identity-system/)
- **로고** — 공식 검정 워드마크와 오렌지 브랜드마크를 상단 좌우에 분리 배치했다. Equal weight 방식으로 브랜드마크 폭은 짧은 변의 6%인 480mm, 높이는 워드마크 x-height의 두 배다. 워드마크는 약 1704 × 323mm이며 공통 수평 중심은 y≈493mm, 두 에셋 사이 간격은 약 15,336mm이다. 좌우 설명이 엇갈리는 부분은 배치 단락과 승인 도해를 따랐다. [Logo Mechanics](https://brand.zalando.com/identity/logo-system/logo-mechanics/)
- **서체** — 제공된 Zalando Sans Semi Expanded Regular WOFF2를 사용했다. 브라우저가 지정 글리프를 사용했고 PDF에서 임베드된 벡터 텍스트와 정확한 문구 FW25를 확인했다. 배너 내 다른 캠페인 카피는 없다. [Core Expression](https://brand.zalando.com/identity/typography/core-expression/)
- **사진 보존** — 첨부 ZIP의 PNG(2400 × 1350px)를 그대로 사용했다. OpenAI 이미지 생성 확장본에서 비어 있는 스튜디오 측면만 취해 왼쪽 520px과 오른쪽 122px을 이어 붙였다. 접합 보정은 원본 바깥에서만 적용했다. 상하 끝에 1px씩 이어 붙여 완성 이미지가 3042 × 1352px의 정확한 9:4가 되었다. 확장본의 (520, 1)부터 원본 영역 전체를 RGBA 바이트로 검증했고, 얼굴·자세·의상·의자 세 개가 모두 원본과 일치했다. PNG와 PDF 렌더를 시각적으로 대조했다.
- **인쇄 확인 범위** — 사진의 실물 유효 해상도는 약 4.3ppi다. 관람 거리별 적합성, CMYK 프로파일, 도련 및 출력 업체 사양은 확인하지 않았다.
