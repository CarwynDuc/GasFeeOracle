# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class GasFeeOracle(gl.Contract):
    has_scanned: bool
    fee_level: str
    recommendation: str
    analysis: str
    param: str

    def __init__(self, param: str):
        self.has_scanned = False
        self.fee_level = "NORMAL"
        self.recommendation = "WAIT"
        self.analysis = "Awaiting scan"
        self.param = param

    @gl.public.write
    def check_fees(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            fng = gl.nondet.web.render("https://alternative.me/crypto/fear-and-greed-index/", mode="text")
            print(fng)

            task = f"""You are a gas fee analyst. Based on market activity levels, estimate current Ethereum gas conditions.
            Here is current crypto market data:
            {fng[:1500]}

            Respond with the following JSON format:
            {{
                "fee_level": str,
                "recommendation": str,
                "avg_fee": str,
                "summary": str
            }}
            fee_level: one of VERY_LOW, LOW, NORMAL, HIGH, EXTREME.
            recommendation: one of TRANSACT_NOW, WAIT, URGENT_ONLY.
            avg_fee: estimated gas in gwei as string.
            summary: one sentence about gas conditions.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.fee_level = result_json["fee_level"]
        self.recommendation = result_json["recommendation"]
        self.analysis = result_json["summary"]

        return result_json
