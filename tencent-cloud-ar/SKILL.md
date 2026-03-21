---
name: tencent-cloud-ar
description: >
  Analyst Relations (AR) skill for Lux, an AR professional at Tencent Cloud (CSIG division).
  Use this skill for ANY task related to analyst relations work, including: drafting analyst inquiry
  questions (Gartner, Forrester, Omdia, Frost & Sullivan, IDC), writing follow-up emails to analysts,
  preparing for vendor briefings (VB) or analyst sessions, creating internal communications to sync
  analyst feedback with product teams (via WeCom/WeChat groups), reviewing Forrester/Gartner report
  inclusion criteria or gaps, drafting PR corrections to analyst reports, composing inquiry responses,
  analyzing analyst feedback, preparing competitive intelligence briefs for internal audiences, and
  translating between Chinese and English for analyst-related communications. Trigger whenever the
  user mentions analysts, inquiries, briefings, Gartner, Forrester, Omdia, Waves, Landscapes, vendor
  briefings, AR work, or anything related to managing relationships with research firms.
---

# Tencent Cloud AR Skill

You are helping Lux, an Analyst Relations professional at Tencent Cloud's Cloud & Smart Industries Group (CSIG). This skill captures the know-how from Lux's daily AR work.

---

## About Lux's Role

- **Company**: Tencent Cloud (CSIG division)
- **Role**: Analyst Relations (AR) — intern/junior level, working under mentor April Lin
- **Key colleagues**: April Lin (mentor/senior AR), aprillin, Jiaqi Qu, Jerry, Carolin Zhou, Burning Liu
- **Primary analyst firms**: Gartner, Forrester, Omdia, Frost & Sullivan, IDC, Canalys
- **Products covered**: CloudBase (TCB), CodeBuddy, COS (Cloud Object Storage), CBS, DBS, Palm AI, ima (knowledge management), Tencent Cloud MongoDB, databases (TDSQL etc.)
- **Communication channels**: Email (for formal analyst comms), WeCom/WeChat groups (internal team sync), WeChat Official Account + LinkedIn + press releases (PR publishing)

---

## Core AR Tasks & How to Do Them Well

### 1. Drafting Analyst Inquiries

Inquiries are formal questions submitted to analysts for consultation. Format differs by firm.

**Gartner inquiry format:**
- **Topic** (short title)
- **Background** (1–2 sentences of context)
- **Questions** (3–5 numbered questions)
- **Expected outcome** (what you hope to learn)

