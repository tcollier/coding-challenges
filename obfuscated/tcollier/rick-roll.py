ńămё = '᠎R᠎᠎᠎i᠎᠎c﻿​᠎k᠎​᠎᠎​᠎ ᠎᠎᠎D​᠎᠎​᠎​᠎i​᠎᠎​᠎​᠎l​᠎​᠎l​᠎o​᠎᠎​᠎n'
ňămȅ = len([ńămё, ńămё])
ňămё = ńămё[ňămȅ:ňămȅ:ňămȅ]
ňāmȅ = ['﻿​᠎', '᠎​᠎᠎​᠎', '᠎', '​᠎', '​᠎​᠎', '​᠎᠎​᠎​᠎', '᠎᠎', '᠎᠎᠎', '​᠎᠎​᠎']
ňāmё = [-41, -6, 11, 28, 32, 35, 36, 38, 41]
ńāmё = dict(zip(ňāmȅ, ňāmё))
ńāmȅ = ňāmё[ňămȅ] + ňămȅ * ňāmё[ňămȅ + ňămȅ] - ňămȅ
ňāmё = ňămё[ňāmё[ňămȅ + ňămȅ]:ňāmё[ňămȅ + ňămȅ + ňămȅ]]
for ńămȅ in ńămё:
  if ńămȅ in [ňămȅ for ňămȅ in '﻿​᠎᠎​᠎']:
    ňāmё += ńămȅ
  else:
    ňămё += chr(ńāmё[ňāmё] + ńāmȅ)
    ňāmё = ňāmё[ńāmё[ňāmё]:ńāmё[ňāmё]:ńāmё[ňāmё]]
print(ňămё)
