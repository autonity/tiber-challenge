# Autonity Piccadilly Tiber Challenge

GitHub repository for the Autonity Piccadilly Tiber Challenge, an open and incentivised set of tasks on the Autonity Piccadilly Testnet.

Piccadilly Testnet has been re-genesised with the v1 Autonity Protocol, the Tiber protocol upgrade. To celebrate this milestone the *Piccadilly Tiber Challenge* will now run with two categories of activity: *Use-case Testing* and *Oracle Calibration Testing*.

For how to participate see [Take part in the challenge](./README.md#take-part-in-the-challenge) in this README.

This repo contains [Starter Kit](./README.md#starter-kit) example code to take part in the *Use-case Testing* activity.

You need to set up and run a validator node on Piccadilly Testnet to take part in the *Oracle Calibration Testing* activity. Go to the [autonity](https://github.com/autonity/autonity) and [autonity-oracle](https://github.com/autonity/autonity-oracle) GitHub repos for Autonity main client and oracle server software. Refer to [docs.autonity.org](https://docs.autonity.org/node-operators/install-aut/) for how to install and run.

---

## Take part in the challenge

You can sign-up, get setup and prepare for the *Piccadilly Tiber Challenge* now! 

Scoring for Tiber Challenge will begin 18<sup>th</sup> December at 12:00 UTC. So you have plenty of time to get ready to take part. The challenge will run through into January and an end date will be announced after the New Year. To take part, just:

- [Register and set-up](./README.md#register-and-set-up) for the *Piccadilly Tiber Challenge*
- Take part in the [Tiber Tasks](./README.md#tiber-tasks) challenges
- Join the [Autonity Discord](https://discord.gg/autonity), the main social hub of the Autonity community, for discussions about the game and Autonity in general, and [follow](https://twitter.com/autonity_) the project on X (formerly Twitter&hellip;) so you don’t miss any key announcements!

---

### Register and set-up

To enter the challenge, register and setup your technology.

To register, simply complete the **registration form** at [http://tiber.autonity.org/](http://tiber.autonity.org/) ([Ts&amp;Cs](https://gateway.pinata.cloud/ipfs/Qmcdza1BscJFAr2ubkJ2WEksqG8e3gc3XAVpwR83xNY39g) for the challenge are linked from the form).

After registration, your participant’s Registered Address will be funded with:

| Asset | Amount |
| :--|:--|
| ATN on Piccadilly | `1` |
| NTN on Piccadilly | `0` |
| Test USDCx on Piccadilly | `1000` |
| Test USDC on Polygon Amoy Testnet | `25` |
| Test POL on Polygon Amoy Testnet | `0.01` |

Your Piccadilly funding lets you get going straightaway. USDCx is an ERC-20 mock USD stablecoin deployed on Piccadilly just for the Tiber Challenge and you can trade ATN and NTN in a Uniswap V2 AMM with ATN-USDCx and NTN-USDCx markets. You also get some funding on Polygon Amoy Testnet, so you can bridge some USDC over to Piccadilly, too.

To set up your technology:

- for *Use-case Testing*, install the [autonity/tiber-challenge](https://github.com/autonity/tiber-challenge) starter-kit in this GitHub.  To score, configure the starter kit to submit transactions from your registered participant address.
- for *Oracle Calibration Testing*, install the Autonity main client and oracle server, and setup a validator node (see [docs.autonity.org](https://docs.autonity.org/node-operators/install-aut/) to get going). When you register the validator on-chain use your registered participant address to submit the registration transaction. To score, aim to become a consensus committee member and submit accurate oracle price reports.

You're now ready to take part in [Tiber Tasks](./README.md#tiber-tasks).

---

### Tiber Tasks

There are two categories of activity in the *Piccadilly Tiber Challenge*: *Use-case Testing* and *Oracle Calibration Testing* activities.

Task enrolment is automatic and scoring is detected by querying chain data associated with the participant address you provided in the [registration form](https://tiber.autonity.org/).  

Task infrastructure is straightforward:

- Autonity itself - the range of Autonity Protocol functionality accessible to you through the Autonity Contract Interfaces.
- A Uniswap V2 AMM with ATN-USDCx and NTN-USDCx markets for trading.
- A USDC Bridge for bridging USDC between Polygon Amoy Testnet and Piccadilly Testnet.

#### Use-case Testing

For all challenge participants. The task goal is to test Autonity Protocol interfaces by calling as wide a range of interface functions as possible.

Configure your cloned [/autonity/tiber-challenge](https://github.com/autonity/tiber-challenge) starter-kit to use your registered participant address, and get going.

The starter-kit comes with an out-the-box baseline of pre-built transaction calls to protocol contract functions and the Uniswap V2 AMM deployed on Piccadilly for trading NTN and ATN in USDCx markets.

Earn points proportionate to the variety of interface functions you call.

Scale-up your point score by extending the starter-kit to call more Autonity Contract Interface functions ([docs.autonity.org, Autonity Interfaces](https://docs.autonity.org/reference/api/)), USDC Bridge, and AMM interface functions.

##### Points and scoring

Points are scored based on transactions submitted from your registered Participant Address to Autonity Contract Interface functions, for bridging USDC onto or from Piccadilly, and for trades to the AMM.

*Scoring is based on the range of functions called and calling those functions in a variable way*. To maximise your score:

- focus on calling Autonity Contract Interface functions to interact with the Autonity Protocol functions.
- focus on the diversity of interface functions called. Extend the starter-kit baseline to call as many different interface functions as you can. See [docs.autonity.org, Autonity Interfaces](https://docs.autonity.org/reference/api/) for the range of Autonity Protocol interfaces you can call.
- focus on the variety of your transaction pattern. Maximise the randomness of how you call interfaces, aim not to call the same function sequentially but call a variety of different interface functions as you proceed.

Award Tributes will be allocated to participants taking part in the task *pro rata* to their score.

#### Oracle calibration testing

Any participant who registers a validator node will be participating in the Oracle
Calibration activity _when that validator is in the consensus committee_.

The task is testing the accuracy of price reporting by the validator oracle network. Price reports submitted by committee validator oracles are sampled periodically and compared to an intraday FX benchmark dataset.

As a validator operator, aim to optimise the quality of your validator oracle price reporting and when a member of the consensus committee be sure to be active!

A "Midterm Report" will be published as a research paper on the *Autonity Papers* website [papers.autonity.org/](https://papers.autonity.org/) with detailed analysis of the calibration findings (systematic biases, conjectures about their causes, *etc.*) Participants can use the findings to tweak their oracle server configurations and have a more performant second half.

>[!NOTE]
>The "Midterm Report", analysis findings, and the data analysed by the report is publicly available at <https://github.com/autonity/oracle-submission-analysis>. The report can be viewed and built as a standalone quarto website as described in the repo [README](https://github.com/autonity/oracle-submission-analysis/blob/master/README.md). Publication of the report to [papers.autonity.org/](https://papers.autonity.org/) is pending.

Participants will be asked to provide details of their oracle configurations and any changes they made after the Midterm Report via a Web-based form.

A "Final Report" will be published on [papers.autonity.org](https://papers.autonity.org/) detailing the final scores of the participants, analysis of any improvement in computed ACU veracity over the second half, and practical best practice recommendations for oracle server configurations.

##### Points and scoring

Points are scored based on the accuracy of your price reports when a committee member in comparison to the benchmark.

*Scoring is based on (a) your completing the midterm feedback form, providing details of your oracle server setup; (b) the accuracy of your price reporting - the difference between the prices submitted by your validator and the prices reported in the benchmark;, and, (c) the amount of time your validator was in the consensus committee.* To score:

- complete Midterm Feedback (mandatory). Provide details of your oracle configuration when requested at the midterm point. This is required to qualify for an award.
- focus on managing the quality and accuracy of your validator oracle price reporting.
- focus on being an active member of the consensus committee.

Award Tributes will be allocated to participants taking part in the task *pro rata* to their score.

### Tiber Challenge Rewards

There is an overall Piccadilly Tiber Challenge Award Budget of *150,000 Award Tributes**, convertible to NTN on Mainnet launch.

This budget is subdivided over the two activity categories:

- **75,000 Award Tributes** allocated to participants doing Use-case Testing.
- **75,000 Award Tributes** allocated to participants doing Oracle Calibration Testing.

---

## Starter Kit

Participants can earn points by running the script as-is, but in order to get
awarded with a higher score it is recommended to modify and optimize the code.

The example code has been written in Python using [v6.19.0 of the Web3.py
framework](https://web3py.readthedocs.io/en/v6.19.0/) and [v4.0.0 of the
autonity.py library](https://github.com/autonity/autonity.py/tree/v4.0.0) of Autonity
contract bindings.

The [`starter_kit.bindings`](./starter_kit/bindings/) module contains Python
bindings for the Uniswap V2 Factory and Uniswap V2 Router contracts.

### Getting Started

Pre-requisites:

- Install Nix with the [Determinate Nix Installer](https://zero-to-nix.com/concepts/nix-installer).
- Install [devenv](https://devenv.sh/getting-started/) using `nix profile install --accept-flake-config nixpkgs#devenv`.

Run the starter kit and optional linters:

1. Clone this repository.
2. Duplicate `.env.template` as `.env` and set the required environment variables.
    - `RPC_URL`: The URL of a Piccadilly (Tiber) Testnet RPC provider, please select
      one from [Chainlist](https://chainlist.org/?testnets=true&search=piccadilly).
    - `SENDER_PRIVATE_KEY`: The private key of the account that will sign and
      send the transactions.
    - `RECIPIENT_ADDRESS`: The address of an arbitrary account that tokens may
      be sent to.
3. Run `devenv shell` to enter a devenv shell.
4. In the devenv shell, run the script with `starter-kit`.
5. In the devenv shell, you can run linters with `lint-code`.

Note: the private key can be extracted from a Geth keyfile as a hex-string with
[autonity-cli](https://github.com/autonity/autonity-cli)'s `aut account
reveal-private-key` command.
