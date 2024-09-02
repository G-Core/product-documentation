---
title: fastedge-cli
displayName: FastEdge CLI
published: true
toc:
   --1--Install and set up FastEdge CLI: "install-and-set-up-fastedge-cli"
   --1--Run FastEdge CLI: "run-fastedge-cli"
   --1--Example commands: "example-commands"   
pageTitle: A guide on how to use FastEdge CLI for locally testing applications | Gcore
pageDescription: Explore FastEdge CLI tool and learn how to install, build, and run it locally to test FastEdge applications. Check example commands for using the CLI tool.
---
# FastEdge CLI  

Run and test your FastEdge applications locally with the Gcore <a href="https://github.com/G-Core/FastEdge-lib" target="_blank">FastEdge CLI tool</a>. The following instructions will help you install, build, and execute some basic commands with FastEdge CLI. 

<alert-element type="tip" title="Tip">

We are actively developing <a href="https://github.com/G-Core/FastEdge-lib" target="_blank">FastEdge CLI</a> and recommend regularly checking the FastEdge-lib repository for updates and new versions. 

</alert-element>

## Install and set up FastEdge CLI  

1\. Clone the <a href="https://github.com/G-Core/FastEdge-lib" target="_blank">FastEdge-lib</a> repository. 

2\. Install Rust by running the following command:  

`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh 
source "$HOME/.cargo/env"`  

3\. In the directory where you cloned the repository, run the following command to initialize and update all submodules: `git submodule update --init --recursive -f` 

4\. Build the CLI tool and all required dependencies: `cargo build –release`

5\. Compile and run the binary with the `help` flag to view the full list of available CLI commands and parameters: `cargo run --bin cli -- --help`

## Run FastEdge CLI

To run the compiled CLI tool, use the following command:

<code-block>

./target/release/cli <span style="color:#FF5913">command</span>

</code-block>

For example, if you want to open help and view the list of supported commands, run: `./target/release/cli http --help`.

## Example commands

This section provides some basic examples of how to work with FastEdge CLI. The sample commands use a test application from the <a href="https://github.com/G-Core/FastEdge-examples" target="_blank">FastEdge-examples</a> repository. 

### Run a FastEdge application and print all its headers 

Execute the following command: 

<code-block>

./target/release/cli http –w <span style="color:#FF5913">[path-to-your-application]</span> –-port <span style="color:#FF5913">[port number]</span>

</code-block>

For example:  `./target/release/cli http -w ../FastEdge-examples/rust/target/wasm32-wasi/release/print.wasm –-port 8080`

To view the list of all printed headers, run `curl http://localhost:8080`

### Run a FastEdge application with environment variables

Execute the following command: 

<code-block>

./target/release/cli http –w <span style="color:#FF5913">[path-to-your-application]</span> –-env <span style="color:#FF5913">[variables]</span> --port <span style="color:#FF5913">[port number]</span> 

</code-block>

For example, to set the BASE variable to the URL of the repository’s README:  

`./target/release/cli http -w ../FastEdge-examples/rust/target/wasm32-wasi/release/markdown.wasm env BASE=https://raw.githubusercontent.com/G-Core/FastEdge-lib/main --port 8080`

After executing the command, you can run the FastEdge application, which will output the contents of the README: `http://localhost:8080/README.md`

### Run an application with sample geo headers 

FastEdge CLI can add sample geo headers to your application without using a real IP address: 

<code-block>

./target/release/cli http -w <span style="color:#FF5913">[path-to-your-application]</span> –geo –port <span style="color:#FF5913">[port number]</span> 

</code-block>

For example:  `./target/release/cli http -w ../FastEdge-examples/rust/target/wasm32-wasi/release/print.wasm –-geo --port 8081` 

To view the list of sample geo headers, run `curl http://localhost:8081`. You should see an output similar to the following: 

```
Headers:
    host: localhost:8081
    user-agent: curl/8.6.0
    accept: */*
    pop-country-name: luxembourg
    pop-city: luxembourg
    pop-country-code: au
    server_name: test.localhost
    pop-continent: eu
    pop-lat: 49.6113
    pop-long: 6.1294
    pop-reg: lu%
```    