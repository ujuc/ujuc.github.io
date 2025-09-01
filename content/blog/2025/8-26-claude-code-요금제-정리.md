Title: Claude Code 요금제 정리
Date: 2025-08-26 19:26
Modified: 2025-09-01 15:19
Category: Chat
Tags: claude, 요금제
Slug: claude-code-요금제-정리
Summary: Team 과 Enterprise Plan에 Claude Code 을 사용할 수 있는 새로운 요금제가 생겨서 정리한다.

**Note**: 이 글은 지금 시점(2025/08/26)에 스냅샷일뿐 최신 내용은 [Claude Code Help Page][1]를 이용하자.

# TL;DR

- Claude for Work를 사용하고 있는 사용자에게 Premium seat로 변경하여 Claude Code를 사용할 수 있도록 하고, 사용할 수 있는 한도도 늘린 것으로 보인다.
  - 기존 Standard seat는 Pro plan과 동일한 한도이고, Claude Code 접근할 수 없음[^1].
- 개인 플랜(Pro, Max plan) 에서는 **오토 모델 스위칭** 기능이 있기에 온전히 Opus를 사용할 수는 없음. 그러나 Claude for Work에서는 오토 모델 스위칭 기능이 없음.
- 한도 도달시 개인 플랜은 **API로 인증을 해서 작업하거나 쉬어**야함. Claude for Work 에서는 **자동으로 API를 사용**하게되며, **관리자가 설정한 만큼만 과금**됨.

| **Plan**   | **요금**             | **Claude Code<br>사용 가능 모델** | **사용량 한도**<br>(5시간당)                                  | **추가 사항**                                                                                       |
| ---------- | -------------------- | --------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Pro        | $20/월               | Sonnet 4                          | Claude: 약 45 메시지<br>Claude Code: 약 10-40 프롬프트        | **주간 한도**<br>- Sonnet: 40-80시간                                                                |
| Max 5x     | $100/월              | Sonnet 4<br>Opus 4.1              | Claude: 약 225 메시지<br>Claude Code: 약 50-200 프롬프트      | **주간 한도**<br>- Sonnet: 140-280 시간<br>- Opus: 14-35 시간<br>**오토 모델 스위칭**: _20% 도달시_ |
| Max 20x    | $200/월              | Sonnet 4<br>Opus 4.1              | Claude: 약 800 메시지<br>Claude Code: 약 200-800 프롬프트     | **주간 한도**<br>- Sonnet: 240-480 시간<br>- Opus: 24-40 시간<br>**오토 모델 스위칭**: _50% 도달시_ |
| Team       | $150/월/Premium seat | Sonnet 4<br>Opus 4.1              | Claude: 약 225 메시지<br>Claude Code: Claude 사용 한도에 포함 | **주간 한도**<br>- Sonnet: 50-95 시간<br>- Opus: 3-7 시간                                           |
| Enterprise | 후불제               | Sonnet 4<br>Opus 4.1              | 어드민이 설정한 한도 만큼<br>(시간 제한 없음)                 | 토큰 요금으로 청구                                                                                  |

#### 수정 내용

- 25/09/01 - 오토 모델 스위칭 기능이 동작하는 모델에 대한 내용을 추가함.

---

# 공통 사항

- 사용량 한도는 Claude(Web, App) 과 Claude Code에서 사용한 메시지를 포함한다.
- 사용량은 5시간 동안 사용할 수 있는 한도치에 대해서 명시한다.
- Claude(Web, App)의 경우, 작성해 두었으나 언급되지 않은 것은 문서에 없는 내용이다.

## 사용량

- 메시지 수량은 메시지 길이, 대화 길이, 첨부파일에 따라 달라짐.
- Claude Code 사용량은 프로젝트 복잡성, 코드베이스 크기, 자동 수락 설정에 따라 달라짐.

# Individual

## Pro Plan

- 적합한 용도: 소규모 저장소 (1,000 줄 미만의 코드)에서 가벼운 작업 수행
- 요금: $20/월
- 모델
  - Claude: 모든 모델 서비스
  - Claude Code: Sonnet 4
- 사용 한도
  - Claude: 약 45 메시지
  - Claude Code: 약 10-40 프롬프트
- 주간 한도
  - Sonnet 4: 40-80 시간
- 한도 도달시
  - 한도가 풀릴때까지 쉬면 된다.
  - API로 변경해서 사용하면 된다.
  - 부족하다고 느끼면 Max Plan으로 변경하면 된다.

## Max Plan

- [Anthropic - Max Plan][2]
- 적합한 용도: 매일 사용하는 큰 코드베이스나 파워 유저 인 경우
- 한도 도달시
  - 한도가 풀릴때까지 쉬면 된다.
  - API로 변경해서 사용하면 된다.
