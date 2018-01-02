# Contributor Guideline

This document provides an overview of how you can participate in improving this project or extending it. We are grateful for all your help: bug reports and fixes, code contributions, documentation or ideas. Feel free to join, we appreciate your support!!

## Communication

### GitHub repositories

Much of the issues, goals and ideas are tracked in the respective projects in GitHub. Please use this channel to report bugs and post ideas.

## git and GitHub

In order to contribute code please:

1. Fork the project on GitHub
2. Clone the project
3. Add changes (and tests)
4. Commit and push
5. Create a merge-request

To have your code merged, see the expectations listed below.

You can find a well-written guide [here](https://help.github.com/articles/fork-a-repo).

Please follow common commit best-practices. Be explicit, have a short summary, a well-written description and references. This is especially important for the merge-request.

Some great guidelines can be found [here](https://wiki.openstack.org/wiki/GitCommitMessages) and [here](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message).

## Releases

Generally we try to stick to semantic versioning, where every accepted PR is treated as patch or minor feature and version is released accordingly by our CI pipeline.

## Expectations

### Keep it simple

We try to provide production ready ansible roles which should be as much zero-conf as possible but this doesn't mean to overcomplicate things. Just follow [KISS](https://en.wikipedia.org/wiki/KISS_principle).

### Be explicit

* Please avoid using nonsensical property and variable names.
* Use self-describing attribute names for user configuration.
* In case of failures, communicate what happened and why a failure occurs to the user. Make it easy to track the code or action that produced the error. Try to catch and handle errors if possible to provide improved failure messages.


### Add tests

We try to have as much tests written in testinfra framework as possible, so when you copy file, some template or starting some server just add couple of lines in [/tests/test)default.py](test_default.py) file. If you want to know how to write tests in testinfra, go to their [docs](http://testinfra.readthedocs.io/en/latest/index.html).

### Follow best practices

Please follow [ansible best practices](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html) and especially provide meaningful names to tasks and even comments where needed.

Our test framework automatically lints code with [`ansible-lint`](https://github.com/willthames/ansible-lint) command so be sure to follow it's rules.

Remember: Code is generally read much more often than written.

### Use Markdown

Wherever possible, please refrain from any other formats and stick to simple markdown.
