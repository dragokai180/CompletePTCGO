from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import retribution, signal_beam

card = PokemonCardDef(
    guid="b05df036-9f99-5c30-92fe-1276ddec7969",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull","Basic","Duskull"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=signal_beam,
        ),
    ],
)
