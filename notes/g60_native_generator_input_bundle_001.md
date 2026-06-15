# G60 native generator input bundle 001

Status: g60_native_generator_input_bundle_built

## Purpose

Prepare canonical G60-native inputs for the next Gap A generator search.

## Summary

- old_source: "/data/data/com.termux/files/home/dev/zarchive/zarchive/hyperxi_lab/reports/true_quotients/export_thalean_graph_definition.json"
- current_source: "/data/data/com.termux/files/home/dev/cori/aletheos.ai/public_html/labs/registered_boundary_flux/data/canonical_g60_local_edges.v1.csv"
- map_source: "/data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/old_g60_to_current_g60_vertex_map_001.json"
- old_edges: 120
- mapped_old_edges: 120
- current_edges: 120
- mapped_old_equals_current: true
- old_summary: {"automorphism_count": 480, "degree_set": [4], "diameter": 6, "edges": 120, "graph6": "{to?GKC@H??@?BGA@G?A@A?G?Q??CG?_G??????G??@???D???K????????G???B????O???@G???_?????C???OA?????o???GG????_@????@A????CC????A?G?????a???O_??O??A??I???@???@??@??D???G??A???O??I???O??@?_??P???C?G???G?OC???A?@??O??@???G?A??@??C??O???_?CA???@???_?G??A???G??_??C??O??O???O?@?@???@???_??O??G?O?_??O??A?_C", "shell_profile": [1, 4, 8, 16, 24, 6, 1], "triangles": 40, "vertices": 60}
- degree_counts_current: {"4": 60}
- relabeled_a_size: 60
- relabeled_b_size: 60
- relabeled_pair_count: 30
- g15_sign_rows: 30
- g15_sign_summary: {"G15_edges": 30, "G15_vertices": 15, "G30_edges": 60, "G30_vertices": 30, "G60_edges": 120, "G60_vertices": 60, "negative_edges": 20, "positive_edges": 10}
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "search_g60_native_overlay_generator_family_001"

## Boundary

- This builds a native input bundle only.
- It does not derive a WXYZTI generator.
- It does not close Gap A.
- It does not prove full G900.

## Checks

- PASS old_def_exists: /data/data/com.termux/files/home/dev/zarchive/zarchive/hyperxi_lab/reports/true_quotients/export_thalean_graph_definition.json
- PASS old_pairs_exists: /data/data/com.termux/files/home/dev/zarchive/zarchive/hyperxi_lab/reports/quotients/g60_involution_pairs.json
- PASS old_signs_exists: /data/data/com.termux/files/home/dev/zarchive/zarchive/hyperxi_lab/reports/quotients/g15_edge_sign_table.json
- PASS current_edges_exists: /data/data/com.termux/files/home/dev/cori/aletheos.ai/public_html/labs/registered_boundary_flux/data/canonical_g60_local_edges.v1.csv
- PASS map_exists: /data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/old_g60_to_current_g60_vertex_map_001.json
- PASS old_edge_count_120: 120
- PASS mapped_old_edge_count_120: 120
- PASS current_edge_count_120: 120
- PASS mapped_old_equals_current: {'intersection': 120, 'mapped_only': 0, 'current_only': 0}
- PASS relabeled_a_size_60: 60
- PASS relabeled_b_size_60: 60
- PASS relabeled_pair_count_30: 30
- PASS g15_sign_rows_30: 30
- PASS no_gap_a_claim_made: input bundle only
