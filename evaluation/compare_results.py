import pandas as pd

def compare():
    classic = pd.read_csv("classic_ai/classic_ai_answers.csv")
    llm = pd.read_csv("llm/llm_answers.csv")

    def evaluate(df, method):
        groups = []
        for problem_type, group_df in df.groupby("problem_type"):
            total = len(group_df)
            correct = group_df["is_correct"].sum()
            wrong = total - correct
            wrong_ids = group_df.loc[~group_df["is_correct"], "prompt_id"].tolist()

            groups.append({
                "method": method,
                "problem_type": problem_type,
                "accuracy": round(correct / total, 4),
                "num_correct": correct,
                "num_wrong": wrong,
                "wrong_prompt_ids": wrong_ids
            })
        return groups

    classic_eval = evaluate(classic, "classic_ai")
    llm_eval = evaluate(llm, "llm")

    all_results = classic_eval + llm_eval
    pd.DataFrame(all_results).to_csv("evaluation/comparison_report.csv", index=False)

if __name__ == "__main__":
    compare()