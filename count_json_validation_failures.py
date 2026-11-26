import json
import sys

files = {
    "large": r".\logs\base_cafe_spiral_mean_both\2026-11-26_03-57-08_3b6d48be\run.jsonl",
    "small": r".\logs\base_cafe_spiral_mean_both_small\2026-11-26_16-27-46_1b136dad\run.jsonl",
}

for id, file_name in files.items():
    with open(file_name, "r") as f:
        data = [json.loads(line) for line in f if line.strip()]

    count = 0
    for line in data:
        if (
            line.get("msg") == "llm_json_validation_error"
            or line.get("reason") == "json_validation"
            or line.get("reason") == "json_unmarshal"
        ):
            count += 1

    print(f"{id}: {count}")
