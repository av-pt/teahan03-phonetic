# teahan03-phonetic
Authorship Verification algorithm based on Teahan and Harper [2003] extended to use phonetic transcriptions.

## Notes
- This project uses [CLTS data](https://github.com/cldf-clts/clts) as a submodule. Use `git clone --recurse-submodules` for cloning the repository. If you already cloned the repository with `git clone`, run `git submodule update --init` to get the required submodules.  
- This project uses Pipenv. Alternatively, the modules in the Pipfile can be installed manually. Then `pipenv run` is not required anymore.
- You can either conduct cross-validation or use a standard train-test-split to evaluate the models. The cross-validation requires only one data file, as it splits the data into folds internally.


## Example commands
Initialize:
```
git clone --recurse-submodules ...

pipenv install
pipenv run python -m spacy download en_core_web_sm
```
Load the PAN20 data into the folder `teahan03-phonetic/data/raw/`

Run (cross-validation):
```
pipenv run python ba-util/transcribe.py -i data/raw/pan20-data.jsonl

python teahan03.py prep -i data/transcribed_<timestamp>/ -w data/raw/pan20-truth.jsonl 

python teahan03.py crossval -i data/prepared_<timestamp>/
```

Run (train-test-split):
```
pipenv run python teahan03.py prep -i data/raw/pan20-training-set.jsonl -w data/raw/pan20-truth.jsonl

pipenv run python teahan03.py train -i data/prepared/prepared_<timestamp>.txt

pipenv run python teahan03.py apply -i data/raw/pan20-test-set.jsonl -m data/model/model_<timestamp>.joblib

python3 pan20_verif_evaluator.py -i data/raw/pan20-authorship-verification-training-tiny-truth.jsonl -a data/answers.jsonl -o data/

```

## Flow Chart
[![A rendered picture of the first diagram described below.](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBkYXRhMVtQQU4yMCBUcmFpbmluZyBGaWxlXSAtLT4gb3JcbiAgICBkYXRhMSAtLT4gcHJvYzBcbiAgICBwcm9jMChbdHJhbnNjcmliZS5weV0pIC0tPiBkYXRhMFxuICAgIGRhdGEwW1RyYW5zY3JpYmVkIFBhbjIwIFRyYWluaW5nIEZpbGVzXSAtLT4gb3JcbiAgICBkYXRhMltQQU4yMCBUcnV0aCBGaWxlXSAtLT4gcHJvYzFcbiAgICBvcntvcn0gLS0-IHByb2MxXG4gICAgcHJvYzEoW3RlYWhhbjAzLnB5IHByZXBdKSAtLT4gZGF0YTNcbiAgICBkYXRhM1tcIlByZXBhcmVkIERhdGEgRmlsZShzKVwiXSAtLT4gcHJvYzJcbiAgICBzdWJncmFwaCBcIlRyYWluLVRlc3QtU3BsaXQgKE9ubHkgc2luZ2xlIGZpbGVzKVwiXG4gICAgcHJvYzIoW3RlYWhhbjAzLnB5IHRyYWluXSkgLS0-IGRhdGE0XG4gICAgZGF0YTRbVHJhaW5lZCBNb2RlbF0gLS0-IHByb2MzXG4gICAgZGF0YTVbUEFOMjAgVGVzdCBGaWxlXSAtLT4gcHJvYzNcbiAgICBwcm9jMyhbdGVhaGFuMDMucHkgYXBwbHldKSAtLT4gZGF0YTZcbiAgICBlbmRcbiAgICBkYXRhNltUZXN0IHNldCBhbnN3ZXJzXVxuICAgIGRhdGEzIC0tPiBwcm9jNFxuICAgIHN1YmdyYXBoIENyb3NzLVZhbGlkYXRpb25cbiAgICBwcm9jNChbdGVhaGFuMDMucHkgY3Jvc3N2YWxdKSAtLT4gZGF0YTdcbiAgICBlbmRcbiAgICBkYXRhN1tPdXQtb2YtZm9sZCBhbnN3ZXJzXSAtLT4gcHJvYzVcbiAgICBwcm9jNShbcGFuMjBfdmVyaWZfZXZhbHVhdG9yLnB5XSkgLS0-IGRhdGE4XG4gICAgZGF0YTYgLS0-IHByb2M1XG4gICAgZGF0YThbRXZhbHVhdGlvbiByZXN1bHRzXVxuXG4gICAgY2xhc3NEZWYgZGF0YSBmaWxsOiNmMmFjMzUsc3Ryb2tlOiMzMzM7XG4gICAgY2xhc3MgZGF0YTAsZGF0YTEsZGF0YTIsZGF0YTMsZGF0YTQsZGF0YTUsZGF0YTYsZGF0YTcsZGF0YTggZGF0YTtcbiAgICBjbGFzc0RlZiBwcm9jZXNzIGZpbGw6IzVkYjVlZixzdHJva2U6IzMzMztcbiAgICBjbGFzcyBvcixwcm9jMCxwcm9jMSxwcm9jMixwcm9jMyxwcm9jNCxwcm9jNSBwcm9jZXNzOyIsIm1lcm1haWQiOnt9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBkYXRhMVtQQU4yMCBUcmFpbmluZyBGaWxlXSAtLT4gb3JcbiAgICBkYXRhMSAtLT4gcHJvYzBcbiAgICBwcm9jMChbdHJhbnNjcmliZS5weV0pIC0tPiBkYXRhMFxuICAgIGRhdGEwW1RyYW5zY3JpYmVkIFBhbjIwIFRyYWluaW5nIEZpbGVzXSAtLT4gb3JcbiAgICBkYXRhMltQQU4yMCBUcnV0aCBGaWxlXSAtLT4gcHJvYzFcbiAgICBvcntvcn0gLS0-IHByb2MxXG4gICAgcHJvYzEoW3RlYWhhbjAzLnB5IHByZXBdKSAtLT4gZGF0YTNcbiAgICBkYXRhM1tcIlByZXBhcmVkIERhdGEgRmlsZShzKVwiXSAtLT4gcHJvYzJcbiAgICBzdWJncmFwaCBcIlRyYWluLVRlc3QtU3BsaXQgKE9ubHkgc2luZ2xlIGZpbGVzKVwiXG4gICAgcHJvYzIoW3RlYWhhbjAzLnB5IHRyYWluXSkgLS0-IGRhdGE0XG4gICAgZGF0YTRbVHJhaW5lZCBNb2RlbF0gLS0-IHByb2MzXG4gICAgZGF0YTVbUEFOMjAgVGVzdCBGaWxlXSAtLT4gcHJvYzNcbiAgICBwcm9jMyhbdGVhaGFuMDMucHkgYXBwbHldKSAtLT4gZGF0YTZcbiAgICBlbmRcbiAgICBkYXRhNltUZXN0IHNldCBhbnN3ZXJzXVxuICAgIGRhdGEzIC0tPiBwcm9jNFxuICAgIHN1YmdyYXBoIENyb3NzLVZhbGlkYXRpb25cbiAgICBwcm9jNChbdGVhaGFuMDMucHkgY3Jvc3N2YWxdKSAtLT4gZGF0YTdcbiAgICBlbmRcbiAgICBkYXRhN1tPdXQtb2YtZm9sZCBhbnN3ZXJzXSAtLT4gcHJvYzVcbiAgICBwcm9jNShbcGFuMjBfdmVyaWZfZXZhbHVhdG9yLnB5XSkgLS0-IGRhdGE4XG4gICAgZGF0YTYgLS0-IHByb2M1XG4gICAgZGF0YThbRXZhbHVhdGlvbiByZXN1bHRzXVxuXG4gICAgY2xhc3NEZWYgZGF0YSBmaWxsOiNmMmFjMzUsc3Ryb2tlOiMzMzM7XG4gICAgY2xhc3MgZGF0YTAsZGF0YTEsZGF0YTIsZGF0YTMsZGF0YTQsZGF0YTUsZGF0YTYsZGF0YTcsZGF0YTggZGF0YTtcbiAgICBjbGFzc0RlZiBwcm9jZXNzIGZpbGw6IzVkYjVlZixzdHJva2U6IzMzMztcbiAgICBjbGFzcyBvcixwcm9jMCxwcm9jMSxwcm9jMixwcm9jMyxwcm9jNCxwcm9jNSBwcm9jZXNzOyIsIm1lcm1haWQiOnt9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

```mermaid
graph TD
    data1[PAN20 Training File] --> or
    data1 --> proc0
    proc0([transcribe.py]) --> data0
    data0[Transcribed Pan20 Training Files] --> or
    data2[PAN20 Truth File] --> proc1
    or{or} --> proc1
    proc1([teahan03.py prep]) --> data3
    data3["Prepared Data File(s)"] --> proc2
    subgraph "Train-Test-Split (Only single files)"
    proc2([teahan03.py train]) --> data4
    data4[Trained Model] --> proc3
    data5[PAN20 Test File] --> proc3
    proc3([teahan03.py apply]) --> data6
    end
    data6[Test set answers]
    data3 --> proc4
    subgraph Cross-Validation
    proc4([teahan03.py crossval]) --> data7
    end
    data7[Out-of-fold answers] --> proc5
    proc5([pan20_verif_evaluator.py]) --> data8
    data6 --> proc5
    data8[Evaluation results]

    classDef data fill:#f2ac35,stroke:#333;
    class data0,data1,data2,data3,data4,data5,data6,data7,data8 data;
    classDef process fill:#5db5ef,stroke:#333;
    class or,proc0,proc1,proc2,proc3,proc4,proc5 process;
```