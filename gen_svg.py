import math

def generate_svg(comp_easy, comp_med, comp_hard, total_easy=951, total_med=2074, total_hard=947):
    total = total_easy + total_med + total_hard
    completed = comp_easy + comp_med + comp_hard
    
    def describe_arc(x, y, r, start_angle, end_angle):
        if end_angle <= start_angle:
            return ""
        # SVG angles: 0 is top, 90 is right, 180 is bottom, 270 is left.
        # polar_to_cartesian uses 0 as right, so we offset by -90 inside it.
        def polar_to_cartesian(cx, cy, radius, angle_deg):
            angle_rad = (angle_deg - 90) * math.pi / 180.0
            return cx + radius * math.cos(angle_rad), cy + radius * math.sin(angle_rad)

        start = polar_to_cartesian(x, y, r, end_angle)
        end = polar_to_cartesian(x, y, r, start_angle)
        large_arc_flag = "0" if end_angle - start_angle <= 180 else "1"
        return f"M {start[0]:.2f} {start[1]:.2f} A {r} {r} 0 {large_arc_flag} 0 {end[0]:.2f} {end[1]:.2f}"

    # Arc backgrounds
    # Easy: bottom-left (approx 215 to 325)
    # Med: top (approx -25 to 85)
    # Hard: bottom-right (approx 95 to 205)
    bg_med = describe_arc(150, 100, 60, -25, 85)
    bg_hard = describe_arc(150, 100, 60, 95, 205)
    bg_easy = describe_arc(150, 100, 60, 215, 325)

    # Progress arcs
    fg_med = describe_arc(150, 100, 60, -25, -25 + (comp_med / total_med * 110)) if comp_med > 0 else ""
    fg_hard = describe_arc(150, 100, 60, 95, 95 + (comp_hard / total_hard * 110)) if comp_hard > 0 else ""
    fg_easy = describe_arc(150, 100, 60, 215, 215 + (comp_easy / total_easy * 110)) if comp_easy > 0 else ""

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 600 200">
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
    
    <!-- Background -->
    <rect class="bg" width="600" height="200" rx="10" />
    
    <!-- Donut Chart -->
    <path class="ring-bg-med" d="{bg_med}" />
    <path class="ring-bg-hard" d="{bg_hard}" />
    <path class="ring-bg-easy" d="{bg_easy}" />
    
    <path class="ring-med" d="{fg_med}" />
    <path class="ring-hard" d="{fg_hard}" />
    <path class="ring-easy" d="{fg_easy}" />
    
    <!-- Center Text -->
    <text x="135" y="105" class="text-huge" text-anchor="middle">{completed}</text>
    <text x="175" y="105" class="text-small" text-anchor="middle">/{total}</text>
    <text x="150" y="130" class="text-medium" text-anchor="middle"><tspan fill="#00b8a3">✓</tspan> Solved</text>
    
    <!-- Right side stats -->
    <g transform="translate(400, 25)">
        <rect class="box" x="0" y="0" width="170" height="40" />
        <text x="15" y="25" class="text-large text-easy">Easy</text>
        <text x="155" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_easy}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_easy}</tspan></text>
    </g>
    <g transform="translate(400, 80)">
        <rect class="box" x="0" y="0" width="170" height="40" />
        <text x="15" y="25" class="text-large text-medium-diff">Med.</text>
        <text x="155" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_med}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_med}</tspan></text>
    </g>
    <g transform="translate(400, 135)">
        <rect class="box" x="0" y="0" width="170" height="40" />
        <text x="15" y="25" class="text-large text-hard">Hard</text>
        <text x="155" y="25" class="text-large" text-anchor="end"><tspan fill="#fff">{comp_hard}</tspan><tspan fill="#8c8c8c" font-size="14px">/{total_hard}</tspan></text>
    </g>
</svg>"""
    return svg

svg_content = generate_svg(12, 4, 0)
with open('test_stats.svg', 'w') as f:
    f.write(svg_content)
print("Generated test_stats.svg")
