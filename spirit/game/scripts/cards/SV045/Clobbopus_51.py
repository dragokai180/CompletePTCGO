from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='579d5e3f-2e8f-5d19-9d02-736bf68be9de',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name',
    display_name='Clobbopus',
    searchable_by=['Clobbopus', 'Basic', 'Clobbopus'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=852,
    abilities=[
        Attack(
            title='Feint',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
