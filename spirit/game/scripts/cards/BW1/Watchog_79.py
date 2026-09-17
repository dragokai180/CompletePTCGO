from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack

card = PokemonCardDef(
    guid="7f4966fd-4082-5e69-1855-fee0e79f0ffa",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    weakness_type=PokemonTypes.FIGHTING,
    family_id=505,
    abilities=[
        Attack(title="Confuse Ray", cost={PokemonTypes.COLORLESS: 2},
               game_text="The Defending Pokémon is now Confused.",
               effect=bw_legacy_attack),
        Attack(title="Hyper Fang", cost={PokemonTypes.COLORLESS: 2}, damage=60,
               game_text="Flip a coin. If tails, this attack does nothing.",
               effect=bw_legacy_attack),
    ],
)

