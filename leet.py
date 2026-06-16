#!/usr/bin/env python3
import os
import sys
import re
import ast
import time
import inspect
import argparse
import importlib.util
from typing import List, Dict, Tuple, Any, Optional, get_type_hints

# Ensure rich is installed, otherwise provide a fallback or instruct the user
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich.align import Align
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
except ImportError:
    print("Error: The 'rich' library is required to run this script.")
    print("Please install it by running: pip install rich")
    sys.exit(1)

# Configure non-interactive backend for matplotlib if benchmarking is used
HAS_MATPLOTLIB = False
try:
    import matplotlib
    matplotlib.use('Agg')  # Headless/safe backend
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    pass

# Initialize Rich Console
console = Console()

# ==============================================================================
# DEFAULT METADATA (For bootstrapping existing files)
# ==============================================================================
DEFAULT_METADATA = {
    "1-Closest-num-to-zero.py": {
        "number": "2239",
        "title": "Find Closest Number to Zero",
        "difficulty": "Easy",
        "category": "Arrays & Hashing",
        "link": "https://leetcode.com/problems/find-closest-number-to-zero/",
        "time": "O(N)",
        "space": "O(1)"
    },
    "2-merge-string-alternately.py": {
        "number": "1768",
        "title": "Merge Strings Alternately",
        "difficulty": "Easy",
        "category": "Two Pointers",
        "link": "https://leetcode.com/problems/merge-strings-alternately/",
        "time": "O(N + M)",
        "space": "O(N + M)"
    },
    "3-Roman-to-Integer.py": {
        "number": "13",
        "title": "Roman to Integer",
        "difficulty": "Easy",
        "category": "Math",
        "link": "https://leetcode.com/problems/roman-to-integer/",
        "time": "O(N)",
        "space": "O(1)"
    },
    "4-IsSubsequence.py": {
        "number": "392",
        "title": "Is Subsequence",
        "difficulty": "Easy",
        "category": "Two Pointers",
        "link": "https://leetcode.com/problems/is-subsequence/",
        "time": "O(T)",
        "space": "O(1)"
    },
    "5-Best_time_to_buy_&_sell_Stocks.py": {
        "number": "121",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "category": "Sliding Window",
        "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
        "time": "O(N)",
        "space": "O(1)"
    },
    "5-Two_sum.py": {
        "number": "1",
        "title": "Two Sum",
        "difficulty": "Easy",
        "category": "Arrays & Hashing",
        "link": "https://leetcode.com/problems/two-sum/",
        "time": "O(N)",
        "space": "O(N)"
    },
    "6-Longest_common_prefix.py": {
        "number": "14",
        "title": "Longest Common Prefix",
        "difficulty": "Easy",
        "category": "Strings",
        "link": "https://leetcode.com/problems/longest-common-prefix/",
        "time": "O(N * M)",
        "space": "O(1)"
    },
    "7-Summary_Ranges.py": {
        "number": "228",
        "title": "Summary Ranges",
        "difficulty": "Easy",
        "category": "Arrays",
        "link": "https://leetcode.com/problems/summary-ranges/",
        "time": "O(N)",
        "space": "O(N)"
    },
    "8-Product_of_array_Except_itself.py": {
        "number": "238",
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "category": "Arrays & Hashing",
        "link": "https://leetcode.com/problems/product-of-array-except-self/",
        "time": "O(N)",
        "space": "O(1)"
    },
    "9-Merge_Intervals.py": {
        "number": "56",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "category": "Sorting",
        "link": "https://leetcode.com/problems/merge-intervals/",
        "time": "O(N log N)",
        "space": "O(N)"
    },
    "10-Sprial_matrix.py": {
        "number": "54",
        "title": "Spiral Matrix",
        "difficulty": "Medium",
        "category": "Matrices",
        "link": "https://leetcode.com/problems/spiral-matrix/",
        "time": "O(M * N)",
        "space": "O(1)"
    },
    "11-Rotate_image.py": {
        "number": "48",
        "title": "Rotate Image",
        "difficulty": "Medium",
        "category": "Matrices",
        "link": "https://leetcode.com/problems/rotate-image/",
        "time": "O(N^2)",
        "space": "O(1)",
        "in_place": True
    },
    "12-Valid_parenthesis.py": {
        "number": "20",
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "category": "Stacks",
        "link": "https://leetcode.com/problems/valid-parentheses/",
        "time": "O(N)",
        "space": "O(N)"
    }
}

