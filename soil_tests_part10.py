# === Stage 10: Постраничный вывод ===
# Project: SoilTests
def paginate_plot_areas(plots, page, per_page):
    if per_page <= 0:
        return []
    start = (page - 1) * per_page
    return plots[start:start + per_page]


def paginate_plot_areas_with_meta(plots, page, per_page):
    if per_page <= 0:
        return {"items": [], "page": page, "per_page": per_page,
                "total": 0, "total_pages": 0}
    total = len(plots)
    total_pages = (total + per_page - 1) // per_page
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    start = (page - 1) * per_page
    items = plots[start:start + per_page]
    return {"items": items, "page": page, "per_page": per_page,
            "total": total, "total_pages": total_pages}


def build_page_of_plots(plots, page, per_page):
    if per_page <= 0:
        raise ValueError("per_page must be a positive integer")
    if page < 1:
        raise ValueError("page must be a positive integer")
    page_data = paginate_plot_areas_with_meta(plots, page, per_page)
    return page_data["items"], page_data


def render_plot_areas_table(page_items, per_page, page, total_pages):
    rows = []
    for item in page_items:
        rows.append(f"<tr>"
                    f"<td>{item.get('name', '')}</td>"
                    f"<td>{item.get('area', '')}</td>"
                    f"<td>{item.get('soil_type', '')}</td>"
                    f"<td>{item.get('sample_date', '')}</td>"
                    f"</tr>")
    header = "<tr><th>Name</th><th>Area</th><th>Soil Type</th><th>Sample Date</th></tr>"
    footer = (f"<tr><td colspan='4' style='text-align:center'>"
              f"Page {page} of {total_pages}</td></tr>")
    return "<table>" + header + "\n".join(rows) + footer + "</table>"
