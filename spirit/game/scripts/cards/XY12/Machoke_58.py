from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c765d06d-1318-527f-a782-dbf65f739797',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    display_name='Machoke',
    searchable_by=['Machoke', 'Stage 1', 'Machoke'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    family_id=66,
    abilities=[
        Attack(
            title='Karate Chop',
            game_text='This attack does 60 damage minus 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator='-',
            effect=standard_attack,
        ),
        Attack(
            title='Submission',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
