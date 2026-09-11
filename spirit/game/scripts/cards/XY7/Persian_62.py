from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c45e2878-e89a-51e3-8530-a7ff4f454bf4',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name',
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=62,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=52,
    abilities=[
        Attack(
            title='Fake Out',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
