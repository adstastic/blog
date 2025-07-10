# Task: Extract Malformed Snipd Quotes from PRs

## Overall Goal
Find all malformed Snipd podcast quote files from open Readwise PRs, extract them into a new PR called "Malformed snipd quotes", and remove them from their original PRs. This leaves the original PRs with only ready-to-merge files.

## Background
- The blog uses a script (`fetch_and_generate_quotes.py`) to generate quote posts from Readwise
- Quote posts follow a specific template structure (see `template.md`)
- Some Snipd podcast quotes may be malformed (missing transcript content)

## Expected Quote Structure
A properly formed quote post should have:
1. **Frontmatter**: title, date, slug, tags, ref
2. **Body**: 
   - "Quoting [author](url):" line
   - For Snipd podcasts: bullet point summaries followed by transcript sections
   - For other sources: quoted text with > prefix

## Process

### 1. Create Collection Branch
```bash
git checkout main
git checkout -b malformed-snipd-quotes
```

### 2. For Each Open PR
1. Switch to PR branch: `git checkout <branch-name>`
2. List quote files: `git diff --name-only main...HEAD | grep "content/quotes/"`
3. Manually inspect each file for malformed Snipd content
4. If malformed file found:
   - Copy to malformed-snipd-quotes branch
   - Delete from current PR
   - Commit with message: "Remove malformed Snipd quote: <filename>"
   - Push changes: `git push origin <branch-name>`

### 3. Create Final PR
After processing all PRs:
```bash
git checkout malformed-snipd-quotes
git push origin malformed-snipd-quotes
gh pr create --title "Malformed snipd quotes" --body "Extracted malformed Snipd podcast quotes that need manual fixing"
```

## Identifying Malformed Snipd Quotes
Look for files that:
- Have a Snipd URL (`https://share.snipd.com/...`) in the ref field
- Are missing transcript content after bullet points
- Have incomplete or placeholder content
- Have only frontmatter with no body

## Important Notes
- Check file contents, not file size - even short quotes can be valid
- Well-formed Snipd quotes have: bullet summaries + transcript sections
- Some PRs may not contain any Snipd quotes at all
- All files must be manually inspected