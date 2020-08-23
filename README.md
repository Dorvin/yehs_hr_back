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
| `api-token-auth/` | 로그인 토큰 조회 | POST |
| `event/` | 모든 행사 조회 | GET |
| `event/` | 행사(=1) 등록 | POST |
| `event/<int:pk>/` | 특정 행사(pk=pk) 조회 | GET |
| `event/<int:pk>/` | 특정 행사(pk=pk) 수정 | POST |
| `event/<int:pk>/` | 특정 행사(pk=pk) 삭제 | DELETE |
| `member/` | 모든 회원 조회 | GET |
| `member/` | 회원(>=1) 등록 | POST |
| `member/<string:code>/` | 특정 회원(code=code) 조회 | GET |
| `member/<string:code>/` | 특정 회원(code=code) 수정 | POST |
| `member/<string:code>/` | 특정 회원(code=code) 삭제 | DELETE |
| `register/<int:pk>/` | 특정 행사(pk=pk) 회원(>=1) 참가 등록 | POST |
| `success/` | 기간 중 조건 충족 회원 조회 | POST |

## REST API EXAMPLE
- api-token-auth/(POST)
    - request body
    ```
        {
            "username": "abcd",
            "password": "1234"
        }
    ```
    - response body
    ```
        {
            "token": "this is token"
        }
    ```
- event/(GET)
    - request body
    ```
    ```
    - response body
    ```
    # category should be one of ("academic", "volunteer", "society")
    # datae should be in the form(YYYYMM)
        [
            {
                "id": 1,
                "name": "cs seminar",
                "category": "academic",
                "date": "202008",
                "participants": [
                    {
                        "id": 1,
                        "code": "code1",
                        "name": "name1",
                        "email": "email1@gmail.com",
                        "phone": "010-1234-1234",
                        "yn": "1",
                        "fn": "1",
                        "univ": "SNU",
                        "major": "CS",
                        "events": [
                            {
                                "id": 1,
                                "name": "cs seminar",
                                "category": "academic",
                                "date": "202008"
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "code": "code2",
                        "name": "name2",
                        "email": "email2@gmail.com",
                        "phone": "010-1111-2222",
                        "yn": "1",
                        "fn": "1",
                        "univ": "SNU",
                        "major": "CS",
                        "events": [
                            {
                                "id": 1,
                                "name": "cs seminar",
                                "category": "academic",
                                "date": "202008"
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2,
                "name": "volunteer event",
                "category": "volunteer",
                "date": "202009",
                "participants": []
            },
            {
                "id": 3,
                "name": "society event",
                "category": "society",
                "date": "202010",
                "participants": []
            }
        ]
    ```
- event/(POST)
    - request body
    ```
    # category should be one of ("academic", "volunteer", "society")
    # datae should be in the form(YYYYMM)
    # empty name or category or date is not allowed
        {
            "name": "volunteer event2",
            "category": "volunteer",
            "date": "202011"
        }
    ```
    - response body
    ```
        {
            "id": 4,
            "name": "volunteer event2",
            "category": "volunteer",
            "date": "202011",
            "participants": []
        }
    ```
- event/4/(GET)
    - request body
    ```
    ```
    - response body
    ```
        {
            "id": 4,
            "name": "volunteer event2",
            "category": "volunteer",
            "date": "202011",
            "participants": []
        }
    ```
- event/4/(POST)
    - request body
    ```
    # just include what you want to change
    # anythings among ("name", "category", "date")
        {
            "name" : "hi"
        }
    ```
    - response body
    ```
        {
            "id": 4,
            "name": "hi",
            "category": "volunteer",
            "date": "202011",
            "participants": []
        }
    ```
- event/4/(DELETE)
    - request body
    ```
    ```
    - response body
    ```
    ```
- member/(GET)
    - request body
    ```
    ```
    - response body
    ```
    # code must be unique
        [
            {
                "id": 1,
                "code": "code1",
                "name": "name1",
                "email": "email1@gmail.com",
                "phone": "010-1234-1234",
                "yn": "1",
                "fn": "1",
                "univ": "SNU",
                "major": "CS",
                "events": [
                    {
                        "id": 1,
                        "name": "cs seminar",
                        "category": "academic",
                        "date": "202008"
                    }
                ]
            },
            {
                "id": 2,
                "code": "code2",
                "name": "name2",
                "email": "email2@gmail.com",
                "phone": "010-1111-2222",
                "yn": "1",
                "fn": "1",
                "univ": "SNU",
                "major": "CS",
                "events": [
                    {
                        "id": 1,
                        "name": "cs seminar",
                        "category": "academic",
                        "date": "202008"
                    }
                ]
            }
        ]
    ```
