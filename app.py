import os
import subprocess
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = {
    'Finance': [
        ('Finance API/AI_Agent_yfinance_code.py', 'Magic Formula Screener'),
        ('Finance API/f-score-yfinance.py', 'Piotroski F-Score Calculator'),
        ('Finance API/yfinance1.0.py', 'Large F-Score Evaluation'),
        ('Finance API/yfinance_combined_fs_and_mf.py', 'Combined FS & Magic Formula'),
        ('Finance API/yfinance_fixed_assets_magic_formula.py', 'Fixed Assets Magic Formula'),
        ('Finance API/yfinance_fscore_growth.py', 'Growth-Adjusted F-Score'),
        ('Finance API/yfinance_full_fscore.py', 'Full F-Score Screener'),
        ('Finance API/yfinance_full_magic_formula.py', 'Full Magic Formula Analyzer'),
        ('Finance API/yfinance_input_fscore.py', 'Interactive F-Score Calculator'),
        ('Finance API/yfinance_input_magic_formula.py', 'Interactive Magic Formula'),
        ('Finance API/yfinance_og_fscore.py', 'Legacy F-Score'),
        ('Finance API/yfinance_og_magic_formula.py', 'Legacy Magic Formula'),
    ],
    'AI': [
        ('AI/ai_num_guessr.py', 'Number Guesser'),
        ('AI/basic_ollama.py', 'Basic Ollama Chat'),
        ('AI/enhanced_ollama.py', 'Enhanced Ollama Assistant'),
        ('AI/enhanced_ollama_coding.py', 'Coding Helper with Ollama'),
        ('AI/tensorflow_stock_neural_network.py', 'Stock Neural Network with TensorFlow'),
    ],
    'Game Bots': [
        ('Game Bots/backgammon_bot_v1.py', 'Backgammon Bot v1'),
        ('Game Bots/backgammon_bot_v2.py', 'Backgammon Bot v2'),
        ('Game Bots/blackjack_bot_v1.py', 'Blackjack Advisor v1'),
        ('Game Bots/blackjack_bot_v2.py', 'Blackjack Advisor v2'),
        ('Game Bots/file_sorter_bot.py', 'File Sorter'),
        ('Game Bots/poker_bot.py', 'Poker Assistant'),
        ('Game Bots/tic_tac_toe_bot.py', 'Tic-Tac-Toe Bot'),
        ('Game Bots/wordle_bot_dynamic_points.py', 'Wordle Solver (Dynamic)'),
        ('Game Bots/wordle_bot_static_points.py', 'Wordle Solver (Static)'),
    ],
    'Other': [
        ('Other Projects/large_exponent_calc.py', 'Large Exponent Calculator'),
        ('Other Projects/loading_screen.py', 'Fake Loading Screen'),
        ('Other Projects/num_guessing_game.py', 'Number Guessing Game'),
        ('Other Projects/pwd_strength_checker.py', 'Password Strength Checker'),
        ('Other Projects/roman_numeral.py', 'Roman Numeral Converter'),
        ('Other Projects/simple_games.py', 'Simple Games Collection'),
        ('Other Projects/test.py', 'Test Script'),
        ('Other Projects/weather_checker_(fake).py', 'Fake Weather Checker'),
        ('Other Projects/weather_checker_(real).py', 'Real Weather Checker'),
    ],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/<name>')
def category(name):
    scripts = SCRIPTS.get(name, [])
    return render_template('category.html', name=name, scripts=scripts)

@app.route('/run/<path:script>', methods=['POST'])
def run_script(script):
    script_path = os.path.join(BASE_DIR, script)
    user_input = request.form.get('input', '')
    try:
        result = subprocess.run(
            ['python3', script_path],
            input=user_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=20,
        )
        output = result.stdout.decode()
    except Exception:
        output = f'Failed to run script. Example command:\npython3 {script}'
    return render_template('output.html', script=script, output=output)

if __name__ == '__main__':
    app.run(debug=True)
