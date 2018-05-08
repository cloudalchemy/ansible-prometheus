# Contributor Guideline

This document provides an overview of how you can participate in improving this project or extending it. We are grateful for all your help: bug reports and fixes, code contributions, documentation or ideas. Feel free to join, we appreciate your support!!

## Communication

### IRC

You can talk with us on #cloudalchemy channel on freenode.

### GitHub repositories

Much of the issues, goals and ideas are tracked in the respective projects in GitHub. Please use this channel to report bugs.

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

We try to stick to semantic versioning and our releases are made by CI pipeline. It is done by assigning a keyword (in a way similar to travis [`[ci skip]`](https://docs.travis-ci.com/user/customizing-the-build#Skipping-a-build)) to a commit with merge request. Available keywords are (square brackets are important!):
 
* `[patch]`, `[fix]` - for PATCH version release
* `[minor]`, `[feature]`, `[feat]` - for MINOR version release
* `[major]`, `[breaking change]` - for MAJOR version release
 
## Changelog
 
Changelog is generateg automatically on every merged Pull Request and all information is taken from github issues, PRs and labels.

## Expectations

### Keep it simple

We try to provide production ready ansible roles which should be as much zero-conf as possible but this doesn't mean to overcomplicate things. Just follow [KISS](https://en.wikipedia.org/wiki/KISS_principle).

### Be explicit

* Please avoid using nonsensical property and variable names.
* Use self-describing attribute names for user configuration.
* In case of failures, communicate what happened and why a failure occurs to the user. Make it easy to track the code or action that produced the error. Try to catch and handle errors if possible to provide improved failure messages.


### Add tests

Currently we are using two test scenarios located in [/molecule](molecule) directory. First ([default](molecule/default/molecule.yml)) one is testing default configuration without any additional variables, second one ([alternative](molecule/alternative/molecule.yml)) is testing what happens when many variables from [/defaults/main.yml](defaults/main.yml) are changed. When adding new functionalities please add tests to proper scenarios. Tests are written in testinfra framework and are located in `/tests` subdirectory of scenario directory (for example default tests are in [/molecule/default/tests](molecule/default/tests)).
More information about:
  - [testinfra](http://testinfra.readthedocs.io/en/latest/index.html)
  - [molecule](https://molecule.readthedocs.io/en/latest/index.html)

### Follow best practices

Please follow [ansible best practices](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html) and especially provide meaningful names to tasks and even comments where needed.

Our test framework automatically lints code with [`yamllint`](https://yamllint.readthedocs.io) and [`ansible-lint`](https://github.com/willthames/ansible-lint) programs so be sure to follow their rules.

Remember: Code is generally read much more often than written.

### Use Markdown

Wherever possible, please refrain from any other formats and stick to simple markdown.
