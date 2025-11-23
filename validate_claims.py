import pandas as pd

ground_truth = {
    "Player A": {"g": 55, "A": 52, "to": 22},
    "Player B": {"g": 38, "A": 56, "to": 30},
    "Player C": {"g": 30, "A": 21, "to": 17},
}

def check_claim(response):
    # Example rule: Does response claim Player A is top goal scorer correctly?
    if "Player A" in response and ("most goals" in response or "top scorer" in response):
        return True
    return False

def main():
    df = pd.read_csv("results/raw_responses.csv")
    df['claim_supported'] = df['response'].apply(check_claim)
    fabrication_rate = 1 - df['claim_supported'].mean()
    os.makedirs("analysis", exist_ok=True)
    df.to_csv("analysis/claims_validated.csv", index=False)
    print(f"Fabrication rate calculated: {fabrication_rate:.2f}")

if __name__ == "__main__":
    main()

#filepath modified for security