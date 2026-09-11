from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="11d6364b-316f-5863-bbc8-e75c1ad5ece5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScraggy.Name",
    display_name="Marnie's Scraggy",
    searchable_by=["Marnie's Scraggy", "Basic", "MarniesScraggy"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=559,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
