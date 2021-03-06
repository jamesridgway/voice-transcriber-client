# Voice Transcriber
![CI](https://github.com/jamesridgway/voice-transcriber-client/workflows/CI/badge.svg?branch=master)

A python client for [voice-transcriber](https://github.com/jamesridgway/voice-transcriber).

## Installation

    pip install voice-transcriber-client

## Usage

### Setup credentials

    voice-transcriber config -d mydoma.in -a MyApiKey-l3tm31n

### Transcribe an audio file

    voice-transcriber transcribe meeting.m4a

## Development
The following instructions will help you get started in developing changes for this project.

### Python Environment
Run the following to setup a python virtual environment and install all dependencies:

    ./setup.sh

### Pylint
Pylint is used to check code quality and style, pylint can be run using:

    ./run-pylint.sh

### Tests
You can run the test as follows:

    ./run-tests.sh

An HTML code coverage report will be generated in the `htmlcov` directory.
