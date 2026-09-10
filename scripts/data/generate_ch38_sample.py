"""Generate deterministic geometry data for Chapter 38."""

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch38_sample.csv"
QUERY = (1.05, 0.40)


def build_rows():
    points = []
    for group, base_radius, label in (("ordinary", 0.58, 0), ("late", 1.48, 1)):
        for i in range(24):
            angle = 2 * math.pi * i / 24 + (0.035 if label else 0.0)
            radius = base_radius + 0.10 * math.sin(3 * angle) + 0.04 * math.cos(5 * angle)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            qdist = math.hypot(x - QUERY[0], y - QUERY[1])
            points.append((group, label, i + 1, x, y, radius, qdist))

    ordered = sorted(range(len(points)), key=lambda j: (points[j][6], points[j][0], points[j][2]))
    ranks = {j: rank + 1 for rank, j in enumerate(ordered)}
    rows = []
    for j, (group, label, seq, x, y, radius, qdist) in enumerate(points):
        rows.append(
            {
                "shipment_id": f"G38-{j + 1:03d}",
                "operating_group": group,
                "route_distance_km": f"{5000 + 2000 * x:.1f}",
                "port_wait_hours": f"{8 + 3 * y:.2f}",
                "distance_scaled": f"{x:.6f}",
                "wait_scaled": f"{y:.6f}",
                "late_label": label,
                "radial_position": f"{radius:.6f}",
                "query_distance": f"{qdist:.6f}",
                "query_neighbor_rank": ranks[j],
                "rbf_similarity_gamma_1": f"{math.exp(-(qdist ** 2)):.6f}",
            }
        )
    return rows


def main():
    rows = build_rows()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
