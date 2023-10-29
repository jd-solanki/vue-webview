# Vue WebView

## Get Started

```bash
# Installation
pushd ui && npm i && popd
cd webview
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Development
python app/main.py

# Build
rm -rf build dist && pushd ../ui && npm run build-only && popd && pyinstaller --noconsole --onefile --windowed app/main.py

# Test build
./dist/main
```
