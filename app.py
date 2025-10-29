from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    expression = request.form.get("expression")

   
    funny_results = ["5", "42", "100", "lol", "no idea", "try again 😂", "69", "420", "3.14159",
    "∫(x² + 3x + 1) dx",
    "√(3x + 5) + π",
    "d/dx (sin(x²))",
    "lim┬(x→∞) (3x² + 1)/(x - 7)",
    "Σ (n=1 to ∞) 1/n²",
    "(a² + b² + c²) - 2ab + 3ac - 4bc",
    "logₑ(42)",
    "sin(θ) + cos(θ) = √2 sin(θ + 45°)",
    "Matrix [[1,2],[3,4]]",
    "∂/∂x (e^(x²))",
    "∮ E · dA",
    "∫∫∫ r² sinθ dr dθ dφ",
    "|x|; x ∈ ℝ",
    "∑ (k=1 to n) k = (n(n+1))/2",
    "Γ(n) = (n-1)!",
    "√(69) ≈ 8.3066 (nice)",
    "Probability = 0.0000001 (L skill issue)"]
    result = random.choice(funny_results)

    return render_template("calculator.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
