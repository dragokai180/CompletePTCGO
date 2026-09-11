from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ac70f91-f395-580b-a6e8-1ca694f0d5bc',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name',
    display_name='Nacli',
    searchable_by=['Nacli', 'Basic', 'Nacli'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=932,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Stone Edge',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
