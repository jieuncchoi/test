# Zalando Mobile Shopping UI

- 첫 화면은 1125 × 2436px이고 화면 안쪽 패딩은 80px이다. 편집 원본에서 Best Seller를 스크롤할 수 있다. 상품 세 칸은 약 305.67px 정사각형이며 거터는 24px이다. PNG와 PDF는 첫 화면 높이에서 똑같이 자르고, 상품 이름 일부는 아래로 이어진다.
- 캠페인 원본은 사용자 첨부 ZIP의 8001 × 4501px JPG다. 965 × 1700px 캠페인 영역에 비례 유지 크롭으로 적용했다. 헤드라인은 “Style on your way”이며 공식 Zalando Sans와 검정 Wordmark SVG를 사용했다.
- 아이콘 ZIP에는 개별 SVG 파일이 없었다. 내부 경로 `Zalando_Iconography16x16_MasterDoc.ai`의 UI–Icons 레이어에서 검정 벡터를 SVG로 내보냈다. 1부터 센 페이지 16은 Heart, 17은 Shopping Bag의 첫 번째 모양, 19는 Avatar의 첫 번째 모양이다. PDF 호환 레이어에서 개별 아트보드 명칭 문자열은 확인되지 않아 순서와 형태로 첫 번째 변형을 식별했다. 출력 경로는 `assets/wishlist-heart.svg`, `assets/shopping-bag-01.svg`, `assets/avatar-01.svg`다. 키 라인과 제작 가이드는 내보내기에서 제외했고, 16×16 아트워크 전체를 동일 비율로 확대했다. [Iconography](https://brand.zalando.com/identity/visual-assets/iconography/)
- 세 상품은 OpenAI 이미지 생성 도구로 한 스트립에 생성한 뒤 정사각형 세 장으로 분리했다. 상품 파일에는 사용자 인터페이스나 로고가 들어 있지 않다.
- PDF 한 페이지는 843.75 × 1827pt로, 96ppi 기준 PNG와 같은 화면 비율과 영역이다. 두 출력을 시각적으로 대조했다.
- 편집 소스는 스크롤·Wishlist 토글이 있는 화면 프로토타입이다. My Page와 Shopping Bag은 인터페이스 표현용이다. 재출력하려면 폴더에서 `python -m http.server 8782 --bind 127.0.0.1`을 실행한 후, Playwright·Chromium·PyMuPDF·Pillow 환경에서 `python render.py`를 실행한다.
