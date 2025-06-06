# Asher Lieberman Portfolio

This repository collects a wide range of Python projects covering data analysis, machine learning, automation and game development. The code demonstrates how I use libraries such as **pandas**, **yfinance**, **TensorFlow**, **Ollama** and **Flask** to build practical tools and experiments.

## Skills Demonstrated
- Python scripting and general automation
- Financial analysis with the `yfinance` API
- Machine learning with TensorFlow
- Local AI assistants powered by the Ollama model
- Game AI and simple GUI utilities
- Web interfaces served with Flask

## Projects Overview

### AI
Experiments with artificial intelligence and helper bots.
- **WIP_tensorflow_backgammon** – reinforcement learning backgammon agent using TensorFlow.
- **ai_num_guessr.py** – interactive number guesser that talks through Ollama.
- **basic_ollama.py** – minimal chat interface to a local Llama model.
- **enhanced_ollama.py** – task-based assistant for summarizing or brainstorming.
- **enhanced_ollama_coding.py** – coding helper that can debug or convert snippets.
- **tensorflow_stock_neural_network.py** – example network predicting stock moves.

### Finance API
Tools that analyse market data using `yfinance` and `pandas`.
- **AI_Agent_yfinance_code.py** – Magic Formula screener for S&P 500 companies.
- **f-score-yfinance.py** – Piotroski F-Score calculator for custom tickers.
- **yfinance1.0.py** – large batch F-Score evaluation over many symbols.
- **yfinance_combined_fs_and_mf.py** – combines EBIT/EV and ROIC rankings.
- **yfinance_fixed_assets_magic_formula.py** – Magic Formula variant using fixed assets.
- **yfinance_fscore_growth.py** – growth-adjusted F-Score calculations.
- **yfinance_full_fscore.py** – full implementation for hundreds of companies.
- **yfinance_full_magic_formula.py** – comprehensive Magic Formula ranking tool.
- **yfinance_input_fscore.py** – interactive command-line F-Score tool.
- **yfinance_input_magic_formula.py** – interactive Magic Formula analyzer.
- **yfinance_og_fscore.py** and **yfinance_og_magic_formula.py** – legacy versions of the above utilities.

### Game Bots
Scripts that provide simple AIs or utilities for popular games.
- **backgammon_bot_v1.py** and **backgammon_bot_v2.py** – heuristic move generators with doubling cube logic.
- **blackjack_bot_v1.py** and **blackjack_bot_v2.py** – Blackjack advisors with probability tables.
- **file_sorter_bot.py** – organizes Python files into folders by keyword.
- **poker_bot.py** – poker assistant that scores hands and suggests strategy.
- **tic_tac_toe_bot.py** – unbeatable Tic‑Tac‑Toe bot.
- **wordle_bot_dynamic_points.py** and **wordle_bot_static_points.py** – Wordle solvers using different letter weighting methods.

### Misc
Utilities and data files used by the other projects.
- **current_market_data.py** and **prev_years_market_data.py** – gather S&P 500 metrics for model training.
- **s&p_500_tickers_real.txt** – ticker list for finance scripts.
- **wordle_words.txt** – official Wordle answer list.

### Other Projects
Smaller experiments and learning exercises.
- **large_exponent_calc.py** – converts large powers into scientific notation.
- **loading_screen.py** – fake loading screen for a simple game.
- **num_guessing_game.py** – basic guessing game with multiple attempts.
- **pwd_strength_checker.py** – evaluates password strength.
- **roman_numeral.py** – converts between integers and Roman numerals.
- **simple_games.py** – a collection of casual games like Rock‑Paper‑Scissors.
- **test.py** – small placeholder script.
- **weather_checker_(fake).py** – mock weather app that cracks jokes.
- **weather_checker_(real).py** – asynchronous example using the `python_weather` API.

### Web Interface
A small Flask application serves these projects through a simple website. It embeds my resume on the home page and lets visitors run many of the scripts directly in the browser. If a script cannot run due to missing dependencies, the site shows an example command to execute locally.

### Using Your Own Resume
Replace `static/resume.pdf` with your personal PDF to display it on the home page. The file name should remain `resume.pdf` so the iframe reference in `templates/index.html` continues to work.

### Deploying the Site
Host the Flask app on any platform that supports Python, such as Replit or Render. After cloning the repository, install Flask with `pip install flask` and launch the site using `python app.py`. The service's public URL can then be shared with others.

---
Repository: <https://github.com/asherwuzhere/projects/>

---
Feel free to explore each folder and try out the utilities. They showcase my experimentation across finance, AI, games and general Python tooling.
