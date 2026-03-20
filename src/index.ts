type WatchRule = {
  rule_id: string;
  watch_target: string;
  asset: string;
  time_window: string;
  trigger_threshold: number;
  event_type: string;
  notification_channel: string;
  status: string;
  created_at: string;
};

type AlertResult = {
  alert_id: string;
  rule_id: string;
  watch_target: string;
  event_type: string;
  observed_amount: number;
  threshold: number;
  window: string;
  alert_triggered: boolean;
  sent_to: string;
  timestamp: string;
};

const watchRule: WatchRule = {
  rule_id: "watch_rule_001",
  watch_target: "btc_whale_wallet_001",
  asset: "BTC",
  time_window: "24h",
  trigger_threshold: 500,
  event_type: "outflow",
  notification_channel: "telegram",
  status: "active",
  created_at: "2026-03-20T10:00:00Z"
};

const observedAmount = 742;

const alertResult: AlertResult = {
  alert_id: "alert_001",
  rule_id: watchRule.rule_id,
  watch_target: watchRule.watch_target,
  event_type: watchRule.event_type,
  observed_amount: observedAmount,
  threshold: watchRule.trigger_threshold,
  window: watchRule.time_window,
  alert_triggered: observedAmount >= watchRule.trigger_threshold,
  sent_to: watchRule.notification_channel,
  timestamp: "2026-03-20T12:10:00Z"
};

console.log("Watch rule:");
console.log(JSON.stringify(watchRule, null, 2));

console.log("\nAlert result:");
console.log(JSON.stringify(alertResult, null, 2));
