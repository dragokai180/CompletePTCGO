from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="81e3fe26-5ed8-5733-bb0e-d63bc5c1f52b",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic", "Ekans"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=23,
    abilities=[
        Attack(
            title="Poison Blend",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)
