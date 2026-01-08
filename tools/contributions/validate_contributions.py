import json
import os

submissions_path = r'C:\Users\bbbvl\OneDrive\Desktop\HIBA_llm\github_ready\user_stories.jsonl'
dataset_path = r'C:\Users\bbbvl\OneDrive\Desktop\HIBA_llm\github_ready\dataset.jsonl'

def validate():
    if not os.path.exists(submissions_path):
        print("No new submissions found.")
        return

    with open(submissions_path, 'r', encoding='utf-8') as f:
        submissions = [json.loads(line) for line in f]

    if not submissions:
        print("Submissions file is empty.")
        return

    approved = []
    print(f"Found {len(submissions)} new submissions. Press [y] to approve, [n] to skip, [q] to quit.\n")

    for i, sub in enumerate(submissions):
        print(f"--- Submission {i+1} ---")
        print(f"Name: {sub.get('contributor', 'Anonymous')}")
        print(f"Message: {sub['messages'][1]['content']}")
        
        choice = input("Approve this message? (y/n/q): ").lower()
        if choice == 'y':
            approved.append(sub)
            print("Approved.")
        elif choice == 'q':
            break
        else:
            print("Skipped.")

    if approved:
        with open(dataset_path, 'a', encoding='utf-8') as f:
            for item in approved:
                # Remove'contributor' metadata before adding to dataset
                clean_item = {"messages": item["messages"]}
                f.write(json.dumps(clean_item, ensure_ascii=False) + '\n')
        print(f"\nSuccessfully added {len(approved)} approved stories to {dataset_path}")
        
        # Clear submissions after processing
        with open(submissions_path, 'w', encoding='utf-8') as f:
            pass
        print("Submissions file cleared.")
    else:
        print("\nNo stories were added.")

if __name__ == "__main__":
    validate()
