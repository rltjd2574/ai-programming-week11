# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV 파일을 읽어 유효한 (이름, 점수) 목록과 제외한 행의 기록을 반환합니다.

0~100의 정수 점수를 보관하며, 중복 이름은 그대로 유지합니다. 쉼표가 포함된 이름도 따옴표로 감싸져 있으면 읽을 수 있습니다. 잘못된 행은 이유와 함께 기록하고, 빈 줄은 무시합니다.

평균과 학점 계산 기능은 포함하지 않습니다.

## ② 왜 만들었나요 (Why)

성적 파일에는 빈칸이나 잘못된 점수가 섞여 있을 수 있습니다. 정상적인 행은 계속 읽고, 제외한 행은 이유를 확인할 수 있도록 처리하는 방법을 연습하기 위해 만들었습니다.

## ③ 어떻게 쓰나요 (How)

Python과 pip가 필요합니다. 저장소 폴더의 Windows PowerShell에서 다음 명령을 순서대로 실행합니다.

```powershell
python --version
python -m pip install --user -U "pytest~=7.0" pytest-cov
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD="1"
python load_scores.py scores.csv
```

새 PowerShell 터미널을 열면 테스트 전에 환경변수 설정 명령을 다시 실행합니다.

scores.csv 실행 결과: 읽은 줄 5개 / 건너뛴 줄 5개.

## ④ 어떻게 테스트하나요

기본 테스트와 보강 테스트를 실행합니다.

```powershell
python -m pytest test_load_scores.py -q
```

확인한 결과: 12 passed (기본 11개 + weird.csv 보강 1개).

커버리지는 다음 명령으로 확인합니다.

```powershell
python -m pytest test_load_scores.py -p pytest_cov --cov=load_scores --cov-report=term-missing
```

보강 전 Cover는 76%, Missing은 55-56, 77-86이었습니다.
보강 후 Cover는 80%, Missing은 77-86이었습니다.
남은 부분은 파일을 직접 실행할 때 동작하는 명령행 처리·출력 코드입니다.

AI 비교 실험은 별도로 실행합니다.

```powershell
python -m pytest test_bug_A.py -q
python -m pytest test_bug_B.py -q
```

- A 결과: 1 failed, 2 passed. 마지막 원소가 최댓값인 입력에서 버그를 발견했습니다.
- B 결과: 4 passed. 마지막 원소를 놓치는 버그를 드러내는 입력이 없어 버그를 발견하지 못했습니다.

A/B 파일은 AI 응답을 보관한 비교용 테스트입니다. A의 실패는 의도적으로 제공된 bug3_logic.py의 버그를 검출한 결과이며, 테스트와 구현은 수정하지 않았습니다. 전체 테스트를 한꺼번에 실행하면 이 실패도 포함됩니다.

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | 성적 CSV를 읽어 (kept, skipped)를 반환 |
| scores.csv | 정상 행과 잘못된 행이 섞인 데이터 |
| empty.csv | 헤더만 있는 데이터 |
| weird.csv | 이름 누락 등 추가 검증용 데이터 |
| test_load_scores.py | 기본 11개 항목과 보강 테스트 1개 |
| bug3_logic.py | 마지막 원소를 검사하지 않는 버그가 있는 비교 실험용 함수 |
| test_bug_A.py | 구현 코드를 제공하여 생성한 AI 테스트 |
| test_bug_B.py | 명세를 제공하여 생성한 AI 테스트 |
| prompts.txt | 실험 요청문 |
| README.md | 실행 및 테스트 안내 |
| LICENSE | MIT 라이선스 |
| .gitignore | Git 추적 제외 설정 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람: 박기성
- 사용한 AI: VS Code Copilot Chat(Ask)의 Copilot Fusion (gpt-5.6-luna)
- AI에게 도움받은 부분: 테스트 코드, 실행 방법, A/B 비교 테스트 생성
- 직접 수행한 부분: 파일 저장, 명령 실행, 출력과 기대값 대조, 문서 작성, 실패 및 커버리지 결과 확인

## 라이선스

MIT License (LICENSE 파일 참고)