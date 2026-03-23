# OKX Onchain OS Macro Regime Mapper

A natural-language agent for reading onchain market regimes.

## Overview

OKX Onchain OS Macro Regime Mapper is an AI agent that turns broad macro questions into structured onchain analysis tasks and returns a readable market regime.

Instead of generating direct trading signals, it helps users understand whether onchain capital is currently deploying, rotating, hiding, or fading.

## Core Idea

Most onchain tools answer local questions.

This project focuses on a higher-level one:

**What kind of market are we actually in?**

Using Claw for intent parsing and OKX Onchain OS for workflow orchestration, the system maps user questions into regime classifications such as:

- Risk Expansion
- Risk Rotation
- Defensive Parking
- Narrative Exhaustion

## Example Questions

- Is the market currently in risk expansion or defensive parking?
- Are stablecoins being redeployed into risk or staying idle?
- Is this ecosystem attracting sticky capital or short-term speculative traffic?
- Is current activity broadening into real participation or fading into narrative exhaustion?

## Workflow

1. User enters a natural-language macro question
2. Claw parses the intent into structured analysis targets
3. OKX Onchain OS routes the analysis workflow
4. Internal regime engine maps signal combinations into regime states
5. Report formatter returns a concise human-readable explanation

## Repository Contents

- `prompts/` prompt design
- `config/` sample inputs
- `src/` simple demo logic
- `demo/` example questions and outputs
- `assets/` cover image

## Reproducibility

This repo includes:
- prompt structure
- sample workflow
- example inputs
- demo outputs
- runnable Python demo

## Internal Note

Built with OKX Onchain OS + Claw  
Lobster is used here only as the internal engine label.
