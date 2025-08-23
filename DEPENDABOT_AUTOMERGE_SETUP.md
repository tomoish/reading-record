# Dependabot Auto-Merge Setup

This document explains how to set up automatic merging of Dependabot PRs with co-author attribution.

## Overview

The auto-merge system will:
- Automatically merge patch and minor version updates from Dependabot
- Include you as a co-author in the merge commits
- Only merge safe updates (no major version changes)
- Preserve full git history

## Setup Instructions

1. **Move the workflow file**: 
   Move `dependabot-automerge.yml` to `.github/workflows/dependabot-automerge.yml`

2. **Enable auto-merge permissions**:
   - Go to your repository settings
   - Navigate to Actions → General
   - Under "Workflow permissions", ensure "Read and write permissions" is selected
   - Check "Allow GitHub Actions to create and approve pull requests"

3. **Configure Dependabot** (optional):
   Create `.github/dependabot.yml` if it doesn't exist:
   ```yaml
   version: 2
   updates:
     - package-ecosystem: "pip"
       directory: "/book_project"
       schedule:
         interval: "weekly"
       open-pull-requests-limit: 5
   ```

## How It Works

1. When Dependabot creates a PR, the workflow triggers
2. It checks if the update is a patch or minor version (safe updates)
3. If safe, it merges the PR with a commit message that includes you as co-author
4. Major version updates require manual review

## Security Considerations

- Only patch and minor updates are auto-merged
- Major version updates require manual review
- The workflow has limited permissions
- All changes are logged in git history

## Customization

You can modify the workflow to:
- Change which update types are auto-merged
- Adjust the co-author information
- Add additional checks or tests before merging
- Customize commit messages

## Testing

To test the setup:
1. Create a test branch with an outdated dependency
2. Let Dependabot create a PR for a patch/minor update
3. Verify the auto-merge works with co-author attribution