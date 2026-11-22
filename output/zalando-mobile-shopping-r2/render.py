"""Capture the first viewport of the scrollable shopping design."""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

import fitz
from PIL import Image
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent
with TemporaryDirectory() as temp, sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
    page = browser.new_page(viewport={'width':1125,'height':2436},device_scale_factor=1)
    page.goto('http://127.0.0.1:8783/',wait_until='networkidle')
    page.evaluate("async()=>{await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode()));}")
    result=page.evaluate("""() => {
      const screen=document.querySelector('.screen'), cards=[...document.querySelectorAll('.product-image')];
      return { height: screen.clientHeight, scroll:screen.scrollHeight,
        headline:document.querySelector('h1').textContent,
        cards: cards.map(e=>[e.getBoundingClientRect().x,e.getBoundingClientRect().width,e.getBoundingClientRect().height]) };
    }""")
    print(result)
    assert result['height']==2436 and result['headline']=='Style on your way'
    assert len(result['cards'])==3
    assert max(x[1] for x in result['cards'])-min(x[1] for x in result['cards'])<.02
    assert all(abs(w-h)<.02 for _,w,h in result['cards'])
    page.screenshot(path=str(root/'zalando-mobile-shopping_R2.png'))
    intermediate=Path(temp)/'print.pdf'
    page.pdf(path=str(intermediate),prefer_css_page_size=True,print_background=True)
    with fitz.open(intermediate) as src,fitz.open() as pdf:
        assert len(src)==1
        sheet=pdf.new_page(width=1125*.75,height=2436*.75)
        sheet.show_pdf_page(sheet.rect,src,0,keep_proportion=False)
        assert 'Best Seller' in sheet.get_text()
        pdf.save(root/'zalando-mobile-shopping_R2.pdf',garbage=4,deflate=True)
        sheet.get_pixmap(matrix=fitz.Matrix(.45,.45)).save('/tmp/ui-pdf-view.png')
im=Image.open(root/'zalando-mobile-shopping_R2.png')
assert im.size==(1125,2436)
im.thumbnail((440,960));im.save('/tmp/ui-r2-view.png')
