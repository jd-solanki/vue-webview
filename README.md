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
rm -rf build dist && pushd ../ui && npm run build-only && popd && pyinstaller build-linux.spec

# Test build
./dist/main
```
