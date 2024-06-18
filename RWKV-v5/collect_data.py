from datasets import load_dataset
import json
import os.path

#dataset_lamini = load_dataset("MBZUAI/LaMini-instruction")
#
#print(dataset_lamini["train"]["features"])

datasets = {
        "wiki": "olm/wikipedia",
        }


def load_data(k, v):
    #cache_dir = "/p/alpha/hf_cache"
    if k == "wiki":
        return load_dataset(v, language="en", date="20240601")
    else:
        return load_dataset(v)


def main():
    for k, v in datasets.items():
        d = load_data(k, v)

        texts = []
        #for row in ds_databricks["train"]:
        #    text = f"""
        #    instruction: {row["instruction"]}
        #    context: {row["context"]}
        #    response: {row["response"]}
        #    """
        for row in d["train"]:
            print(row)
            texts.append({"text": text})
        
    # write concat jsonl
    with open(f"data/data.jsonl", "w") as f:
        for row in texts:
            f.write(json.dumps(row) + "\n")

if __name__ == "__main__":
    main()
