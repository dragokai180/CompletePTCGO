from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f4943309-6a2b-5e87-bb1c-db345455876a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name',
    display_name='Latias',
    searchable_by=['Latias', 'Basic', 'Latias'],
    subtypes=['Basic'],
    collector_number=153,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=380,
    abilities=[
        Attack(
            title='Energy Arrow',
            game_text="This attack does 20 damage times the amount of Energy attached to 1 of your opponent's Pokémon to that Pokémon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Speed Wing',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
