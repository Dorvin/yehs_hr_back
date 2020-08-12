# yehs_hr_back

## Dependency
1. venv 설치
    - virtualenv==16.4.3
1. venv 생성
    - virtualenv .env
1. venv 구동
    - source .env/bin/activate
1. 의존성 설치
    - pip3 install -r requirements.txt
1. 의존성 추가시
    - pip3 freeze > requirements.txt

## REST API guide
| path | function | method |
|:---|:---:|---:|
| `admin/` | 관리자 페이지 | GET |
