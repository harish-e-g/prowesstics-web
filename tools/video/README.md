# Hero film: Smart Assembly and Packing Line

`public/video/smart-assembly-line.mp4` is the 2-minute factory automation and traceability film
(background music and voiceover), rebranded to Prowesstics from the partner cut
`Ladera_JKFenner_Smart_Line_Film_1080p.mp4` (Downloads/Ladera_JKFenner_Film_Revamp, 10 Oct 2026).

How it was made:
1. `scan.py` cuts logo templates from the source (title at 3.5 s, corner badge at 30 s, end card at 119.5 s) and
   `scan2.py` measures, frame by frame, how visible the partner logo is at its three positions
   (title card, bottom-right corner badge, end card) by projecting each frame onto a logo template.
2. `render.py` places the Prowesstics overlays (`ov_title.png`, `ov_bug.png`, `ov_end.png`) at the
   same positions with matching opacity, so they fade in and out with the original, and re-encodes
   (H.264 CRF 24, AAC 160k, faststart) with the original soundtrack untouched.

Set `SRC` in both scripts to the source film path, then run `python3 scan2.py` and `python3 render.py`.
