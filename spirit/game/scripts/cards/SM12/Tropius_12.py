from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='03265989-fea7-5e88-8357-1f0d19f47cb3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name',
    display_name='Tropius',
    searchable_by=['Tropius', 'Basic', 'Tropius'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=357,
    abilities=[
        Attack(
            title='Synthesis',
            game_text='Search your deck for a Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
