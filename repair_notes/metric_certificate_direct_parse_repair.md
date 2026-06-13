# Metric Certificate Direct Parse Repair

Project 19 found that the current `source/kernel_payload/x_sigma_edges.csv` edge file recomputes to:

- diameter 8
- radius 6
- center_count 342
- eccentricity_counts {6:342, 7:526, 8:32}

The existing Project 18 metric certificate reports the same diameter/radius but different detailed metric counts.

The likely repair is to ensure `scripts/build_metric_certificate.py` reads the explicit global edge columns:

    u_vertex,v_vertex

when present, instead of inferring slot/local coordinates from the first four integer fields.

This branch regenerates the metric certificate from the explicit global edge columns and then updates downstream certificate/manuscript material as needed.