# ==============================================================================
# DEFAULT TEST CASES (For automated execution)
# ==============================================================================
DEFAULT_TESTS = {
    "1-Closest-num-to-zero.py": [
        (([-4, -2, 1, 4, 8],), 1),
        (([2, -1, 1],), 1),
        (([2, 7, 8, -2],), 2)
    ],
    "2-merge-string-alternately.py": [
        (("abc", "pqr"), "apbqcr"),
        (("ab", "rs"), "arbs"),
        (("abcd", "pq"), "apbqcd")
    ],
    "3-Roman-to-Integer.py": [
        (("III",), 3),
        (("LVIII",), 58),
        (("MCMXCIV",), 1994)
    ],
    "4-IsSubsequence.py": [
        (("abc", "ahbgdc"), True),
        (("axc", "ahbgdc"), False)
    ],
    "5-Best_time_to_buy_&_sell_Stocks.py": [
        (([7, 1, 5, 3, 6, 4],), 5),
        (([7, 6, 4, 3, 1],), 0)
    ],
    "5-Two_sum.py": [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1])
    ],
    "6-Longest_common_prefix.py": [
        ((["flower", "flow", "flight"],), "fl"),
        ((["dog", "racecar", "car"],), "")
    ],
    "7-Summary_Ranges.py": [
        (([0, 1, 2, 4, 5, 7],), ["0->2", "4->5", "7"]),
        (([0, 2, 3, 4, 6, 8, 9],), ["0", "2->4", "6", "8->9"])
    ],
    "8-Product_of_array_Except_itself.py": [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0])
    ],
    "9-Merge_Intervals.py": [
        (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
        (([[1, 4], [4, 5]],), [[1, 5]])
    ],
    "10-Sprial_matrix.py": [
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    ],
    "11-Rotate_image.py": [
        (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],),
          [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
    ],
    "12-Valid_parenthesis.py": [
        (("()",), True),
        (("()[]{}",), True),
        (("(]",), False),
        (("([)]",), False),
        (("{[]}",), True)
    ]
}

# ==============================================================================
# INPUT GENERATORS FOR BENCHMARKING
# ==============================================================================
def gen_array(n: int) -> tuple:
    import random
    return ([random.randint(-1000, 1000) for _ in range(n)],)

def gen_two_strings(n: int) -> tuple:
    import random
    chars = "abcdefghijklmnopqrstuvwxyz"
    return ("".join(random.choices(chars, k=n)), "".join(random.choices(chars, k=n)))

