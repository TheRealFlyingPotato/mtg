purchased = """1 Reviving Vapors
1 Heartwarming Redemption
1 Clearwater Goblet
1 Gerrard Capashen
1 Ivory Tower
1 Lifegift
1 Gift of Paradise
1 Rampant Growth
1 Zur the Enchanter
1 Penance
1 Leyline of Anticipation
1 Repay in Kind
1 Sterling Grove
1 Estrid, the Masked
1 Indestructibility
1 Absorb
1 Forbid
1 Fountain Watch
1 Delaying Shield
1 Solitary Confinement
1 Energy Field
1 Stunning Reversal
1 Platinum Angel
1 Transcendence
1 Hanna, Ship's Navigator
1 Lich
1 Arcane Signet"""

decklist = """1 Kenrith, the Returned King
1 Lich
1 Land Tax
1 Courser of Kruphix
1 Twilight Prophet
1 Reviving Vapors
1 Heartwarming Redemption
1 Phyrexian Arena
1 Clearwater Goblet
1 Gerrard Capashen
1 Lightning Helix
1 Retreat to Kazandu
1 Zuran Orb
1 Ivory Tower
1 Sunscorch Regent
1 Armadillo Cloak
1 Authority of the Consuls
1 Lifegift
1 Smothering Tithe
1 Gift of Paradise
1 Sakura-Tribe Elder
1 Rampant Growth
1 Skirge Familiar
1 Chromatic Lantern
1 Dockside Extortionist
1 Hour of Promise
1 Oracle of Mul Daya
1 Arcane Signet
1 Sidisi, Undead Vizier
1 Demonic Tutor
1 Enlightened Tutor
1 Plea for Guidance
1 Dark Petition
1 Zur the Enchanter
1 Wilderness Reclamation
1 Penance
1 Midnight Clock
1 Training Grounds
1 Vedalken Orrery
1 Leyline of Anticipation
1 Repay in Kind
1 Omniscience
1 Sterling Grove
1 Estrid, the Masked
1 Indestructibility
1 Heroic Intervention
1 Privileged Position
1 Dovin's Veto
1 Absorb
1 Forbid
1 Fountain Watch
1 Curator's Ward
1 Delaying Shield
1 Solitary Confinement
1 Energy Field
1 Stunning Reversal
1 Platinum Angel
1 Transcendence
1 Elixir of Immortality
1 Hanna, Ship's Navigator
1 Eternal Witness
1 Wrath of God
1 Cyclonic Rift
1 Anguished Unmaking
""".split('\n')

for card in decklist:
  if card not in purchased:
    print(card)