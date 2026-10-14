# Technical visual generators

These scripts turn realistic source photos into the technical, data-driven images used on the website: detection boxes with confidence, 2D-to-wireframe conversion, measurements, heat maps, data panels and flow lines. All overlay text is drawn in code, so every label and number stays exact and readable.

| Script | Produces |
|---|---|
| `hud.py` | Shared toolkit: boxes, chips, panels, heat maps, wireframes, flows |
| `overlay_provision.py` | Full ProVision AI technical view (`IMG-10-detail.jpg`) |
| `make_products.py` | Full technical views for ProChurn, DEO Suite, ProSight, ProTrace and the pilot review (`IMG-11-detail.jpg` to `IMG-15-detail.jpg`) |
| `make_cards.py` | Card-size product versions with large callouts (`IMG-10` to `IMG-15`) |
| `make_industries.py` | Industry grid images (`IND-01` to `IND-09`) |
| `make_services.py` | Service card visuals: product cut-out plus data callouts (`IMG-02` to `IMG-09`) |

## Run
```bash
pip install pillow numpy opencv-python-headless
python3 tools/visuals/make_industries.py          # all industries
python3 tools/visuals/make_industries.py IND-05   # one slot
```

## Source photos
Place the untouched source photos in `tools/visuals/src/` (not committed; they are kept in the Prowesstics image archive `Prowesstics_Website_Images_Realistic_Batch02/gamma_batch03`). Expected names: `GAMMA_IND-01.jpg` to `GAMMA_IND-09.jpg`, `GAMMA_IMG-11.jpg`, `GAMMA_IMG-13.jpg` to `GAMMA_IMG-15.jpg`, `SRC_IMG-10.png`, `SRC_IMG-12.png`, and the service cut-outs `IMG-02.png` to `IMG-09.png`.

## Rules
- Every overlay carries the note "Illustrative visualisation".
- Numbers that describe Prowesstics results must come from case studies or collateral; operational readouts (counts, IDs, timestamps) are illustrative examples.
- Keep two versions of each product image: a card version with three or four large callouts, and a `-detail.jpg` with the full technical overlay that opens in the lightbox.
