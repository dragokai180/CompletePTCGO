from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import discard_own_energy

card = PokemonCardDef(
    guid="14a373f0-db5d-5fa3-ac28-e8d9bbe2b805",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel","Basic","Numel"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=discard_own_energy,
        ),
    ],
)
