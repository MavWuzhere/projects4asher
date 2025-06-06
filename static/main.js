window.addEventListener('DOMContentLoaded', () => {
    const resume = document.getElementById('resume');
    if (resume) {
        fetch('static/resume.txt')
            .then(res => res.text())
            .then(text => {
                resume.textContent = text;
            });
    }

    // setup Pyodide for running python snippets
    window.pyodideReady = loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.0/full/" });

    document.querySelectorAll('.run-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const output = btn.nextElementSibling;
            output.textContent = 'Running...';
            try {
                const pyodide = await window.pyodideReady;
                const code = await fetch(btn.dataset.script).then(r => r.text());
                await pyodide.loadPackagesFromImports(code);
                await pyodide.runPythonAsync(`import sys,io\nsys.stdout = io.StringIO()`);
                await pyodide.runPythonAsync(code);
                const result = pyodide.runPython('sys.stdout.getvalue()');
                output.textContent = result;
            } catch (err) {
                output.textContent = 'Pyodide failed to run this script. Showing example output.\n' + output.textContent;
            }
        });
    });
});
