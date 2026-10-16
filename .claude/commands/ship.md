Ship the current work in this repo:
1. Run `git status` and review the diff. Commit only files related to the task.
2. Run the type check and the production build. Stop and fix if either fails.
3. Add a CHANGELOG.md entry under [Unreleased].
4. Commit with a conventional message following CLAUDE.md, then push.
5. If this is prowesstics-web `main`, poll the Pages deploy until it finishes and report the result.
Report in two lines: what shipped, and the deploy status. $ARGUMENTS
