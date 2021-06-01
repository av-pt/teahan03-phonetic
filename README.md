# teahan03-phonetic
Authorship Verification algorithm based on Teahan and Harper [2003] extended to use phonetic transcriptions.

[![A rendered picture of the diagram described below.](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBkYXRhMVtQQU4yMCBUcmFpbmluZyBGaWxlXSAtLT4gcHJvYzFcbiAgICBkYXRhMltQQU4yMCBUcnV0aCBGaWxlXSAtLT4gcHJvYzFcbiAgICBwcm9jMShbdGVhaGFuMDMucHkgcHJlcF0pIC0tPiBkYXRhM1xuICAgIGRhdGEzW1ByZXBhcmVkIERhdGEgRmlsZV0gLS0-IHByb2MyXG4gICAgcHJvYzIoW3RlYWhhbjAzLnB5IHRyYWluXSkgLS0-IGRhdGE0XG4gICAgZGF0YTRbVHJhaW5lZCBNb2RlbF0gLS0-IHByb2MzXG4gICAgZGF0YTVbUEFOMjAgRXZhbHVhdGlvbiBGaWxlXSAtLT4gcHJvYzNcbiAgICBwcm9jMyhbdGVhaGFuMDMucHkgYXBwbHldKSAtLT4gZGF0YTZcbiAgICBkYXRhNltBbnN3ZXJzXVxuXG5cbiAgICBjbGFzc0RlZiBkYXRhIGZpbGw6I2YyYWMzNSxzdHJva2U6IzMzMztcbiAgICBjbGFzcyBkYXRhMSxkYXRhMixkYXRhMyxkYXRhNCxkYXRhNSxkYXRhNiBkYXRhO1xuICAgIGNsYXNzRGVmIHByb2Nlc3MgZmlsbDojNWRiNWVmLHN0cm9rZTojMzMzO1xuICAgIGNsYXNzIHByb2MxLHByb2MyLHByb2MzIHByb2Nlc3M7IiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBkYXRhMVtQQU4yMCBUcmFpbmluZyBGaWxlXSAtLT4gcHJvYzFcbiAgICBkYXRhMltQQU4yMCBUcnV0aCBGaWxlXSAtLT4gcHJvYzFcbiAgICBwcm9jMShbdGVhaGFuMDMucHkgcHJlcF0pIC0tPiBkYXRhM1xuICAgIGRhdGEzW1ByZXBhcmVkIERhdGEgRmlsZV0gLS0-IHByb2MyXG4gICAgcHJvYzIoW3RlYWhhbjAzLnB5IHRyYWluXSkgLS0-IGRhdGE0XG4gICAgZGF0YTRbVHJhaW5lZCBNb2RlbF0gLS0-IHByb2MzXG4gICAgZGF0YTVbUEFOMjAgRXZhbHVhdGlvbiBGaWxlXSAtLT4gcHJvYzNcbiAgICBwcm9jMyhbdGVhaGFuMDMucHkgYXBwbHldKSAtLT4gZGF0YTZcbiAgICBkYXRhNltBbnN3ZXJzXVxuXG5cbiAgICBjbGFzc0RlZiBkYXRhIGZpbGw6I2YyYWMzNSxzdHJva2U6IzMzMztcbiAgICBjbGFzcyBkYXRhMSxkYXRhMixkYXRhMyxkYXRhNCxkYXRhNSxkYXRhNiBkYXRhO1xuICAgIGNsYXNzRGVmIHByb2Nlc3MgZmlsbDojNWRiNWVmLHN0cm9rZTojMzMzO1xuICAgIGNsYXNzIHByb2MxLHByb2MyLHByb2MzIHByb2Nlc3M7IiwibWVybWFpZCI6e30sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

```mermaid
graph TD
    data1[PAN20 Training File] --> proc1
    data2[PAN20 Truth File] --> proc1
    proc1([teahan03.py prep]) --> data3
    data3[Prepared Data File] --> proc2
    proc2([teahan03.py train]) --> data4
    data4[Trained Model] --> proc3
    data5[PAN20 Evaluation File] --> proc3
    proc3([teahan03.py eval]) --> data6
    data6[Answers]


    classDef data fill:#f2ac35,stroke:#333;
    class data1,data2,data3,data4,data5,data6 data;
    classDef process fill:#5db5ef,stroke:#333;
    class proc1,proc2,proc3 process;
```