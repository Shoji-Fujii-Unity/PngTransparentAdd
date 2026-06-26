# PngTransparentAdd
- PNG に透明色を追加します。
- 透明色は画像の左上の 1 ドット（座標 (0, 0)）の RGB 色を基準にして扱います。
- さらに、同系色の範囲を指定するための許容値 `--tolerance` を指定できます。

## 使い方
```bash
python png_transparent_add.py input.png output.png --tolerance 5
```

## 開発
```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```