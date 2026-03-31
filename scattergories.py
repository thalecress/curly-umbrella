import random
import sys

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else random.randint(1, 9999)
    random.seed(seed)

    with open('questions.txt', 'r') as f:
        questions = [q.strip() for q in f.read().split('\t') if q.strip()]

    selected = random.sample(questions, 12)

    print(f"Scattergories Game (Seed: {seed})")
    print("----------------")
    for i, q in enumerate(selected, 1):
        print(f"{i}. {q}")

if __name__ == "__main__":
    main()
