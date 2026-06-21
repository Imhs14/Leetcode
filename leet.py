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
    },
    "13-Remove_duplicates_from_sorted_array.py": {
        "number": "26",
        "title": "Remove Duplicates from Sorted Array",
        "difficulty": "Easy",
        "category": "Two Pointers",
        "link": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
        "time": "O(N)",
        "space": "O(1)"
    },
    "14-Find_the_Index_of_the_First_Occurrence_in_a_String.py": {
        "number": "28",
        "title": "Find the Index of the First Occurrence in a String",
        "difficulty": "Easy",
        "category": "Strings",
        "link": "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/",
        "time": "O(N * M)",
        "space": "O(1)"
    },
    "15-Check_good_integer.py": {
        "number": "N/A",
        "title": "Check Good Integer",
        "difficulty": "Easy",
        "category": "Math",
        "link": "",
        "time": "O(D)",
        "space": "O(D)"
    }
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

def sync_readme(directory: str):
    import math
    problems = scan_problems(directory)
    
    comp_easy = sum(1 for p in problems if p.difficulty == 'Easy' and p.is_complete)
    comp_med = sum(1 for p in problems if p.difficulty == 'Medium' and p.is_complete)
    comp_hard = sum(1 for p in problems if p.difficulty == 'Hard' and p.is_complete)
    completed = comp_easy + comp_med + comp_hard
    
    total_easy = 951
    total_med = 2074
    total_hard = 947
    total = total_easy + total_med + total_hard

    def describe_arc(x, y, r, start_angle, end_angle):
        if end_angle <= start_angle:
            return ""
        def polar_to_cartesian(cx, cy, radius, angle_deg):
            angle_rad = (angle_deg - 90) * math.pi / 180.0
            return cx + radius * math.cos(angle_rad), cy + radius * math.sin(angle_rad)

        start = polar_to_cartesian(x, y, r, end_angle)
        end = polar_to_cartesian(x, y, r, start_angle)
        large_arc_flag = "0" if end_angle - start_angle <= 180 else "1"
        return f"M {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc_flag} 0 {end[0]:.2f} {end[1]:.2f}"

    bg_med = describe_arc(150, 100, 60, -25, 85)
    bg_hard = describe_arc(150, 100, 60, 95, 205)
    bg_easy = describe_arc(150, 100, 60, 215, 325)

    fg_med = describe_arc(150, 100, 60, -25, -25 + (comp_med / total_med * 110)) if comp_med > 0 else ""
    fg_hard = describe_arc(150, 100, 60, 95, 95 + (comp_hard / total_hard * 110)) if comp_hard > 0 else ""
    fg_easy = describe_arc(150, 100, 60, 215, 215 + (comp_easy / total_easy * 110)) if comp_easy > 0 else ""

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 600 200">
    <style>
        .bg {{ fill: #282828; }}
        .text-huge {{ fill: #ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 32px; font-weight: 600; }}
        .text-large {{ fill: #ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; }}
        .text-medium {{ fill: #ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 500; }}
        .text-small {{ fill: #8c8c8c; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 500; }}
        .text-easy {{ fill: #00b8a3; }}
        .text-medium-diff {{ fill: #ffc01e; }}
        .text-hard {{ fill: #ff375f; }}
        
        .box {{ fill: #333333; rx: 8; }}
        
        .ring-bg-easy {{ fill: none; stroke: #224341; stroke-width: 6; stroke-linecap: round; }}
        .ring-bg-med {{ fill: none; stroke: #5e4e26; stroke-width: 6; stroke-linecap: round; }}
        .ring-bg-hard {{ fill: none; stroke: #5a2c3a; stroke-width: 6; stroke-linecap: round; }}
        
        .ring-easy {{ fill: none; stroke: #00b8a3; stroke-width: 6; stroke-linecap: round; }}
        .ring-med {{ fill: none; stroke: #ffc01e; stroke-width: 6; stroke-linecap: round; }}
        .ring-hard {{ fill: none; stroke: #ff375f; stroke-width: 6; stroke-linecap: round; }}
    </style>
    
    <rect class="bg" width="600" height="200" rx="10" />
    
    <!-- Background arcs -->
    <path class="ring-bg-med" d="{bg_med}" />
    <path class="ring-bg-hard" d="{bg_hard}" />
    <path class="ring-bg-easy" d="{bg_easy}" />
    
    <!-- Foreground arcs -->
    <path class="ring-med" d="{fg_med}" />
    <path class="ring-hard" d="{fg_hard}" />
    <path class="ring-easy" d="{fg_easy}" />
    
    <!-- Center text -->
    <text x="135" y="105" class="text-huge" text-anchor="middle">{completed}</text>
    <text x="175" y="105" class="text-small" text-anchor="middle">/{total}</text>
    <text x="150" y="130" class="text-medium" text-anchor="middle"><tspan fill="#00b8a3">✓</tspan> Solved</text>
    
    <!-- Right side stats -->
    <g transform="translate(380, 25)">
        <rect class="box" x="0" y="0" width="180" height="40" />
        <text x="15" y="25" class="text-large text-easy">Easy</text>
        <text x="165" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_easy}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_easy}</tspan></text>
    </g>
    <g transform="translate(380, 80)">
        <rect class="box" x="0" y="0" width="180" height="40" />
        <text x="15" y="25" class="text-large text-medium-diff">Med.</text>
        <text x="165" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_med}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_med}</tspan></text>
    </g>
    <g transform="translate(380, 135)">
        <rect class="box" x="0" y="0" width="180" height="40" />
        <text x="15" y="25" class="text-large text-hard">Hard</text>
        <text x="165" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_hard}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_hard}</tspan></text>
    </g>
</svg>'''

    svg_path = os.path.join(directory, "leetcode_stats.svg")
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg)

    readme_path = os.path.join(directory, "README.md")
    if not os.path.exists(readme_path):
        console.print(f"[bold red]README.md not found at {readme_path}[/bold red]")
        return
        
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
        
    stats_block = '<p align="center">\\n  <img src="./leetcode_stats.svg" alt="LeetCode Stats" />\\n</p>'
    
    try:
        pattern_stats = r"(<!-- PROGRESS_STATS_START -->)(.*?)(<!-- PROGRESS_STATS_END -->)"
        readme_content = re.sub(pattern_stats, r"\\1\n" + stats_block + r"\n\3", readme_content, flags=re.DOTALL)
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
            
        console.print("[bold green]✓ README.md progress synced successfully![/bold green]")
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
        console.print("  [bold]2.[/bold] 🆕 Create New Problem Skeleton")
        console.print("  [bold]3.[/bold] 🔄 Sync Metadata to README.md")
        console.print("  [bold]4.[/bold] 🔧 Run Doctor to Standardize/Format Workspace")
        console.print("  [bold]0.[/bold] 🚪 Exit")
        
        choice = Prompt.ask("\nSelect option", choices=["0", "1", "2", "3", "4"], default="1")
        
        if choice == "0":
            console.print("\n[bold green]Goodbye! Keep solving and learning! 🧠🚀[/bold green]")
            break
        elif choice == "1":
            list_problems(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "2":
            create_problem(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "3":
            sync_readme(directory)
            Prompt.ask("\nPress Enter to return to menu")
        elif choice == "4":
            doctor_files(directory)
            Prompt.ask("\nPress Enter to return to menu")

# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="LeetCode Workspace Productivity Suite Manager.")
    parser.add_argument("command", nargs="?", choices=["list", "create", "sync", "doctor"],
                        help="Command to run directly without entering the interactive menu.")
    
    args = parser.parse_args()
    directory = os.path.dirname(os.path.abspath(__file__))

    # Run in direct command-line mode or interactive mode
    if args.command == "list":
        list_problems(directory)
    elif args.command == "create":
        create_problem(directory)
    elif args.command == "sync":
        sync_readme(directory)
    elif args.command == "doctor":
        doctor_files(directory)
    else:
        # Run interactive TUI loop
        interactive_loop(directory)

if __name__ == '__main__':
    main()
