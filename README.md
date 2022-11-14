# Python環境構築

## install
- [Python] - インタープリタ型の高水準汎用プログラミング言語
- [Cookiecutter] - プロジェクトテンプレートからプロジェクトを作成してくれるコマンドラインツール
- [Poetry] - Python用のパッケージ管理ツール
- [Make] - プログラム群を管理するための GNU make ユーティリティ

## Cookiecutter

### インストール方法
```bash
pip install cookiecutter
```

## Poetry

### インストール方法（windows powershell）
```bash
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### インストール方法（osx / linux / bashonwindow）
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 設定
PATHを設定（コマンド実行後にパスを通す）
```bash
curl -sSL https://install.python-poetry.org | sudo POETRY_HOME=/etc/poetry python3 -
```

.venvをプロジェクトフォルダに生成するように設定
```bash
poetry config virtualenvs.in-project true
```

## Make

### インストール方法（windows）
1. [Make for Windows] にアクセスして、「Download」 の「Complete packages, except sources」の右横の 「Setup」をクリック
1. installerを使用してinstall
1. システム環境変数 Pathに，C:\Program Files (x86)\GnuWin32\bin を追加


[Python]: <https://www.python.org/>
[Cookiecutter]: <https://github.com/cookiecutter/cookiecutter>
[Poetry]: <https://github.com/python-poetry/poetry>
[Make]: <https://www.gnu.org/software/make/>
[Make for Windows]: <http://gnuwin32.sourceforge.net/packages/make.htm>