- member/(POST)
    - request body
    ```
    # code must be unique
    # len(member_infos) >= 1
    # at least code and name should be specified
    # that is, empty code or name is not allowed
        {
            "member_infos" : [
                    {
                        "code": "code111",
                        "name": "name111",
                        "email": "email111@gmail.com",
                        "phone": "010-1234-1222",
                        "yn": "2",
                        "fn": "2",
                        "univ": "SNU",
                        "major": "CS"
                    },
                    {
                        "code": "code222",
                        "name": "name222",
                        "email": "email222@gmail.com",
                        "phone": "010-1111-2223",
                        "yn": "2",
                        "fn": "2",
                        "univ": "SNU",
                        "major": "CS"
                    }
            ]
        }
    ```
    - response body
    ```
        [
            {
                "id": 3,
                "code": "code111",
                "name": "name111",
                "email": "email111@gmail.com",
                "phone": "010-1234-1222",
                "yn": "2",
                "fn": "2",
                "univ": "SNU",
                "major": "CS",
                "events": []
            },
            {
                "id": 4,
                "code": "code222",
                "name": "name222",
                "email": "email222@gmail.com",
                "phone": "010-1111-2223",
                "yn": "2",
                "fn": "2",
                "univ": "SNU",
                "major": "CS",
                "events": []
            }
        ]
    ```
- member/code222/(GET)
    - request body
    ```
    ```
    - response body
    ```
        {
            "id": 4,
            "code": "code222",
            "name": "name222",
            "email": "email222@gmail.com",
            "phone": "010-1111-2223",
            "yn": "2",
            "fn": "2",
            "univ": "SNU",
            "major": "CS",
            "events": []
        }
    ```
- member/code222/(POST)
    - request body
    ```
    # just include what you want to change
    # anythings among ("name", "email", "phone", "univ", "major")
        {
            "univ": "KAIST"
        }
    ```
    - response body
    ```
        {
            "id": 4,
            "code": "code222",
            "name": "name222",
            "email": "email222@gmail.com",
            "phone": "010-1111-2223",
            "yn": "2",
            "fn": "2",
            "univ": "KAIST",
            "major": "CS",
            "events": []
        }
    ```
- member/code222/(DELETE)
    - request body
    ```
    ```
    - response body
    ```
    ```
- register/2/(POST)
    - request body
    ```
    # len(codes) >= 1
    # code must be unique and present on database
        {
            "codes": [
                "code111",
                "code222"
            ]
        }
    ```
    - response body
    ```
        {
            "id": 2,
            "name": "volunteer event",
            "category": "volunteer",
            "date": "202009",
            "participants": [
                {
                    "id": 3,
                    "code": "code111",
                    "name": "name111",
                    "email": "email111@gmail.com",
                    "phone": "010-1234-1222",
                    "yn": "2",
                    "fn": "2",
                    "univ": "SNU",
                    "major": "CS",
                    "events": [
                        {
                            "id": 2,
                            "name": "volunteer event",
                            "category": "volunteer",
                            "date": "202009"
                        }
                    ]
                },
                {
                    "id": 4,
                    "code": "code222",
                    "name": "name222",
                    "email": "email222@gmail.com",
                    "phone": "010-1111-2223",
                    "yn": "2",
                    "fn": "2",
                    "univ": "SNU",
                    "major": "CS",
                    "events": [
                        {
                            "id": 2,
                            "name": "volunteer event",
                            "category": "volunteer",
                            "date": "202009"
                        }
                    ]
                }
            ]
        }
    ```
- success/(POST)
    - request body
    ```
    # start and end attributes must be specified
    # start <= date <= end
    # for academic, volunteer, society attributes, written number(n) means that to success at least n participation is required
    # for fn, 0 means don't care, for the other (n) It means that I want to get info about only member with fn = n
        {
            "start": "202002",
            "end": "202008",
            "academic": "1",
            "volunteer": "1",
            "society": "0",
            "fn": "250"
        }
    ```
    - response body
    ```
        [
            {
                "id": 1,
                "code": "code1",
                "name": "name1",
                "email": "email1@gmail.com",
                "phone": "010-1234-1234",
                "yn": "1",
                "fn": "1",
                "univ": "SNU",
                "major": "CS",
                "events": [
                    {
                        "id": 1,
                        "name": "cs seminar",
                        "category": "academic",
                        "date": "202008"
                    }
                ]
            },
            {
                "id": 2,
                "code": "code2",
                "name": "name2",
                "email": "email2@gmail.com",
                "phone": "010-1111-2222",
                "yn": "1",
                "fn": "1",
                "univ": "SNU",
                "major": "CS",
                "events": [
                    {
                        "id": 1,
                        "name": "cs seminar",
                        "category": "academic",
                        "date": "202008"
                    }
                ]
            }
        ]
    ```