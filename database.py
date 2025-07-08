from huggingface_hub import hf_hub_download
import pandas as pd

def download_and_prepare_dataset():
    parquet_path = hf_hub_download(
        repo_id="openai/graphwalks",
        filename="graphwalks_128k_and_shorter.parquet",
        repo_type="dataset"
    )

    df = pd.read_parquet(parquet_path)
    df = df[["problem_type", "prompt", "answer_nodes"]].copy()

    # ============================ INÍCIO DO TRECHO DE TESTE ============================
    # seleciona 25 exemplos de cada tipo (bfs e parents)
    df = pd.concat([
        df[df["problem_type"] == "parents"].head(25),
        df[df["problem_type"] == "bfs"].head(25)
    ]).reset_index(drop=True)
    # ============================ FIM DO TRECHO DE TESTE ==============================

    df.insert(0, "prompt_id", range(1, len(df) + 1))
    df.to_csv("prompts.csv", index=False)

if __name__ == "__main__":
    download_and_prepare_dataset()
