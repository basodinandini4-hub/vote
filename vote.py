votes = {"Alice": 0, "Bob": 0, "Charlie": 0}

print("=" * 30)
print("      🗳️  Voting System")
print("=" * 30)
print("Candidates:", ", ".join(votes.keys()))
print("Type 'exit' to finish voting.\n")

while True:
    choice = input("Enter your vote: ").title()

    if choice == "Exit":
        break
    elif choice in votes:
        votes[choice] += 1
        print("✅ Vote recorded!\n")
    else:
        print("❌ Invalid candidate! Try again.\n")

print("\n" + "=" * 30)
print("        📊 Final Results")
print("=" * 30)

for name, count in votes.items():
    print(f"{name:<10} : {count} vote(s)")

# Determine winner
winner = max(votes, key=votes.get)
print("\n🏆 Winner:", winner)
