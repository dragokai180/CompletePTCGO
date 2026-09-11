from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='deca934f-5728-5799-9221-e5065211c08d',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name',
    display_name='Seaking',
    searchable_by=['Seaking', 'Stage 1', 'Seaking'],
    subtypes=['Stage 1'],
    collector_number=28,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name',
    family_id=118,
    abilities=[
        Attack(
            title='Soaking Horn',
            game_text='If this Pokémon was healed during this turn, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