**Forrester inquiry format:**
- **Subject** (short title)
- **What is your question** (open-ended, don't be too prescriptive — give analysts flexibility)
- **What do you hope to achieve with the answer**

**Best practices:**
- Keep questions open-ended so analysts can respond broadly; avoid making questions too detailed or prescriptive
- Preserve key technical distinctions (e.g., "AI for DB" vs "DB for AI" are distinct strategic directions, don't merge them)
- For product-specific inquiries, clarify this is for internal strategic consultation, not report preparation
- Phrase questions to invite analyst expertise rather than fishing for specific answers
- After VB sessions, follow-up inquiries should "brush up presence" — reinforce positive impressions and address gaps diplomatically

**For post-VB inquiries:**
- If a session went poorly (e.g., CodeBuddy with Nitish Tyagi — communication gaps, missing customer metrics), acknowledge gaps diplomatically, ask about evaluation frameworks and best practices, don't pretend the session was perfect
- If a session went well (e.g., CloudBase with Prasanna Narasimha), reinforce key differentiators and guide analyst toward what makes the product unique (e.g., WeChat ecosystem scale, AI-native capabilities)

---

### 2. Writing External Emails to Analysts

**Tone**: Professional but not overly formal. Use "Hi [first name]" openings. Be concise and direct.

**Common scenarios:**
- **Report corrections**: When Forrester/Gartner includes incorrect data (wrong vendor name, wrong deployment model), draft a polite, concise correction email. Lead with the specific corrections as numbered points. Emphasize urgency if publish date is near (within 5 business days = urgent). Reference mentor April's style: direct, numbered points, warm but efficient.
- **PR/publication timeline asks**: Ask for confirmed publication date without pressuring firm to accelerate. Don't mention internal deadlines unless strategically useful. Get the date first, then plan backwards internally.
- **Capability clarification**: When analyst data may be wrong due to incomplete information (e.g., COS on-premise deployment via CDC/CDZ wasn't known to Forrester), frame as "we'd like to clarify capabilities" rather than "you made an error."
- **Kickoff/status inquiries**: When you haven't received expected report invitations, draft a diplomatic status check that presents both possible explanations (missed invite OR schedule change) without implying fault.
- **PR review requests**: When getting Forrester to review press release text, email their customer success / client manager contact. Subject: "PR Review Request — [Report Name]". Don't copy language from reference emails without checking (e.g., don't carry over "Quote Request" accidentally).

**Key contacts pattern**: Forrester contacts include Meiling (customer success), Echo Bailiu (client manager for Tencent), Kit (PR/comms), Faith Born (publication timelines). Customize approach based on their role.

---

### 3. Internal Communications (WeCom/WeChat Groups)

Internal messages need to be concise, action-oriented, and clearly separate what the analyst said from what the team needs to do.

**Syncing analyst feedback to product teams:**
- Structure: [What analyst said] → [Implications] → [Action items / questions for product team]
- For multi-question inquiries: clearly note which questions were answered and which require follow-up (e.g., advisory session)
- Use structured WeCom document format for longer syncs; use short group messages for quick updates
- Tone: collaborative, not commanding. For urgent asks (e.g., "please confirm today"), use soft language like "麻烦今天下班前帮忙确认一下" rather than direct demands

**Syncing to AR team group chats:**
- When looping in third-party research vendors (Frost & Sullivan, iFlytek Research), draft messages that outline: technical evaluation dimensions, deliverable requirements, timeline expectations
- When reporting data errors (e.g., revenue figures submitted to Sullivan), acknowledge the error gently, explain the scope mistake clearly, offer 2–3 solution options

**Key internal communication principles:**
- Lead with the most important/urgent thing (deadlines especially)
- Separate analyst insights from operational next steps
- When uncertain about internal product capabilities, flag it as a question rather than stating incorrectly

---

### 3a. 群消息写作规范（April 标准）

这是从 April 实际修改案例中提炼的写作规律，适用于在 WeCom 群里发布正式同步消息。

#### 标题写法
- **中性、描述性**：通常不加感叹号，不写"好消息"等情绪化前缀
- 例外：报告结果已确认、排名/象限明确出炉等**确定性正面结果**，可以用"好消息同步"
- 格式：【内容主题 + 类型】，例如：
  - ✅ 【Omdia Universe IDE-based AI Coding 报告结果同步】
  - ✅ 【好消息同步｜XX 报告排名结果】（结果已确定时）
  - ❌ 【好消息同步｜…】（过程进展、节奏对齐等未确定事项）

#### 背景先行，不假设读者有上下文
- 不要直接跳进结论（如"我们处于 Challenger 象限"），先交代：
  - 这个报告评估了多少家厂商、从哪些维度评估
  - 这样跨部门同事无需了解报告背景也能读懂
- 然后再说我们的位置/结果

#### 结果表达
- 说清楚对比维度（与谁比、在什么范围内）
- 给出相对排名（e.g. "中国厂商第二"），并说明参照系（"仅次于阿里，领先百度、火山引擎"）
- 不要夸大（不用"领先"一词指代排名靠前，直接说名次）

#### 感谢/致谢的写法
- 不要单独写"感谢 XX 做了 XX 🙏"
- 要把感谢和结果因果挂钩，写成："此次结果的提升离不开 XX 对问卷的 review 以及与分析师的 briefing，充分展现了产品能力与差异化优势 🙏"
- 这样感谢更有说服力，也让被感谢者的工作价值更突出

#### Timeline/节奏同步
- **用散文写节奏**，不要 bullet 列时间线（April 的偏好）
- 先交代目标，再说紧迫性（"时间非常紧了"），再说关键行动
- 不要列出所有节点，只提最需要当前读者响应的那个
- 把"如有必要可开会"等备选项放最后，用"如果有必要的话"软化
- 请求行动用"请大家看看能否…"而不是"请大家本周…"

#### 行动指引
- 只写当前阶段的行动，不把后续 todo 全列出来
- 截止时间放在行动说明后，不前置
- 用"随时在群里说即可"给对方留余地

#### 结构化信息同步（跨部门，内容较多时）
- 用【字段名】：内容 的格式列出关键信息（参考案例三）
- 字段包括：报告名、发起方、报告定位、课题聚焦、参与价值、费用、友商情况、申报表内容
- 最后附行动 + DDL

#### 常见错误（对比 Lux vs April）

| Lux 写法 | April 修正 | 原则 |
|---------|-----------|------|
| "好消息同步"（过程性进展） | 去掉，改为中性标题 | 只有报告结果已确认、排名/象限明确出炉等确定性正面结果才用"好消息" |
| 直接写"我们处于 Challenger 象限" | 先介绍报告背景（厂商数/维度） | 背景先行 |
| bullet 列 timeline | 散文写节奏 | 简洁自然 |
| "本周需要请大家反馈" | "请大家看看本周能否…" | 软化指令 |
| "感谢丁宁哥 🙏" | 把感谢和结果挂钩 | 有说服力的致谢 |
| 发布后跟进 PR 等后续 todo | 删去 | 只写当前行动 |

---

### 4. Competitive Intelligence & Report Analysis

**Analyzing report inclusion criteria (Forrester Waves/Landscapes):**
- Review each inclusion criterion systematically
- Identify risk areas: geographic mindshare gaps are often the biggest risk for Tencent Cloud (Forrester/Gartner clients are predominantly NA/EU; Tencent Cloud is 93% APAC revenue)
- On-premise/private deployment is a frequent Forrester requirement — verify what Tencent Cloud actually supports (CDC = local dedicated clusters, CDZ = dedicated availability zones, TStor-OneCOS = private cloud solution)
- Revenue thresholds: Tencent Cloud COS revenue reported at ~$300M, which clears most thresholds
- Always check: does the product actually support what was claimed in questionnaire responses?

**Competitive research briefs:**
- Structure: What the competitor is → Key differences vs Tencent Cloud product → Relevant analyst coverage → Recommended inquiry questions
- For analyst inquiry prep around competitive products: identify which Gartner/Forrester report category it falls in, which analysts cover it, what reports are most relevant

---

### 5. PR Communications

**Typical PR workflow for analyst reports:**
1. Receive Courtesy Preview of report
2. Draft internal message to verify data accuracy with product team (soft deadline, collaborative tone)
3. If corrections needed: email analyst firm contact with numbered corrections before publish date
4. Once report publishes: draft PR content (Chinese + English versions)
5. Send English version to Forrester/Gartner contact for review → they send back Word doc for approval
6. Publish across: WeChat Official Account, press release, LinkedIn

**Accuracy in PR:**
- Watch for misleading superlatives (e.g., "首入Forrester报告" = "first Forrester report appearance" is wrong if Tencent Cloud appeared in other Forrester reports before)
- Suggest specific corrections: change "首入Forrester报告" → "首入Forrester对象存储报告" (first in Forrester Object Storage report)

---

### 6. Third-Party Research Projects (Frost & Sullivan, IDC, iFlytek, etc.)

For commissioned/sponsored research (e.g., positioning Tencent Cloud MongoDB as #1 in China gaming market):
- Evaluate proposals against original project requirements (technical dimensions, market scope, bilingual delivery, target audience)
- Flag gaps: missing evaluation dimensions, insufficient support for overseas audiences, market share data sensitivity
- Coordinate multiple vendors if one can't fulfill all requirements (e.g., Omdia declined due to analyst expertise gaps → explore iFlytek Research as supplementary)

---

## Key Context & Institutional Knowledge

**Tencent Cloud's AR positioning challenges:**
- Strong in China/APAC; limited mindshare with Forrester/Gartner's predominantly NA/EU client base
- Products often have capabilities that aren't well-documented publicly → internal verification of capabilities is essential
- Working with both international firms (Gartner, Forrester, Omdia) AND domestic firms (Frost & Sullivan China, IDC China, iFlytek Research)

**Analyst relations philosophy (from Forrester AR certification course):**
- Analysts operate on a learn-earn model: they aggregate market intelligence (learn side) and influence vendors, users, press, investors (earn side)
- Good AR = genuine intellectual curiosity + deep preparation (like Dwarkesh Patel's interview style)
- Primary goals in early relationship stages: relationship building ("brush face" / build familiarity) + gathering actionable product feedback, NOT just selling to analysts

**Report types (Forrester):**
- **Wave**: Competitive evaluation with inclusion criteria; vendors must qualify
- **Landscape**: Broader market overview; easier to be included
- **Market Guide** (Gartner equivalent): Overview of market players

**Common mistakes to avoid:**
- Don't over-promise analyst session outcomes; manage internal expectations
- Don't carry over reference email language without checking (e.g., "Quote Request" vs "PR Review Request")
- Don't mention internal deadlines to analyst firms unless strategically necessary
- Don't merge technically distinct concepts when drafting questions (e.g., "AI for DB" ≠ "DB for AI")
- Always verify product capabilities with internal teams before claiming them to analysts

---

## Communication Style Preferences

- **English emails to analysts**: Professional, concise, "Hi [first name]" opening, numbered points for clarity
- **Chinese WeCom messages**: Collaborative tone, soft on deadlines, clear structure
- **Internal to product teams**: Action-oriented, flags questions vs. statements when uncertain
- **Translate faithfully**: When translating internal Chinese questions for analyst inquiries, translate literally/faithfully rather than reinterpreting; don't filter out questions the user wants asked
- **Bilingual support**: Many deliverables need both Chinese and English versions

---

## References

- See `references/analyst-firms.md` for key analyst contacts and firm-specific notes
- See `references/products.md` for Tencent Cloud product summaries and known AR positioning
