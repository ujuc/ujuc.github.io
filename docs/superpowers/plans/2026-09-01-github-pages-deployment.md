# GitHub Pages 네이티브 배포 전환 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 현재 uv·서브모듈 빌드를 유지하면서 PAT와 `master` 배포 브랜치를 GitHub Pages 네이티브 artifact/OIDC 배포로 교체한다.

**Architecture:** `build` 작업이 테스트와 Pelican 빌드를 수행한 뒤 `output/`을 Pages artifact로 업로드한다. 별도 `deploy` 작업이 GitHub OIDC 권한으로 artifact를 배포한다.

**Tech Stack:** GitHub Actions, uv, Pelican 4.12, `actions/upload-pages-artifact`, `actions/deploy-pages`

**Spec:** 이 대화에서 승인된 항목 5의 별도 CI 전환 범위

## Global Constraints

- `clean` Git 서브모듈의 재귀 checkout을 유지한다.
- `uv sync --locked`로 `uv.lock` 재현성을 유지한다.
- 배포 전에 단위 테스트, Ruff, ty, Pelican warning 검사를 통과해야 한다.
- GitHub 저장소 설정 변경, workflow 수동 실행, secret 삭제는 각각 실행 전에 명시적 승인을 받는다.
- Giscus와 Utterances 설정은 변경하지 않는다.

---

### Task 1: 배포 전 품질 게이트 확정

**Files:**
- Modify: `.github/workflows/gh-pages.yml`
- Test: `tests/test_cli.py`

**Interfaces:**
- Consumes: `uv.lock`, `publishconf.py`, `clean` 서브모듈
- Produces: 배포 artifact를 만들기 전에 실행할 고정 검증 명령

- [ ] **Step 1: 현재 로컬 검증 기준 확인**

Run:

```bash
uv sync --locked
uv run python -m unittest discover -s tests -v
uv run ruff check cli/main.py pelicanconf.py publishconf.py tests
uv run ruff format --check cli/main.py pelicanconf.py publishconf.py tests
uv run ty check cli/main.py pelicanconf.py publishconf.py tests
```

Expected: 모든 명령이 상태 코드 0으로 종료한다.

- [ ] **Step 2: Pelican 경고를 실패로 처리해 확인**

Run:

```bash
uv run python -m pelican content -s publishconf.py --fatal warnings
```

Expected: 전체 글을 경고 없이 생성하고 상태 코드 0으로 종료한다.

- [ ] **Step 3: workflow의 빌드 단계에 같은 검증 명령 추가**

`.github/workflows/gh-pages.yml`의 `Build posts` 전에 다음 단계를 둔다.

```yaml
      - name: Check Python
        run: |
          uv run python -m unittest discover -s tests -v
          uv run ruff check cli/main.py pelicanconf.py publishconf.py tests
          uv run ruff format --check cli/main.py pelicanconf.py publishconf.py tests
          uv run ty check cli/main.py pelicanconf.py publishconf.py tests

      - name: Build posts
        run: uv run python -m pelican content -s publishconf.py --fatal warnings
```

- [ ] **Step 4: 변경을 검토 가능한 단위로 커밋**

```bash
git add .github/workflows/gh-pages.yml
git commit -m "ci: 배포 전 Python 및 Pelican 검증 추가"
```

### Task 2: 브랜치 push 배포를 Pages artifact 배포로 교체

**Files:**
- Modify: `.github/workflows/gh-pages.yml`

**Interfaces:**
- Consumes: `build` 작업이 만든 `output/`
- Produces: 이름이 `github-pages`인 artifact와 Pages deployment URL

- [ ] **Step 1: workflow 트리거와 권한 교체**

`cli/**`와 `.github/**` 변경도 검증되도록 `paths-ignore`를 제거하고 다음 권한을 선언한다.

```yaml
on:
  push:
    branches: [develop]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false
```

- [ ] **Step 2: 기존 빌드 절차 유지 후 artifact 업로드**

`checkout`, `setup-uv`, `uv sync --locked`, 품질 검사, 빌드, `ads.txt` 생성을 유지하고 기존 `peaceiris/actions-gh-pages` 단계를 다음으로 교체한다.

```yaml
      - name: Configure Pages
        uses: actions/configure-pages@v5

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: output
```

- [ ] **Step 3: 별도 deploy 작업 추가**

```yaml
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 4: workflow 정적 검토**

Run:

```bash
git diff --check
git diff -- .github/workflows/gh-pages.yml
```

Expected: whitespace 오류가 없고 `personal_token`, `publish_branch`, `peaceiris`가 남아 있지 않다.

- [ ] **Step 5: 배포 전환을 별도 커밋**

```bash
git add .github/workflows/gh-pages.yml
git commit -m "ci: GitHub Pages 네이티브 배포로 전환"
```

### Task 3: GitHub Pages 저장소 설정 전환

**Files:**
- Modify: GitHub 저장소의 Pages 설정

**Interfaces:**
- Consumes: Task 2의 `github-pages` artifact
- Produces: `https://ujuc.github.io` Pages deployment

- [ ] **Step 1: 사용자에게 외부 설정 변경 승인 요청**

변경 대상은 저장소 **Settings → Pages → Build and deployment → Source**이다. 승인 전에는 설정을 변경하거나 workflow를 수동 실행하지 않는다.

- [ ] **Step 2: Pages Source를 GitHub Actions로 변경**

승인 후 Source를 `Deploy from a branch`에서 `GitHub Actions`로 바꾼다.

- [ ] **Step 3: workflow_dispatch로 최초 배포 실행**

승인 후 `gh-pages.yml`을 한 번 수동 실행하고 `build`와 `deploy` 작업이 모두 성공하는지 확인한다.

- [ ] **Step 4: 배포 결과 검증**

다음을 확인한다.

```text
https://ujuc.github.io/
https://ujuc.github.io/feeds/rss.xml
https://ujuc.github.io/2026/01/01/v39-26-0/
https://ujuc.github.io/ads.txt
```

Expected: HTTP 200이며 CSS, 내부 글 링크, RSS, 광고 파일이 정상이다.

### Task 4: 레거시 배포 자원 정리와 롤백 확인

**Files:**
- Modify: GitHub Actions repository secrets
- Preserve: `master` 브랜치(안정화 기간 동안 롤백용)

**Interfaces:**
- Consumes: 성공한 네이티브 Pages 배포
- Produces: PAT 없는 배포 구성과 명시적인 롤백 경로

- [ ] **Step 1: 안정화 후 secret 삭제 승인 요청**

최소 한 번의 자동 push 배포까지 확인한 뒤 `PERSONAL_TOKEN` 삭제 승인을 별도로 요청한다.

- [ ] **Step 2: 승인 후 사용하지 않는 secret 삭제**

`PERSONAL_TOKEN`이 다른 workflow에서 사용되지 않는지 검색한 후 삭제한다.

- [ ] **Step 3: 롤백 절차 기록**

배포 실패 시 다음 순서로 되돌린다.

```text
1. GitHub Pages Source를 기존 master 브랜치 방식으로 복원한다.
2. Task 2의 workflow 커밋을 revert한다.
3. master의 마지막 정상 output으로 즉시 서비스를 복구한다.
4. 새 글 배포도 필요하면 PAT를 다시 발급·등록한 뒤 기존 peaceiris 배포를 실행한다.
```

- [ ] **Step 4: 안정화 후 master 배포 브랜치 정리 여부 결정**

브랜치 삭제는 이 계획의 자동 실행 범위에 포함하지 않는다. 충분한 안정화 뒤 별도 승인을 받아 처리한다.
