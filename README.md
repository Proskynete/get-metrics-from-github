<div id="top" align="center">
  <h3>Get Github PR Metrics</h3>
</div>

<p align="center">
  <a href="https://nextjs.org/">
    <img alt="Nextjs" src="https://img.shields.io/badge/Made%20with-Python-blue.svg">
  </a>
  <a href="https://resume.eduardoalvarez.dev">
    <img alt="With love" src="https://img.shields.io/badge/Developed%20with-♡-red">
  </a>
  <a href="http://makeapullrequest.com">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-Welcome-lightgrey.svg">
  </a>
</p>

<br />
<br />

<details>
  <summary>Table of contents</summary>
  <ol>
    <li>
      <a href="#prepare-environment">Prepare environment</a>
      <ul>
        <li><a href="#github-token">Github Token</a></li>
        <li><a href="#environment-variable">Environment variable</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-use">How to use</a>
    </li>
  </ol>
</details>

<h2 id="prepare-environment">⚙️ Prepare environment</h2>

We need the following things:

- [Python](https://www.python.org/)
- [pytz](https://pypi.org/project/pytz/)
- Create a personal access token in your Github account
- Know the name of the organization: `Example: Proskynete`
- Know the name of the repository you want to analyze. `Example: vertical-timeline-component-react`

<h3 id="github-token">🌟 Github Token</h3>

To get Github PR metrics, you need to create a personal access token. Follow the link below to learn [how to create a personal access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)

<h3 id="environment-variable">⌛️ Environment variable</h3>

> _Recommendation: If you want to optimize your time, you can add the following environment variables in your pc, so that the script only asks you for the name of the repository_

```
export GITHUB_TOKEN=<your-token>
export GITHUB_ORGANIZATION=<the-organization-name>
```

In case you don't want to add environment variables, the script will always ask for your personal access token and organization name

## <p align="right"><a href="#top">🔝</a></p>

<h2 id="how-to-use">💪 How to use</h2>

Run the following command:

- With Python 2

```bash
python get_metrics.py
```

- With Python 3

```bash
python3 get_metrics.py
```

- Then, in the terminal you must write your `personal access token` (called `GITHUB_TOKEN`), the organization name (called `GITHUB_ORGANIZATION`), the repository name and finally the number of days with which you will obtain the metric (default will be 30 days).

```bash
❯ Enter your personal github access token:
❯ Enter the organization name or user name:
❯ Enter github repository name:
❯ Enter the number of days to extract data (if you write 0, it will default to 30):
```

_If you previously added `GITHUB_TOKEN` and `GITHUB_ORGANIZATION` as environment variables, the terminal will only prompt you for the repository name and number days._

```bash
❯ Enter github repository name:
❯ Enter the number of days to extract data (if you write 0, it will default to 30):
```

Once you finish adding the requested information, the script will start scanning for the latest PRs found between today and the last `x` days (based on what you typed) and display the result as what you see below:

```
🏁 Start the extraction of data from the VERTICAL-TIMELINE-COMPONENT-REACT project of the last 240 days
💾 Extracting from page 1...
💾 Extracting from page 2...

--- ⌛️ Total execution time: 1.3048 seconds ⌛️ ---

        Average: 68 days
        Max: 204 days
        Min: 0 days
        Count: 3 PRs
        Contributors:
                - Proskynete has 1 PRs
                - jangoergens has 1 PRs
                - stevending1st has 1 PRs

👾 See you!
```

In case there are no PRs within the date range, what you will see will be the following

```
🏁 Start the extraction of data from the ADMIN project of the last 1 days

💩 There are not enough PRs to generate the report.
👾 Bye!
```

## <p align="right"><a href="#top">🔝</a></p>
