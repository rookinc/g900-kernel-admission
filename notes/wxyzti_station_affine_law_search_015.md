# WXYZTI station affine law search 015

Status: wxyzti_station_affine_law_search_recorded

## Output

- row_count: `24`
- modulus: `15`

## Best station-role laws for to_C

- IW: rows=4, from_C=[1, 2, 5], to_C=[0, 2, 10, 14], from_slot=[2, 4, 11, 13]
  - 2*from_A + 12*from_C + 3*from_slot mod 15
  - 2*from_A + 3*from_B + 12*from_C mod 15
  - 2*from_A + 3*from_B + 12*from_fiber_mod15 mod 15
  - 2*from_A + 3*from_B + 12*from_fiber_mod30 mod 15
  - 2*from_A + 3*from_slot + 12*from_fiber_mod15 mod 15
- TI: rows=4, from_C=[2, 4, 11, 13], to_C=[1, 2, 5], from_slot=[1, 2, 5]
- WX: rows=4, from_C=[0, 2, 10, 14], to_C=[2, 4, 11, 13], from_slot=[2, 4, 11, 13]
- XY: rows=4, from_C=[2, 4, 11, 13], to_C=[1, 2, 5], from_slot=[0, 2, 10, 14]
- YZ: rows=4, from_C=[1, 2, 5], to_C=[0, 2, 10, 14], from_slot=[0, 2, 10, 14]
- ZT: rows=4, from_C=[0, 2, 10, 14], to_C=[2, 4, 11, 13], from_slot=[1, 2, 5]

## Exact named tests

- station_role=IW: to_C = from_C + C_delta matches 4/4
- station_role=TI: to_C = from_slot matches 4/4
- station_role=TI: to_C = from_B matches 4/4
- station_role=TI: to_C = from_C + C_delta matches 4/4
- station_role=WX: to_C = from_slot matches 4/4
- station_role=WX: to_C = from_B matches 4/4
- station_role=WX: to_C = from_C + C_delta matches 4/4
- station_role=XY: to_C = from_C + C_delta matches 4/4
- station_role=YZ: to_C = from_slot matches 4/4
- station_role=YZ: to_C = from_B matches 4/4
- station_role=YZ: to_C = from_C + C_delta matches 4/4
- station_role=ZT: to_C = from_C + C_delta matches 4/4
- role_pair=IW/YZ: to_C = from_C + C_delta matches 8/8
- role_pair=TI/XY: to_C = from_C + C_delta matches 8/8
- role_pair=WX/ZT: to_C = from_C + C_delta matches 8/8
- role_class=reverse_partner: to_C = from_slot matches 12/12
- role_class=reverse_partner: to_C = from_B matches 12/12
- role_class=reverse_partner: to_C = from_C + C_delta matches 12/12
- role_class=shared_B: to_C = from_C + C_delta matches 12/12

## Near named tests

- role_class=reverse_partner: to_C = from_B matches 12/12
- role_class=reverse_partner: to_C = from_C + C_delta matches 12/12
- role_class=reverse_partner: to_C = from_slot matches 12/12
- role_class=shared_B: to_C = from_C + C_delta matches 12/12
- role_pair=IW/YZ: to_C = from_C + C_delta matches 8/8
- role_pair=TI/XY: to_C = from_C + C_delta matches 8/8
- role_pair=WX/ZT: to_C = from_C + C_delta matches 8/8
- role_pair=IW/YZ: to_C = from_B matches 4/8
- role_pair=IW/YZ: to_C = from_slot matches 4/8
- role_pair=TI/XY: to_C = from_B matches 4/8
- role_pair=TI/XY: to_C = from_slot matches 4/8
- role_pair=WX/ZT: to_C = from_B matches 4/8
- role_pair=WX/ZT: to_C = from_slot matches 4/8
- station_role=IW: to_C = from_C + C_delta matches 4/4
- station_role=TI: to_C = from_B matches 4/4
- station_role=TI: to_C = from_C + C_delta matches 4/4
- station_role=TI: to_C = from_slot matches 4/4
- station_role=WX: to_C = from_B matches 4/4
- station_role=WX: to_C = from_C + C_delta matches 4/4
- station_role=WX: to_C = from_slot matches 4/4

## Boundary

This is a law search over realized rows only. Affine laws found here do not prove selection from non-realized candidates and do not close Gap A.
