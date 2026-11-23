# Film Green Book (Streamlit)

`index.html`(업로드하신 화면 그대로)를 Streamlit으로 여는 래퍼 앱입니다. 화면과 계산은 모두 `index.html` 안에서 동작하고, `app.py`는 그 파일을 Streamlit 페이지에 담아 보여줍니다.

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| `app.py` | `index.html`을 Streamlit 화면에 표시 |
| `index.html` | 앱 본체 (화면, 계산, 주소 검색 전부) |
| `requirements.txt` | 필요한 패키지 (streamlit) |
| `.streamlit/config.toml` | 민트 배경 테마 |

화면을 고치고 싶으면 `index.html`만 수정해서 다시 올리면 됩니다. `app.py`는 건드릴 필요가 없습니다.

## 내 컴퓨터에서 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

## GitHub + Streamlit Community Cloud로 열기

1. GitHub에서 새 저장소를 만들고 이 폴더의 파일 전체를 올립니다. `.streamlit` 폴더도 함께 올려야 합니다. 웹에서는 Add file → Upload files로 끌어다 놓으면 됩니다.
2. [share.streamlit.io](https://share.streamlit.io)에 GitHub 계정으로 로그인합니다.
3. **Create app → Deploy a public app from GitHub**를 선택합니다.
4. Repository는 방금 만든 저장소, Branch는 `main`, Main file path는 `app.py`로 지정하고 **Deploy**를 누릅니다.
5. 몇 분 뒤 `https://<앱이름>.streamlit.app` 주소가 생깁니다.

## 참고

- 앱 설치(PWA) 기능은 Streamlit 안에서는 동작하지 않습니다. 설치형이 필요하면 GitHub Pages로 올리는 방식을 쓰세요.
- 카카오 키 같은 설정은 브라우저에 저장되므로 기기마다 다시 입력해야 할 수 있습니다.
