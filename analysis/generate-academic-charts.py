from pathlib import Path

OUT = Path(__file__).parent / "charts"
OUT.mkdir(exist_ok=True)

TEXT = "#050315"
MUTED = "#5f5b73"
GRID = "#d8d6ea"
PRIMARY = "#3930ed"
SECONDARY = "#8a86f6"
LIGHT = "#f4f3ff"
BG = "#ffffff"


def svg_header(width=900, height=560):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="{BG}"/>',
        f'<style>text{{font-family:Arial, Helvetica, sans-serif;fill:{TEXT}}}.muted{{fill:{MUTED}}}.title{{font-weight:700;font-size:25px}}.subtitle{{font-size:15px}}.axis{{stroke:{TEXT};stroke-width:1.2}}.grid{{stroke:{GRID};stroke-width:1}}.label{{font-size:14px}}.tick{{font-size:12px;fill:{MUTED}}}.note{{font-size:12px;fill:{MUTED}}}</style>',
    ]


def finish(parts):
    parts.append("</svg>")
    return "\n".join(parts)


def pre_post():
    width, height = 900, 560
    left, right, top, bottom = 120, 70, 95, 440
    maxv = 5
    vals = [("Pre-test", 3.821, "#4a46d9"), ("Post-test", 3.228, "#9a97f7")]
    parts = svg_header(width, height)
    parts += [
        '<text x="48" y="46" class="title">Figure 1. Pre-test and post-test self-rating</text>',
        '<text x="48" y="73" class="subtitle muted">Mean score on a 1-5 scale; lower post-test rating is interpreted in the discussion as recalibration.</text>',
    ]
    plot_w = width - left - right
    plot_h = bottom - top
    for i in range(0, 6):
        y = bottom - plot_h * (i / maxv)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{left-18}" y="{y+4:.1f}" text-anchor="end" class="tick">{i}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{width-right}" y2="{bottom}" class="axis"/>')
    bar_w = 140
    xs = [310, 590]
    for (label, val, color), x in zip(vals, xs):
        bar_h = plot_h * val / maxv
        y = bottom - bar_h
        parts.append(f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{bar_h:.1f}" fill="{color}"/>')
        parts.append(f'<text x="{x+bar_w/2}" y="{y-14:.1f}" text-anchor="middle" font-size="21" font-weight="700">{val:.2f}</text>')
        parts.append(f'<text x="{x+bar_w/2}" y="{bottom+32}" text-anchor="middle" class="label">{label}</text>')
    parts.append(f'<text x="{width/2}" y="515" text-anchor="middle" font-size="16" font-weight="700" fill="{PRIMARY}">Mean change: -0.593 (post - pre)</text>')
    (OUT / "pre-post-awareness.svg").write_text(finish(parts), encoding="utf-8")


def gap_indicators():
    width, height = 920, 560
    left, right, top, bottom = 245, 85, 100, 440
    data = [
        ("Any gap", 31, 75.6),
        ("Budget-control gap", 22, 53.7),
        ("Default-option gap", 22, 53.7),
        ("Time-pressure gap", 20, 48.8),
        ("Information-checking gap", 19, 46.3),
    ]
    max_count = 41
    parts = svg_header(width, height)
    parts += [
        '<text x="48" y="46" class="title">Figure 2. Rule-based self-perception / choice gaps</text>',
        '<text x="48" y="73" class="subtitle muted">Number of participants with each gap indicator, N = 41.</text>',
    ]
    plot_w = width - left - right
    for i in range(0, 42, 10):
        x = left + plot_w * i / max_count
        parts.append(f'<line x1="{x:.1f}" y1="{top-10}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        parts.append(f'<text x="{x:.1f}" y="{bottom+24}" text-anchor="middle" class="tick">{i}</text>')
    parts.append(f'<line x1="{left}" y1="{top-10}" x2="{left}" y2="{bottom}" class="axis"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{width-right}" y2="{bottom}" class="axis"/>')
    y = top
    for idx, (label, count, pct) in enumerate(data):
        bar_w = plot_w * count / max_count
        color = PRIMARY if idx == 0 else SECONDARY
        parts.append(f'<text x="{left-18}" y="{y+24}" text-anchor="end" class="label">{label}</text>')
        parts.append(f'<rect x="{left}" y="{y}" width="{bar_w:.1f}" height="36" fill="{color}"/>')
        parts.append(f'<text x="{left+bar_w+12:.1f}" y="{y+24}" class="label">{count} ({pct:.1f}%)</text>')
        y += 64
    parts.append(f'<text x="{left+plot_w/2}" y="500" text-anchor="middle" class="note">Count of participants</text>')
    (OUT / "gap-indicators.svg").write_text(finish(parts), encoding="utf-8")


def mismatch_recalibration():
    width, height = 900, 560
    left, right, top, bottom = 110, 70, 95, 430
    data = [(0, 0.033, 10), (1, 0.186, 9), (2, 0.500, 4), (3, 0.833, 6), (4, 1.277, 12)]
    max_x, max_y = 4, 1.4
    parts = svg_header(width, height)
    parts += [
        '<text x="48" y="46" class="title">Figure 3. Mismatch count and recalibration</text>',
        '<text x="48" y="73" class="subtitle muted">Recalibration = pre-test score minus post-test score. Larger values mean a larger drop in self-rating.</text>',
    ]
    plot_w = width - left - right
    plot_h = bottom - top
    for i in range(0, 5):
        x = left + plot_w * i / max_x
        parts.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        parts.append(f'<text x="{x:.1f}" y="{bottom+24}" text-anchor="middle" class="tick">{i}</text>')
    for j in range(0, 8):
        val = j * 0.2
        y = bottom - plot_h * val / max_y
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" class="grid"/>')
        parts.append(f'<text x="{left-16}" y="{y+4:.1f}" text-anchor="end" class="tick">{val:.1f}</text>')
    parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" class="axis"/>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{width-right}" y2="{bottom}" class="axis"/>')
    points = []
    for xval, yval, n in data:
        x = left + plot_w * xval / max_x
        y = bottom - plot_h * yval / max_y
        points.append((x, y))
        r = 8 + n * 0.9
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{PRIMARY}" fill-opacity="0.78"/>')
        parts.append(f'<text x="{x:.1f}" y="{y-18:.1f}" text-anchor="middle" class="tick">n={n}</text>')
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    parts.append(f'<polyline points="{poly}" fill="none" stroke="{TEXT}" stroke-width="2"/>')
    parts.append(f'<text x="{left+plot_w/2}" y="505" text-anchor="middle" class="note">Mismatch count</text>')
    parts.append(f'<text x="32" y="{top+plot_h/2}" transform="rotate(-90 32 {top+plot_h/2})" text-anchor="middle" class="note">Mean recalibration</text>')
    parts.append(f'<text x="{width-right}" y="506" text-anchor="end" font-size="15" font-weight="700" fill="{PRIMARY}">r = 0.758</text>')
    (OUT / "mismatch-recalibration.svg").write_text(finish(parts), encoding="utf-8")


def action_distribution():
    width, height = 980, 620
    left, right, top, bottom = 240, 80, 95, 500
    rows = [
        ("Price drop: viewed", 21),
        ("Price drop: postponed", 12),
        ("Price drop: closed", 8),
        ("Detail: bought now", 15),
        ("Detail: added to cart", 9),
        ("Detail: checked reviews", 11),
        ("Detail: checked rules", 6),
        ("Checkout: kept default", 27),
        ("Checkout: cancelled default", 8),
        ("Final: submitted order", 29),
        ("Final: stopped", 6),
    ]
    max_count = 41
    parts = svg_header(width, height)
    parts += [
        '<text x="48" y="46" class="title">Figure 4. Selected action frequencies by stage</text>',
        '<text x="48" y="73" class="subtitle muted">Counts out of 41 completed sessions. Use as an optional presentation figure.</text>',
    ]
    plot_w = width - left - right
    for i in range(0, 42, 10):
        x = left + plot_w * i / max_count
        parts.append(f'<line x1="{x:.1f}" y1="{top-8}" x2="{x:.1f}" y2="{bottom}" class="grid"/>')
        parts.append(f'<text x="{x:.1f}" y="{bottom+24}" text-anchor="middle" class="tick">{i}</text>')
    parts.append(f'<line x1="{left}" y1="{bottom}" x2="{width-right}" y2="{bottom}" class="axis"/>')
    y = top
    for label, count in rows:
        bar_w = plot_w * count / max_count
        color = PRIMARY if count >= 20 else SECONDARY
        parts.append(f'<text x="{left-16}" y="{y+19}" text-anchor="end" class="label">{label}</text>')
        parts.append(f'<rect x="{left}" y="{y}" width="{bar_w:.1f}" height="26" fill="{color}"/>')
        parts.append(f'<text x="{left+bar_w+10:.1f}" y="{y+19}" class="label">{count}</text>')
        y += 36
    parts.append(f'<text x="{left+plot_w/2}" y="565" text-anchor="middle" class="note">Number of participants</text>')
    (OUT / "action-distribution.svg").write_text(finish(parts), encoding="utf-8")


if __name__ == "__main__":
    pre_post()
    gap_indicators()
    mismatch_recalibration()
    action_distribution()
    print("Generated academic SVG charts in", OUT)
