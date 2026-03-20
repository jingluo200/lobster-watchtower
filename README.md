# Lobster Watchtower｜龙虾哨兵
## Natural-Language Onchain Alert Agent on OKX Onchain OS

Lobster Watchtower is a natural-language onchain alert agent built on **OKX Onchain OS + Claw**.

It turns user monitoring requests into structured watch rules, continuously checks target conditions, and triggers alerts when the configured threshold is met.

This project is not a market prediction bot.  
It is an agent that helps users automate onchain observation.

---

## Why this project exists

Many users do not actually need another long-form analysis report.

What they really need is an agent that can keep watching:

- a whale wallet
- a token contract
- exchange inflow / outflow activity
- a specific wallet becoming active again

The problem is not that this information is unavailable.  
The problem is that no one can keep watching all the time.

Lobster Watchtower is designed to solve exactly that problem.

It turns “keep watching this for me” into an executable monitoring task.

---

## Claw model & LLM version

- **Claw**: OpenClaw2026.3
- **LLM**: GPT5.4 / Gemini3.1 Pro
- **Runtime**: Windows 11 + Telegram integration

---

## One-line definition

**Lobster Watchtower is a natural-language onchain monitoring and alert agent.**

It uses **Claw** to compile user intent into structured watch rules, and **OKX Onchain OS** to execute the watch workflow and trigger alerts when conditions are met.

---

## Why OKX Onchain OS + Claw is essential

### Claw as watch-rule compiler

Claw is not just a chat interface here.  
It acts as a rule compiler that converts natural-language monitoring requests into machine-readable watch rules.

For example, a user can say:

> Watch this BTC whale address and alert me if it transfers out more than 500 BTC within 24 hours.

That request becomes a structured rule with fields such as:

- `watch_target`
- `asset`
- `time_window`
- `trigger_threshold`
- `event_type`
- `notification_channel`

Without Claw, the request remains vague human language.  
With Claw, it becomes an executable monitoring rule.

### OKX Onchain OS as execution layer

OKX Onchain OS is the layer that carries the monitoring workflow:

- checking the target state
- evaluating trigger conditions
- generating an alert
- writing event logs
- pushing notifications

Without OKX Onchain OS, this would be just a static query.  
With OKX Onchain OS, it becomes a repeatable alert workflow.

---

## Real problem, clear users, immediate utility

This project is built for a very practical use case:

> Users want to monitor onchain targets continuously without manually checking them all day.

### Target users

- traders who want to monitor whale activity
- researchers who track wallets and protocol behavior
- users who want instant alerts for specific onchain events
- builders who want a reusable watch-and-alert workflow

### Example scenarios

- whale wallet outflow alerts
- exchange inflow / outflow alerts
- token activity spike alerts
- watched wallet reactivation alerts

---

## Minimal demo scenario

The current demo focuses on one minimal scenario:

**Watch a BTC whale wallet and trigger an alert if the wallet transfers out more than 500 BTC within 24 hours.**

Workflow:

1. User submits a natural-language monitoring request
2. Claw compiles it into a structured watch rule
3. The agent continuously checks the target state
4. If the threshold is met, an alert is triggered
5. An event log is generated

---

## What the system checks

The current version checks fields such as:

- `target_valid`
- `window_valid`
- `threshold_matched`
- `event_detected`
- `alert_triggered`

This project is not about predicting the market.  
It is about notifying the user when a meaningful event has actually happened.

---

## Workflow

1. User writes a natural-language monitoring request
2. Claw compiles it into a structured watch rule
3. OKX Onchain OS executes the monitoring workflow
4. The system checks whether the target condition is met
5. If matched, an alert is triggered
6. An event log is recorded

This creates a configurable, repeatable, and explainable watch workflow.

---

## Key innovation

The innovation of Lobster Watchtower is not that it is “another alert bot”.

It has two useful ideas:

### 1. Natural-language monitoring configuration
Users do not need to manually write complicated filtering rules.  
They can describe what they want in plain language.

### 2. From static query to persistent observation
Most tools answer “what is happening now”.  
Lobster Watchtower is designed to answer a different question:

**“Tell me when this condition becomes true.”**

That makes it an observation agent, not just a query interface.

---

## Reproducibility

This repository is designed to be easy to reproduce.

It includes:

- prompt templates
- watch rule schema
- mock event data
- alert result examples
- reproducibility notes
- demo flow description

---

## Repository structure

```text
.
├── demo/
├── docs/
├── mock-data/
├── prompts/
├── schemas/
├── src/
├── README.md
└── package.json