- 오토 모델 스위칭
  - 쾌적한 환경을 유지하고 실수로 사용량 제한에 너무 빨리 도달하는 것을 방지하기 위해 Max Plan 사용자가 특정 사용량 임계값에 도달하면 클로드 코드가 자동으로 Opus -> Sonnet으로 전환한다.
  - 해당 기능은 `Default` 모델 선택시 자동으로 반영되어 동작하게된다. 명시적으로 모델 지정시에는 동작하지 않는다.

### 5x Pro

- 요금: $100/월
- 모델
  - Claude: 모든 모델 서비스
  - Claude Code: Sonnet 4, Opus 4.1
- 사용 한도
  - Claude: 약 225 메시지
  - Claude Code: 약 40-200 프롬프트
- 주간 한도
  - Sonnet: 140-280 시간
  - Opus: 14-35 시간
- 오토 모델 스위칭
  - 한도 사용량의 20%에 도달한 경우

### 20x Pro

- 요금: $200/월
- 모델
  - Claude: 모든 모델 서비스
  - Claude Code: Sonnet 4, Opus 4.1
- 사용 한도
  - Claude: 약 800 메시지
  - Claude Code: 약 200-800 프롬프트
- 주간 한도
  - Sonnet: 240-480 시간
  - Opus: 24-40 시간
- 오토 모델 스위칭
  - 한도 사용량의 50%에 도달한 경우

# Claude for Work

- 기존 Team & Enterprise Plan을 사용하고 있던 경우, [Premium seats][3]로 변경해야 Claude Code를 사용할 수 있다.

## 추가 사용한 토큰 요금

| **Model**                    | **Input** | **Output** | **Write Prompt Caching** | **Read Prompt Caching** |
| ---------------------------- | --------- | ---------- | ------------------------ | ----------------------- |
| Opus 4.1                     | $15/MTok  | $75/MTok   | $18.75/MTok              | $1.50/MTok              |
| Sonnet 4 (Prompt <= 200KTok) | $3/MTok   | $15/MTok   | $3.75/MTok               | $0.30/MTok              |
| Sonnet 4 (Prompt > 200KTok)  | $6/MTok   | $22.5/MTok | $7.50/MTok               | $0.60/MTok              |

- [Extra Usage Token Pricing][4]
- [Claude API Pricing][5]
- [Prompt caching][6]

## Team Plan

- [Anthropic - Team Plan][7]
- 요금: $150/월/[Premium seat][3]
- 모델
  - Claude: 모든 모델 서비스
  - Claude Code: Sonnet 4, Opus 4.1
- 사용 한도
  - Claude: 약 225 메시지
  - Claude Code: Claude 사용 한도에 포함.
- 주간 한도
  - Sonnet: 50-95 시간
  - Opus: 3-7 시간

## Enterprise Plan

- [Anthropic - Enterprise Plan][8]
- API를 직접 사용하는 것과 동일한 효과.
- 요금: 실제 사용 Token 비용에 대해서 월말에 청구.
- 모델: Team Plan과 동일
- 사용 한도 및 주간 한도: 어드민 사용자가 설정한 한도 만큼

# TMI

- Claude for Work 계정과 개인 계정은 다른 그룹으로 인식되기에 Plan을 변경할 수 없다[^2].

# 참고 문서

- [Anthropic - Pricing][9]
- [Anthropic - Team & Enterprise][10]
- [Anthropic - API][5]
- [Using Claude Code with your Pro or Max Plan][11]
- [Using Claude Code with your Team or Enterprise Plan][12]
- [Extra Usage for Claude for Work (Team and Enterprise)][13]

[1]: https://support.anthropic.com/en/collections/14445694-claude-code
[2]: https://www.anthropic.com/max
[3]: https://support.anthropic.com/en/articles/12004354-how-to-purchase-and-manage-premium-seats
[4]: https://support.anthropic.com/en/articles/12005970-extra-usage-for-claude-for-work-team-and-enterprise-plans#h_613f85e65b
[5]: https://www.anthropic.com/pricing#api
[6]: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
[7]: https://www.anthropic.com/team
[8]: https://www.anthropic.com/enterprise
[9]: https://www.anthropic.com/pricing
[10]: https://www.anthropic.com/pricing#team-&-enterprise
[11]: https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan
[12]: https://support.anthropic.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan
[13]: https://support.anthropic.com/en/articles/12005970-extra-usage-for-claude-for-work-team-and-enterprise-plans

[^1]: [About Claude for Work Team and Enterprise Plan Usage](https://support.anthropic.com/en/articles/9267304-about-claude-for-work-team-and-enterprise-plan-usage)

[^2]: [Can individuals with Pro or Max Plan accounts migrate to Claude for Work](https://support.anthropic.com/en/articles/9267400-can-individuals-with-pro-or-max-plan-accounts-migrate-them-to-claude-for-work-team-or-enterprise-plan-organizations)
