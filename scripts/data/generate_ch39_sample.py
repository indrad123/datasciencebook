"""Generate deterministic distributor-segmentation data for Chapter 39."""

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch39_sample.csv"

PROFILES = (
    ("steady_bulk", -1.10, 0.78),
    ("frequent_broad_mix", 1.02, 0.90),
    ("campaign_specialist", 0.05, -1.12),
)


def silhouette(point, own, all_points):
    same = [p for p, group in all_points if group == own and p != point]
    a = sum(math.dist(point, p) for p in same) / len(same)
    other_means = []
    for group, _, _ in PROFILES:
        if group != own:
            members = [p for p, g in all_points if g == group]
            other_means.append(sum(math.dist(point, p) for p in members) / len(members))
    b = min(other_means)
    return (b - a) / max(a, b)


def build_rows():
    constructed = []
    for group, cx, cy in PROFILES:
        for i in range(40):
            angle = 2 * math.pi * i / 40
            radial = 0.22 + 0.11 * ((i * 7) % 11) / 10
            x = cx + radial * math.cos(angle) + 0.035 * math.sin(3 * angle)
            y = cy + 0.72 * radial * math.sin(angle) + 0.025 * math.cos(2 * angle)
            constructed.append(((x, y), group, cx, cy))
    points = [(p, group) for p, group, _, _ in constructed]
    rows = []
    for idx, (point, group, cx, cy) in enumerate(constructed, 1):
        x, y = point
        distance = math.dist(point, (cx, cy))
        rows.append(
            {
                "distributor_id": f"D39-{idx:03d}",
                "designed_profile": group,
                "orders_per_month": f"{18 + 5.5 * x:.2f}",
                "broad_mix_share": f"{0.52 + 0.18 * y:.4f}",
                "orders_scaled": f"{x:.6f}",
                "mix_scaled": f"{y:.6f}",
                "assigned_cluster": group,
                "centroid_orders_scaled": f"{cx:.2f}",
                "centroid_mix_scaled": f"{cy:.2f}",
                "distance_to_centroid": f"{distance:.6f}",
                "silhouette_value": f"{silhouette(point, group, points):.6f}",
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
