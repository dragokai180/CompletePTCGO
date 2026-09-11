from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='48da419f-3215-5cc2-a2e2-65537d72ce96',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name',
    display_name='Girafarig',
    searchable_by=['Girafarig', 'Basic', 'Girafarig'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=203,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Psybite',
            game_text='If this Pokémon has any Psychic Energy attached to it, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
