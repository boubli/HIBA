# Story Contributions ✍️

A pipeline for collecting, validating, and merging user-submitted stories into HIBA's Collective Memory.

## What is it?

The **Contributions** system allows users to share their own stories, messages of hope, or memories via the main HIBA demo app. These submissions are then reviewed and can be merged into the training dataset for future model updates.

## How it Works

1.  **Submission**: Users fill out a form in the "Join the Collective Memory" tab.
2.  **Saving**: The `save_contribution` function in `app.py` appends the story to `user_stories.jsonl`.
3.  **Validation**: An admin runs `validate_contributions.py` to review and approve/reject stories.
4.  **Merging**: Approved stories are appended to the main `dataset.jsonl`.

## Files

-   `hiba_space/app.py` (includes the `save_contribution` function)
-   `scripts/validate_contributions.py`: The admin review script.
-   `user_stories.jsonl`: The file where raw submissions are stored.

## Workflow

You can use the workflow command `/validate-stories` to run the validation process.

---
*Part of the HIBA Project - A Gift from God*
