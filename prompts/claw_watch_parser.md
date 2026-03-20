# Claw Watch Parser Prompt

Convert the user's natural-language monitoring request into a structured watch rule.

You must extract:

- rule_id
- watch_target
- asset
- time_window
- trigger_threshold
- event_type
- notification_channel
- status
- created_at

Rules:
- preserve the user's monitoring intent
- use simple normalized field values
- if notification channel is not specified, default to "telegram"
- if status is not specified, default to "active"

Return JSON only.
