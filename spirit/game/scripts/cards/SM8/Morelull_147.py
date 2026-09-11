from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d5fe3ea1-181b-5ad4-bcc9-46186cd44bdd',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    display_name='Morelull',
    searchable_by=['Morelull', 'Basic', 'Morelull'],
    subtypes=['Basic'],
    collector_number=147,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=755,
    abilities=[
        Attack(
            title='Perplex',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
