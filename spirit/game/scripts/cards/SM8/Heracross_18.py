from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9677e9ff-135f-5c6d-83b4-f4c7749a94a0',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name',
    display_name='Heracross',
    searchable_by=['Heracross', 'Basic', 'Heracross'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Powerful Friends',
            game_text='If you have any Stage 2 Pokémon on your Bench, this attack does 90 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
