# Zalando — Friends under the sunshine | A3 검증

| 항목 | 적용과 검증 |
|---|---|
| A3 및 그리드 | 첨부 패키지에서 `250818_Zalando_Print_Grid Template_A3.indd`를 확인했다. 공개 인쇄 도해의 세로 A3는 8열 × 12행이다. InDesign 파일의 내부 좌표는 직접 읽지 못해 공개 도해의 행·열을 가로 방향으로 회전하고 요청 수치인 8.91mm 마진과 4.455mm 거터로 재구성했다. 최종 12열 × 8행 셀은 약 29.4329 × 31.0019mm다. [Grid System](https://brand.zalando.com/identity/layout/grid-system/) |
| Expressive와 들여쓰기 | 공식 예시의 큰 타이포그래피, 여백, 이미지와의 대비, 열 기준 들여쓰기를 적용했다. “Friends / under the / sunshine”의 세 줄은 1·2·3열 x=8.910, 42.798, 76.686mm에서 각각 좌측 정렬한다. 들여쓰기는 CSS 그리드 열 피치에서 산출한다. 줄마다 별도의 시작점은 요청에 따른 구성 선택이다. [Identity System](https://brand.zalando.com/identity/identity-system/) |
| 서체와 카피 | 헤드라인 32mm, 서브헤드 9mm에 Zalando Sans Semi Expanded Regular(폭 112.5%, 굵기 400)를 적용했다. Chromium에서 네 줄 모두 지정 WOFF2 글리프를 확인했다. 서브헤드 `12nn-18:00 04.02.2026`은 3열·7행에 배치했다. 헤드라인과 서브헤드의 문자열 및 텍스트 잘림 여부를 검증했다. [Core expression](https://brand.zalando.com/identity/typography/core-expression/) |
| 로고 정렬과 이격 | Equal weight 방식으로 검정 워드마크와 오렌지 브랜드마크를 독립 배치했다. 워드마크 왼쪽 x=8.91mm 및 브랜드마크 오른쪽 x=411.09mm를 마진에 맞췄고, 헤드라인 첫 줄은 워드마크의 왼쪽 모서리에 맞췄다. 브랜드마크 폭 23.76mm는 짧은 변의 8%이며, 높이 약 25.01mm는 워드마크 x-height의 두 배다. 워드마크는 약 84.36 × 16mm로 5mm 최소 높이를 넘고, 두 로고의 수평 간격 약 294mm는 워드마크 폭 두 배를 넘는다. 좌우 배치 설명이 상충하는 부분은 Placement 단락과 승인 도해를 우선했다. [Logo Mechanics](https://brand.zalando.com/identity/logo-system/logo-mechanics/) |
| 색상과 이미지 | 흰색 바탕, 검정 문구와 워드마크, 공식 오렌지 SVG를 적용했다. 오른쪽 사진은 8열·2행에서 시작하며 오른쪽·아래 마진을 따른다. 새로 생성한 남성 모델 한 명의 패션 사진에서 선글라스와 자연광이 명확히 보인다. 공식 사례의 인물 중심 구도를 참고했다. 별도 공개 Photography / Imagery 세부 규정은 확인하지 못했다. [Primary colours](https://brand.zalando.com/identity/colour/colour-primary/) · [Visual Assets](https://brand.zalando.com/identity/visual-assets/) |
| 렌더링과 출력 | 420 × 297mm 단일 페이지 PDF와 2100 × 1485px PNG를 시각적으로 대조했다. PDF에 임베드된 글꼴을 확인했고, 공식 SVG는 벡터로 내보냈다. 사진에 크롭만 적용했으며 그라디언트, 오버레이, 그림자 효과를 추가하지 않았다. 그리드는 검증용 PNG에만 표시된다. 원본 사진의 유효 해상도는 약 158ppi이며 인쇄 프로파일·도련·인쇄소별 적합성은 검증하지 않았다. |
