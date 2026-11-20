"""Gera as figuras vetoriais a partir dos resultados do Jupiter."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "resultados" / "resultados-jupiter.csv"
OUTPUT = ROOT / "output" / "pdf"

PLOTS = (
    ("E3", "cap_fila_vagas", "Capacidade da fila (vagas)", "dp_pct",
     "Probabilidade de descarte (%)", "e3-fila.pdf"),
    ("E4", "cenario", "Cenário (tarefas/s, VMs)", "mrt_s",
     "Tempo médio de resposta (s)", "e4-demanda-e-vms.pdf"),
)


def draw(rows, x_key, x_label, y_key, y_label, filename):
    if x_key == "cenario":
        positions = list(range(len(rows)))
        labels = [
            f"({row['taxa_chegada_tarefas_s']}, {row['num_vms']})"
            for row in rows
        ]
    else:
        rows = sorted(rows, key=lambda row: float(row[x_key]))
        positions = [float(row[x_key]) for row in rows]
        labels = [row[x_key] for row in rows]

    values = [float(row[y_key]) for row in rows]
    fig, ax = plt.subplots(figsize=(3.4, 2.22), layout="constrained")
    color = "#194d70"
    metric = "MRT" if y_key == "mrt_s" else "DP"
    ax.plot(positions, values, color=color, marker="o", linewidth=1.45,
            markersize=4, label=metric, zorder=3)
    ax.set(xlabel=x_label, ylabel=y_label, ylim=(0, max(values) * 1.27))
    ax.set_xticks(positions, labels)
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda value, _: f"{value:g}".replace(".", ",")
    ))
    ax.margins(x=0.13)
    ax.grid(axis="y", color="#dbe1e6", linewidth=0.65)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left" if x_key == "taxa_chegada_tarefas_s"
              else "upper right", frameon=False)
    fig.savefig(OUTPUT / filename)
    plt.close(fig)


def draw_comparison():
    panels = (
        ("u.csv", "(a) Utilização das VMs (%)", 110),
        ("mrt.csv", "(b) Tempo médio de resposta (s)", 1.2),
        ("dp.csv", "(c) Probabilidade de descarte (%)", 65),
        ("mqt.csv", "(d) Tempo médio de espera (s)", 1.1),
    )
    styles = (
        (2, "#1764c0", "o", "-"),
        (3, "#cb3038", "s", "--"),
        (4, "#168348", "^", "-."),
        (5, "#8746b2", "D", ":"),
        (6, "#cf7a00", "v", (0, (5, 2, 1, 2))),
    )
    def draw_panel(ax, source, metric, upper_limit):
        with (DATA.parent / "comparativo" / source).open(
            encoding="utf-8-sig", newline=""
        ) as table:
            rows = sorted(csv.DictReader(table, delimiter=";"),
                          key=lambda row: int(row["TAXA_CHEGADA"]))
        rates = [int(row["TAXA_CHEGADA"]) for row in rows]
        if rates != [10, 20, 30, 40, 50]:
            raise ValueError(f"Taxas de chegada inesperadas em {source}: {rates}")

        for vms, color, marker, linestyle in styles:
            values = [float(row[f"NUM_VMS={vms}"]) for row in rows]
            ax.plot(rates, values, color=color, marker=marker, linestyle=linestyle,
                    linewidth=1.35, markersize=4, label=f"{vms} VMs", zorder=3)

        ax.set(xlabel="Taxa de chegada (tarefas/s)", ylabel=metric,
               ylim=(0, upper_limit), xticks=rates)
        ax.grid(axis="y", color="#dbe1e6", linewidth=0.65)
        ax.spines[["top", "right"]].set_visible(False)
        ax.yaxis.set_major_formatter(FuncFormatter(
            lambda value, _: f"{value:g}".replace(".", ",")
        ))
        ax.legend(loc="lower right" if source == "u.csv" else "upper left",
                  frameon=True, facecolor="white", edgecolor="#dddddd",
                  fontsize=7)


    fig, axes = plt.subplots(2, 2, figsize=(6.9, 5.1), layout="constrained")
    for ax, (source, metric, upper_limit) in zip(axes.flat, panels):
        draw_panel(ax, source, metric, upper_limit)
    fig.savefig(OUTPUT / "comparativo-demanda-e-vms.pdf")
    plt.close(fig)

    separate = OUTPUT / "comparativo-separados"
    separate.mkdir(parents=True, exist_ok=True)
    for source, metric, upper_limit in panels:
        fig, ax = plt.subplots(figsize=(3.4, 2.65), layout="constrained")
        draw_panel(ax, source, metric[4:], upper_limit)
        fig.savefig(separate / f"comparativo-{Path(source).stem}.pdf")
        plt.close(fig)


def main():
    with DATA.open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))

    plt.rcParams.update({"font.size": 8, "pdf.fonttype": 42})
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for experiment, *plot_args in PLOTS:
        draw([row for row in rows if row["experimento"] == experiment], *plot_args)
    draw_comparison()


if __name__ == "__main__":
    main()
