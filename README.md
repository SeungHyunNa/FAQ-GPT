# FAQ-GPT

## Virtual Environment Setup

```bash
python -m venv ./env
source ./env/bin/activate
```

## requirements.txt Install

```bash
pip install -r requirements.txt
```

### 최신 버전 설치하기

가능하면 최신 버전을 설치하는 것이 가장 좋습니다.
requirements.txt를 기반으로 새로운 환경을 만들고, 최신 버전으로 업데이트하는 방법을 추천합니다.
새로운 가상 환경을 만들고 최신 버전으로 설치:

```bash
python3 -m venv ./env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows (PowerShell)
pip install --upgrade pip
pip install -U $(awk '{print $1}' requirements.txt)
```

awk '{print $1}'는 패키지 이름만 추출하여 최신 버전을 설치합니다.

### 버전 호환성 확인하기

특정 버전이 필요한 경우, 공식 문서를 참고하여 최신 버전과의 호환성을 확인해야 합니다.
pip check 명령어를 사용하여 충돌하는 패키지를 찾을 수 있습니다.

```bash
pip check
```