def gen_roman(n: int) -> tuple:
    # Just scale the length of Roman numeral representation
    return ("M" * (n // 1000) + "D" * ((n % 1000) // 500) + "C" * ((n % 500) // 100) + "L" * ((n % 100) // 50) + "X" * ((n % 50) // 10) + "V" * ((n % 10) // 5) + "I" * (n % 5),)

def gen_subsequence(n: int) -> tuple:
    import random
    chars = "abcdefghijklmnopqrstuvwxyz"
    t = "".join(random.choices(chars, k=n))
    s = "".join(t[i] for i in sorted(random.sample(range(n), max(1, n // 10))))
    return (s, t)

def gen_prices(n: int) -> tuple:
    import random
    return ([random.randint(1, 1000) for _ in range(n)],)

def gen_two_sum(n: int) -> tuple:
    import random
    nums = list(range(1, n + 1))
    target = n + n - 1
    return (nums, target)

def gen_string_list(n: int) -> tuple:
    # Generates strings with a common prefix
    return (["prefix_" + str(i) + "_" + "a" * (n // 10) for i in range(10)],)

def gen_intervals(n: int) -> tuple:
    import random
    intervals = []
    for _ in range(n):
        start = random.randint(1, 2 * n)
        end = start + random.randint(1, 10)
        intervals.append([start, end])
    return (intervals,)

def gen_matrix(n: int) -> tuple:
    # Generates a matrix of size sqrt(n) x sqrt(n)
    import math
    size = max(1, int(math.sqrt(n)))
    matrix = [[i * size + j for j in range(size)] for i in range(size)]
    return (matrix,)

def gen_parentheses(n: int) -> tuple:
    # Generate balanced brackets
    return ("[" * (n // 2) + "]" * (n // 2),)

INPUT_GENERATORS = {
    "1-Closest-num-to-zero.py": gen_array,
    "2-merge-string-alternately.py": gen_two_strings,
    "3-Roman-to-Integer.py": gen_roman,
    "4-IsSubsequence.py": gen_subsequence,
    "5-Best_time_to_buy_&_sell_Stocks.py": gen_prices,
    "5-Two_sum.py": gen_two_sum,
    "6-Longest_common_prefix.py": gen_string_list,
    "7-Summary_Ranges.py": gen_array,
    "8-Product_of_array_Except_itself.py": gen_array,
    "9-Merge_Intervals.py": gen_intervals,
    "10-Sprial_matrix.py": gen_matrix,
    "11-Rotate_image.py": gen_matrix,
    "12-Valid_parenthesis.py": gen_parentheses
}

# ==============================================================================
# HELPERS: METADATA & PARSING
# ==============================================================================
class Problem:
    def __init__(self, filename: str, filepath: str):
        self.filename = filename
        self.filepath = filepath
        
        # Parse number and title from filename
        # Format can be: 1-Closest-num-to-zero.py or 10-Sprial_matrix.py
        match = re.match(r"^(\d+)-(.+)\.py$", filename)
        if match:
            self.order = int(match.group(1))
            self.raw_title = match.group(2).replace('-', ' ').replace('_', ' ')
        else:
            self.order = 999
            self.raw_title = filename.replace('.py', '')

        # Metadata properties with defaults
        self.number: str = ""
        self.title: str = self.raw_title.title()
        self.difficulty: str = "Easy"
        self.category: str = "Unknown"
        self.link: str = ""
        self.time: str = "O(N)"
        self.space: str = "O(1)"
        self.in_place: bool = False
        self.is_complete: bool = False
        
        # Load defaults
        if filename in DEFAULT_METADATA:
            d = DEFAULT_METADATA[filename]
            self.number = d.get("number", "")
            self.title = d.get("title", self.title)
            self.difficulty = d.get("difficulty", "Easy")
            self.category = d.get("category", "Unknown")
            self.link = d.get("link", "")
            self.time = d.get("time", "O(N)")
            self.space = d.get("space", "O(1)")
            self.in_place = d.get("in_place", False)

        # Parse from file content (overwrites defaults if present)
        self.parse_file()

    def parse_file(self):
        if not os.path.exists(self.filepath):
            return
            
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse AST to check if class exists and methods are complete (not empty or just "pass")
        try:
            tree = ast.parse(content)
            has_class = False
            has_non_trivial_method = False
            
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and node.name.lower() in ("solution", "solutionclass"):
                    has_class = True
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and not item.name.startswith('__'):
                            # Check body of function
                            statements = item.body
                            if len(statements) > 1:
                                has_non_trivial_method = True
                            elif len(statements) == 1:
                                stmt = statements[0]
                                # If it's a pass statement, it's trivial
                                if not isinstance(stmt, ast.Pass):
                                    has_non_trivial_method = True
                                    
            self.is_complete = has_class and has_non_trivial_method
        except SyntaxError:
            self.is_complete = False

        # Read comments for custom metadata
        lines = content.splitlines()
        for line in lines[:20]:  # Look at the first 20 lines
            line = line.strip()
            if not line.startswith('#'):
                continue
            
            # Look for tags
            m_num = re.search(r'LeetCode Problem\s*(\d+):?\s*(.*)', line, re.IGNORECASE)
            if m_num:
                self.number = m_num.group(1).strip()
                if m_num.group(2):
                    self.title = m_num.group(2).strip()
                continue
                
            m_diff = re.search(r'Difficulty:\s*(\w+)', line, re.IGNORECASE)
            if m_diff:
                self.difficulty = m_diff.group(1).strip().capitalize()
                continue
                
            m_cat = re.search(r'Category:\s*(.+)', line, re.IGNORECASE)
            if m_cat:
                self.category = m_cat.group(1).strip()
                continue
                
            m_link = re.search(r'URL:\s*(http\S+)', line, re.IGNORECASE)
            if m_link:
                self.link = m_link.group(1).strip()
                continue
                
            m_time = re.search(r'Time Complexity:\s*(.+)', line, re.IGNORECASE)
            if m_time:
                self.time = m_time.group(1).strip()
                continue
                
            m_space = re.search(r'Space Complexity:\s*(.+)', line, re.IGNORECASE)
            if m_space:
                self.space = m_space.group(1).strip()
                continue

# ==============================================================================
# AST LOAD & RUNNER ENVIRONMENT
# ==============================================================================
def load_solution_class(filepath: str, class_name: str = "Solution") -> Any:
    """Loads class definitions from the solution file using AST to avoid top-level side effects."""
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
        
    tree = ast.parse(source)
    imports_ast = []
    class_ast = None
    
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports_ast.append(node)
        elif isinstance(node, ast.ClassDef) and node.name.lower() == class_name.lower():
            class_ast = node
            
    if not class_ast:
        raise ValueError(f"Class '{class_name}' (case-insensitive) not found in {os.path.basename(filepath)}")
        
    # Compile a new module consisting only of class imports and class defs
    new_body = imports_ast + [class_ast]
    new_tree = ast.Module(body=new_body, type_ignores=[])
    
    code = compile(new_tree, filename=filepath, mode='exec')
    namespace = {}
    
    # Inject standard LeetCode typing variables and nodes
    from typing import List, Dict, Tuple, Optional, Set, Union
    namespace.update({
        'List': List, 'Dict': Dict, 'Tuple': Tuple, 'Optional': Optional, 'Set': Set, 'Union': Union,
        'list': list, 'dict': dict, 'tuple': tuple
    })
    
    exec(code, namespace)
    return namespace[class_ast.name]

# ==============================================================================
# ACTIONS
# ==============================================================================

def scan_problems(directory: str) -> List[Problem]:
    problems = []
    for f in os.listdir(directory):
        if f.endswith('.py') and f != 'test.py' and not f.startswith('leet'):
            problems.append(Problem(f, os.path.join(directory, f)))
    # Sort by order prefix
    problems.sort(key=lambda p: p.order)
    return problems

def show_dashboard(directory: str):
    problems = scan_problems(directory)
    total = len(problems)
    completed = sum(1 for p in problems if p.is_complete)
    
    easy = sum(1 for p in problems if p.difficulty == 'Easy')
    medium = sum(1 for p in problems if p.difficulty == 'Medium')
    hard = sum(1 for p in problems if p.difficulty == 'Hard')
    
    comp_easy = sum(1 for p in problems if p.difficulty == 'Easy' and p.is_complete)
    comp_medium = sum(1 for p in problems if p.difficulty == 'Medium' and p.is_complete)
    comp_hard = sum(1 for p in problems if p.difficulty == 'Hard' and p.is_complete)

    # ASCII Header
    banner = """
[bold cyan]  __                     _      ____             _ [/bold cyan]
[bold cyan] / /   ___  ___  ___  __| | ___/ ___|___   __| | ___ [/bold cyan]
[bold cyan]/ /   / _ \\/ _ \\/ __|/ _` |/ _ \\ |   / _ \\ / _` |/ _ \\[/bold cyan]
[bold cyan]\\ \\__/  __/  __/\\__ \\ (_| |  __/ |__| (_) | (_| |  __/[/bold cyan]
[bold cyan] \\____/\\___|\\___||___/\\__,_|\\___|\\____\\___/ \\__,_|\\___|[/bold cyan]
                      [bold yellow]LeetCode Workspace Manager v1.0[/bold yellow]
"""
    console.print(Align.center(banner))

    # Stats panels
    stats_table = Table.grid(padding=1, expand=True)
    stats_table.add_column(justify="center", ratio=1)
    stats_table.add_column(justify="center", ratio=1)
    stats_table.add_column(justify="center", ratio=1)
    
    def bar(val, total_val, color="green"):
        if total_val == 0: return "[grey53]0%[/grey53]"
        pct = int(val / total_val * 10)
        return f"[{color}]" + "█" * pct + "░" * (10 - pct) + f" {val}/{total_val}[/{color}]"

    stats_table.add_row(
        Panel(f"[bold cyan]Total Solved[/bold cyan]\n\n[bold white]{completed}/{total}[/bold white]\n{bar(completed, total, 'cyan')}", border_style="cyan"),
        Panel(f"[bold green]Easy Problems[/bold green]\n\n[bold white]{comp_easy}/{easy}[/bold white]\n{bar(comp_easy, easy, 'green')}", border_style="green"),
        Panel(f"[bold yellow]Medium & Hard[/bold yellow]\n\n[bold white]{comp_medium + comp_hard}/{medium + hard}[/bold white]\n{bar(comp_medium + comp_hard, medium + hard, 'yellow')}", border_style="yellow")
    )
    
    console.print(stats_table)

def list_problems(directory: str):
    problems = scan_problems(directory)
    
    table = Table(title="Solved & Skeletons LeetCode Problems", border_style="dim")
    table.add_column("Order", justify="right", style="cyan", no_wrap=True)
    table.add_column("LC #", justify="right", style="magenta")
    table.add_column("Problem Title", style="bold white")
    table.add_column("Difficulty", justify="center")
    table.add_column("Category", style="blue")
    table.add_column("Time/Space", style="dim white")
    table.add_column("Status", justify="center")

    for p in problems:
        # Difficulty color code
        diff_str = p.difficulty
        if diff_str == "Easy":
            diff_styled = f"[bold green]{diff_str}[/bold green]"
        elif diff_str == "Medium":
            diff_styled = f"[bold yellow]{diff_str}[/bold yellow]"
        else:
            diff_styled = f"[bold red]{diff_str}[/bold red]"
            
        status = "[bold green]Complete[/bold green]" if p.is_complete else "[bold yellow]Skeleton (Empty)[/bold yellow]"
        lc_num = p.number if p.number else "N/A"
        
        table.add_row(
            str(p.order),
            lc_num,
            p.title,
            diff_styled,
            p.category,
            f"{p.time} / {p.space}",
            status
        )
        
    console.print(table)

def create_problem(directory: str, title: Optional[str] = None):
    console.print(Panel("[bold green]Create New Problem Skeleton[/bold green]\nFill in details to generate a clean, scaffolded solution file. (We will NOT write solution logic for you!)"))
    
    # Prompt interactively if not provided
    if not title:
        title = Prompt.ask("Problem Name (e.g. 'Longest Substring Without Repeating Characters')")
    
    order_num = Prompt.ask("Sequence Number for file prefix (e.g. '13')", default="13")
    lc_num = Prompt.ask("LeetCode Problem Number (e.g. '3')", default="0")
    difficulty = Prompt.ask("Difficulty", choices=["Easy", "Medium", "Hard"], default="Easy")
    category = Prompt.ask("Category (e.g. 'Two Pointers', 'Sliding Window', 'Arrays')", default="Arrays")
    time_comp = Prompt.ask("Estimated Time Complexity", default="O(N)")
    space_comp = Prompt.ask("Estimated Space Complexity", default="O(1)")
    link = Prompt.ask("LeetCode URL (Optional)", default="")
    
    # Method scaffolding
    method_name = Prompt.ask("Method signature name (e.g. 'longestSubstring')", default="solve")
    method_args = Prompt.ask("Arguments (comma-separated with types, e.g. 's: str, k: int')", default="nums: List[int]")
    return_type = Prompt.ask("Return type (e.g. 'int', 'List[int]', 'bool')", default="int")

    # Format filenames and variables
    safe_title_snake = title.lower().replace(' ', '_').replace('-', '_')
    filename = f"{order_num}-{safe_title_snake.capitalize()}.py"
    filepath = os.path.join(directory, filename)
    
    if os.path.exists(filepath):
        if not Confirm.ask(f"[bold red]File {filename} already exists![/bold red] Overwrite?"):
            console.print("[yellow]Cancelled.[/yellow]")
            return

    # Scaffold content
    scaffold = f"""# LeetCode Problem {lc_num}: {title.title()}
# URL: {link}
# Difficulty: {difficulty}
# Category: {category}
# Time Complexity: {time_comp}
# Space Complexity: {space_comp}

from typing import List, Dict, Tuple, Optional

class Solution:
    def {method_name}(self, {method_args}) -> {return_type}:
        # TODO: Implement your solution here
        pass

# --- Predefined Test Cases ---
# Add test cases in format: (inputs_tuple, expected_output)
tests = [
    # (([args],), expected),
]

if __name__ == '__main__':
    # You can add custom running tests here if you run this file directly
    print("Run `python3 leet.py test {filename}` to run validation tests.")
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(scaffold)
        
    console.print(f"[bold green]Created problem scaffold: [link=file://{filepath}]{filename}[/link][/bold green]")

def run_tests(directory: str, target_filename: Optional[str] = None):
    problems = scan_problems(directory)
    
    if not target_filename:
        # Prompt for problem
        choices = [p.filename for p in problems]
        if not choices:
            console.print("[yellow]No problems found in directory.[/yellow]")
            return
        target_filename = Prompt.ask("Select problem to test", choices=choices)
        
    prob = next((p for p in problems if p.filename == target_filename), None)
    if not prob:
        console.print(f"[bold red]Problem file {target_filename} not found.[/bold red]")
        return
        
    console.print(Panel(f"[bold cyan]Running Tests for LeetCode {prob.number or 'N/A'}: {prob.title}[/bold cyan]\nFile: {prob.filename}"))
    
    try:
        # Load class dynamically
        solution_cls = load_solution_class(prob.filepath)
    except Exception as e:
        console.print(f"[bold red]Failed to load solution class: {e}[/bold red]")
        return
        
    # Get methods
    instance = solution_cls()
    methods = [m for m in dir(solution_cls) if not m.startswith('__') and callable(getattr(solution_cls, m))]
    
    if not methods:
        console.print("[bold red]No solution method found in Class.[/bold red]")
        return
        
    method_name = methods[0]  # Take first method
    method = getattr(instance, method_name)
    
    # Locate test cases: Check file definitions or default database
    test_cases = []
    
    # Let's inspect module variables for a 'tests' object using AST parsing to prevent running top-level input() calls
    try:
        with open(prob.filepath, 'r') as f:
            code_text = f.read()
        tree = ast.parse(code_text)
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'tests':
                        # Compile and execute only this assignment node
                        stmt = ast.Module(body=[node], type_ignores=[])
                        code = compile(stmt, filename='<ast>', mode='exec')
                        local_ns = {}
                        exec(code, {}, local_ns)
                        if 'tests' in local_ns and isinstance(local_ns['tests'], list):
                            test_cases = local_ns['tests']
                            console.print("[green]✓ Loaded custom test cases defined in file.[/green]")
                            break
    except Exception:
        pass
        
    # Fallback: Read comments to parse I/O test cases
    if not test_cases:
        try:
            with open(prob.filepath, 'r') as f:
                content = f.read()
            # Look for block comments containing tests
            # Matches: I/P-O/P : \n input_val \n output_val
            match = re.search(r'(I/P-O/P|i/p & o/p|input & output)\s*:\s*\n\s*(.+?)\n\s*(.+?)\n', content, re.IGNORECASE)
            if match:
                inp_str = match.group(2).strip()
                out_str = match.group(3).strip()
                
                # Format arguments depending on signature
                sig = inspect.signature(method)
                params_count = len(sig.parameters)
                
                # Split inputs by space or parse as python literals
                try:
                    # Try safety parse
                    parsed_inp = ast.literal_eval(inp_str)
                    parsed_out = ast.literal_eval(out_str)
                except Exception:
                    # Treat as simple space-separated strings
                    parts = inp_str.split()
                    if params_count == 1:
                        parsed_inp = (inp_str,)
                    else:
                        parsed_inp = tuple(parts[:params_count])
                    parsed_out = out_str
                
                # Wrap parsed input in a tuple if it isn't one
                if not isinstance(parsed_inp, tuple):
                    parsed_inp = (parsed_inp,)
                
                test_cases = [(parsed_inp, parsed_out)]
                console.print("[green]✓ Extracted fallback test case from comments.[/green]")
        except Exception:
            pass

    # Fallback to default pre-coded tests
    if not test_cases and prob.filename in DEFAULT_TESTS:
        test_cases = DEFAULT_TESTS[prob.filename]
        console.print("[cyan]ℹ Loaded standard built-in test cases for this problem.[/cyan]")
        
    if not test_cases:
        console.print("[yellow]⚠ No test cases found in file, comments, or built-in registry.[/yellow]")
        # Prompt user for manual inputs
        sig = inspect.signature(method)
        params = sig.parameters
        manual_inputs = []
        
        console.print("\n[bold]Enter test values manually:[/bold]")
        for name, param in params.items():
            val_str = Prompt.ask(f"Argument '{name}'")
            try:
                # Safely parse list, dict, integer etc.
                val = ast.literal_eval(val_str)
            except Exception:
                # Keep as string
                val = val_str
            manual_inputs.append(val)
            
        test_cases = [(tuple(manual_inputs), None)]

    # Run tests
    console.print("\n[bold cyan]Executing test suite...[/bold cyan]\n")
    all_passed = True
    
    for idx, (inputs, expected) in enumerate(test_cases, 1):
        # We need to copy inputs if they are lists/dicts to check in-place changes later
        import copy
        inputs_copy = copy.deepcopy(inputs)
        
        start_time = time.perf_counter()
        try:
            # Execute method
            res = method(*inputs_copy)
            elapsed = (time.perf_counter() - start_time) * 1000 # milliseconds
            
            # Check in-place modification
            is_inplace = getattr(prob, 'in_place', False) or (res is None and expected is not None)
            actual_res = inputs_copy[0] if is_inplace else res
            
            # Comparison check
            if expected is None:
                console.print(f"[bold cyan]Manual Test {idx}:[/bold cyan] Input: {inputs} | Output: [bold green]{actual_res}[/bold green] (Executed in {elapsed:.3f}ms)")
            else:
                passed = actual_res == expected
                status_str = "[bold green]PASS[/bold green]" if passed else "[bold red]FAIL[/bold red]"
                if not passed:
                    all_passed = False
                    
                console.print(f"[bold]Test {idx}:[/bold] {status_str}")
                console.print(f"  Inputs:   {inputs}")
                console.print(f"  Expected: {expected}")
                console.print(f"  Actual:   {actual_res}")
                console.print(f"  Time:     {elapsed:.3f} ms\n")
        except Exception as e:
            elapsed = (time.perf_counter() - start_time) * 1000
            console.print(f"[bold]Test {idx}:[/bold] [bold red]CRASH[/bold red]")
            console.print(f"  Inputs:   {inputs}")
            console.print(f"  Error:    {e}")
            console.print(f"  Time:     {elapsed:.3f} ms\n")
            all_passed = False
            
    if all_passed and expected is not None:
        console.print("[bold green]🎉 All tests passed successfully![/bold green]")
    elif not all_passed:
        console.print("[bold red]❌ Some tests failed or crashed. Check details above.[/bold red]")

def benchmark_solution(directory: str, target_filename: Optional[str] = None):
    if not HAS_MATPLOTLIB:
        console.print("[bold red]Error: Matplotlib is not available. Install it with: pip install matplotlib numpy[/bold red]")
        return
        
    problems = scan_problems(directory)
    if not target_filename:
        choices = [p.filename for p in problems]
        if not choices:
            console.print("[yellow]No problems found.[/yellow]")
            return
        target_filename = Prompt.ask("Select problem to benchmark", choices=choices)
        
    prob = next((p for p in problems if p.filename == target_filename), None)
    if not prob:
        console.print(f"[bold red]Problem file {target_filename} not found.[/bold red]")
        return
        
    # Check if we have an input generator for this problem
    if prob.filename not in INPUT_GENERATORS:
        console.print(f"[yellow]No input generator defined for {prob.filename} to scale. We cannot benchmark it dynamically.[/yellow]")
        return
        
    generator = INPUT_GENERATORS[prob.filename]
    
    console.print(Panel(f"[bold cyan]Benchmarking Complexity for {prob.title}[/bold cyan]\nAnalyzing execution time as input size scales..."))
    
    try:
        solution_cls = load_solution_class(prob.filepath)
    except Exception as e:
        console.print(f"[bold red]Failed to load class: {e}[/bold red]")
        return
        
    instance = solution_cls()
    methods = [m for m in dir(solution_cls) if not m.startswith('__') and callable(getattr(solution_cls, m))]
    method = getattr(instance, methods[0])
    
    # Input sizes to test
    sizes = [10, 50, 100, 500, 1000, 3000, 5000, 8000]
    runtimes = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Running benchmarks...", total=len(sizes))
        
        for size in sizes:
            # Generate inputs of this size
            inputs = generator(size)
            
            # Warm up
            try:
                method(*inputs)
            except Exception:
                pass
                
            # Measure multiple runs
            runs = 5
            total_time = 0.0
            
            for _ in range(runs):
                import copy
                inputs_run = copy.deepcopy(inputs)
                
                start = time.perf_counter()
                try:
                    method(*inputs_run)
                except Exception as e:
                    console.print(f"\n[red]Benchmark crashed on size {size}: {e}[/red]")
                    return
                end = time.perf_counter()
                total_time += (end - start)
                
            avg_time = (total_time / runs) * 1000  # milliseconds
            runtimes.append(avg_time)
            progress.advance(task)
            
    # Output Table
    table = Table(title="Complexity Scaling Results")
    table.add_column("Input Size (N)", justify="right", style="cyan")
    table.add_column("Avg Time (ms)", justify="right", style="green")
    
    for size, t in zip(sizes, runtimes):
        table.add_row(f"{size:,}", f"{t:.4f}")
    console.print(table)
    
    # Plot Complexity Curve
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, runtimes, marker='o', color='#FFA116', linewidth=2, label='Solution Time')
    plt.title(f'Complexity Benchmark: {prob.title}', fontsize=12, fontweight='bold')
    plt.xlabel('Input Size (N)', fontsize=10)
    plt.ylabel('Execution Time (ms)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Add a theoretical complexity reference curve for visual comparison
    # Normalizing theoretical curves to match the last value
    last_t = runtimes[-1]
    last_size = sizes[-1]
    
    # O(N) linear line
    ref_o_n = [last_t * (s / last_size) for s in sizes]
    plt.plot(sizes, ref_o_n, linestyle=':', color='green', alpha=0.5, label='Theoretical O(N)')
    
    # O(N log N)
    import math
    ref_o_nlog = [last_t * ((s * math.log(max(2, s))) / (last_size * math.log(last_size))) for s in sizes]
    plt.plot(sizes, ref_o_nlog, linestyle='--', color='blue', alpha=0.5, label='Theoretical O(N log N)')
    
    plt.legend()
    
    # Save the plot
    plot_filename = f"benchmark_{prob.filename.replace('.py', '')}.png"
    plot_filepath = os.path.join(directory, plot_filename)
    plt.savefig(plot_filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    console.print(f"[bold green]✓ Complexity graph plotted and saved as [link=file://{plot_filepath}]{plot_filename}[/link]![/bold green]\n")

def sync_readme(directory: str):
    problems = scan_problems(directory)
    total = len(problems)
    completed = sum(1 for p in problems if p.is_complete)
    
    easy = sum(1 for p in problems if p.difficulty == 'Easy')
    medium = sum(1 for p in problems if p.difficulty == 'Medium')
    hard = sum(1 for p in problems if p.difficulty == 'Hard')
    
    comp_easy = sum(1 for p in problems if p.difficulty == 'Easy' and p.is_complete)
    comp_medium = sum(1 for p in problems if p.difficulty == 'Medium' and p.is_complete)
    comp_hard = sum(1 for p in problems if p.difficulty == 'Hard' and p.is_complete)
    
    # Generate Stats Block
    def get_progress_bar(val, total_val):
        if total_val == 0: return ""
        pct = (val / total_val) * 100
        filled = int(pct / 5)
        return f"`[{'█' * filled}{'░' * (20 - filled)}]` {pct:.1f}% ({val}/{total_val})"

    stats_block = f"""
| Category | Progress | Count |
| :--- | :--- | :---: |
| **Total Solved** | {get_progress_bar(completed, total)} | **{completed}/{total}** |
| **Easy** | {get_progress_bar(comp_easy, easy)} | **{comp_easy}/{easy}** |
| **Medium** | {get_progress_bar(comp_medium, medium)} | **{comp_medium}/{medium}** |
| **Hard** | {get_progress_bar(comp_hard, hard)} | **{comp_hard}/{hard}** |
"""

    # Generate Problems Table Block
    table_block = """
| # | Problem Number | Title | Difficulty | Category | Time | Space | Status | Solution Link |
| :-: | :-: | :--- | :-: | :--- | :-: | :-: | :-: | :-: |
"""
    for p in problems:
        status_badge = "✅ Complete" if p.is_complete else "🚧 Skeleton"
        diff_badge = f"🟢 Easy" if p.difficulty == "Easy" else (f"🟡 Medium" if p.difficulty == "Medium" else "🔴 Hard")
        
        # LeetCode link
        title_linked = f"[{p.title}]({p.link})" if p.link else p.title
        solution_link = f"[Solution](./{p.filename})"
        
        table_block += f"| {p.order} | {p.number or 'N/A'} | {title_linked} | {diff_badge} | {p.category} | `{p.time}` | `{p.space}` | {status_badge} | {solution_link} |\n"

    # Read and update README.md
    readme_path = os.path.join(directory, "README.md")
    if not os.path.exists(readme_path):
        console.print(f"[bold red]README.md not found at {readme_path}[/bold red]")
        return
        
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
        
    # Replace content between placeholders
    try:
        # Progress Stats
        pattern_stats = r"(<!-- PROGRESS_STATS_START -->)(.*?)(<!-- PROGRESS_STATS_END -->)"
        readme_content = re.sub(pattern_stats, f"\\1\n{stats_block}\n\\3", readme_content, flags=re.DOTALL)
        
        # Problems Table
        pattern_table = r"(<!-- PROBLEMS_TABLE_START -->)(.*?)(<!-- PROBLEMS_TABLE_END -->)"
        readme_content = re.sub(pattern_table, f"\\1\n{table_block}\n\\3", readme_content, flags=re.DOTALL)
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        console.print("[bold green]✓ README.md progress dashboard & problem index synced successfully![/bold green]")
    except Exception as e:
        console.print(f"[bold red]Failed to sync README.md: {e}[/bold red]")

def doctor_files(directory: str):
    problems = scan_problems(directory)
    console.print("[bold cyan]Running lint and standardization doctor on files...[/bold cyan]")
    
    count_fixed = 0
    
    for p in problems:
        with open(p.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Add headers if missing
        header_missing = True
        for line in content.splitlines()[:5]:
            if "LeetCode Problem" in line or "Difficulty:" in line:
                header_missing = False
                break
                
        if header_missing:
            header = f"""# LeetCode Problem {p.number or "N/A"}: {p.title}
# URL: {p.link}
# Difficulty: {p.difficulty}
# Category: {p.category}
# Time Complexity: {p.time}
# Space Complexity: {p.space}

"""
            content = header + content
            
        # 2. Add from typing imports if missing but type hints (List, Dict etc) are used
        typing_imports = []
        if 'List[' in content and 'List' not in content:
            typing_imports.append('List')
        if 'Dict[' in content and 'Dict' not in content:
            typing_imports.append('Dict')
        if 'Tuple[' in content and 'Tuple' not in content:
            typing_imports.append('Tuple')
        if 'Optional[' in content and 'Optional' not in content:
            typing_imports.append('Optional')
            
        if typing_imports:
            import_line = f"from typing import {', '.join(typing_imports)}\n"
            # Insert after the header comments
            lines = content.splitlines()
            insert_idx = 0
            for idx, line in enumerate(lines):
                if not line.startswith('#'):
                    insert_idx = idx
                    break
            lines.insert(insert_idx, import_line)
            content = '\n'.join(lines) + '\n'

        # 3. Standardize class name casing: "class solution" -> "class Solution"
        content = re.sub(r'\bclass solution\b', 'class Solution', content)
        
        # 4. Standardize method type hints if needed (best effort)
        # (Skip to avoid breaking logic)
        
        # Save changes if any made
        if content != original_content:
            with open(p.filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            console.print(f"  [green]✓ Cleaned & standardized {p.filename}[/green]")
            count_fixed += 1
            
    console.print(f"[bold green]✓ Doctor process complete! Standardized {count_fixed} files.[/bold green]\n")

# ==============================================================================
# INTERACTIVE TUI LOOP
# ==============================================================================
def interactive_loop(directory: str):
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        show_dashboard(directory)
        
        console.print("\n[bold cyan]Main Operations Menu:[/bold cyan]")
        console.print("  [bold]1.[/bold] 📋 List Problems Index")
        console.print("  [bold]2.[/bold] 🧪 Run Tests on a Solution")
        console.print("  [bold]3.[/bold] 🆕 Create New Problem Skeleton")
        console.print("  [bold]4.[/bold] 📈 Benchmark Execution & Plot Complexity")
        console.print("  [bold]5.[/bold] 🔄 Sync Metadata to README.md")
        console.print("  [bold]6.[/bold] 🔧 Run Doctor to Standardize/Format Workspace")
        console.print("  [bold]0.[/bold] 🚪 Exit")
        
        choice = Prompt.ask("\nSelect option", choices=["0", "1", "2", "3", "4", "5", "6"], default="1")
        
        if choice == "0":
            console.print("\n[bold green]Goodbye! Keep solving and learning! 🧠🚀[/bold green]")
            break
        elif choice == "1":
            list_problems(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "2":
            run_tests(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "3":
            create_problem(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "4":
            if not HAS_MATPLOTLIB:
                console.print("[bold red]Matplotlib is required for plotting complexity curves.[/bold red]")
            else:
                benchmark_solution(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "5":
            sync_readme(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "6":
            doctor_files(directory)
            Prompt.ask("\nPress Enter to return to menu")

# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="LeetCode Workspace Productivity Suite Manager.")
    parser.add_argument("command", nargs="?", choices=["list", "create", "test", "benchmark", "sync", "doctor"],
                        help="Command to run directly without entering the interactive menu.")
    parser.add_argument("--file", "-f", help="Target filename for 'test' or 'benchmark' commands.")
    
    args = parser.parse_args()
    directory = os.path.dirname(os.path.abspath(__file__))

    # Run in direct command-line mode or interactive mode
    if args.command == "list":
        list_problems(directory)
    elif args.command == "create":
        create_problem(directory)
    elif args.command == "test":
        run_tests(directory, args.file)
    elif args.command == "benchmark":
        benchmark_solution(directory, args.file)
    elif args.command == "sync":
        sync_readme(directory)
    elif args.command == "doctor":
        doctor_files(directory)
    else:
        # Run interactive TUI loop
        interactive_loop(directory)

if __name__ == '__main__':
    main()
