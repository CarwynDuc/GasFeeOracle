# gas-fee-oracle

decentralized gas fee monitoring and transaction timing advisor.

## problem

gas fees spike unpredictably. existing gas trackers are centralized websites. this is an on-chain alternative.

## solution

intelligent contract on genlayer that reads market conditions and estimates gas fee environment with AI-powered recommendations.

## usage

```
deploy: param = "test"
call:   check_fees()
```

## response

```json
{
  "fee_level": "NORMAL",
  "recommendation": "TRANSACT_NOW",
  "avg_fee": "15",
  "summary": "Moderate market activity suggests normal gas conditions."
}
```

## fee levels

| level | recommendation |
|-------|----------------|
| VERY_LOW | TRANSACT_NOW |
| LOW | TRANSACT_NOW |
| NORMAL | TRANSACT_NOW |
| HIGH | WAIT |
| EXTREME | URGENT_ONLY |

## how it works

`gl.nondet.web.render` → market data
`gl.nondet.exec_prompt` → ai analysis
`gl.eq_principle.strict_eq` → consensus

## deploy

genlayer studio → paste contract → param = test → deploy → check_fees

mit license · genlayer testnet bradbury
