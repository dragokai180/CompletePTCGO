from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a7f49a5-db64-5ef1-88e4-ba361c46607c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name',
    display_name='Meloetta',
    searchable_by=['Meloetta', 'Basic', 'Meloetta'],
    subtypes=['Basic'],
    collector_number=85,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=648,
    abilities=[
        Attack(
            title='Accelerating Spin',
            game_text='Attach 2 Fighting Energy cards from your discard pile to this Pokémon. Then, switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Prima Rondo',
            game_text='If this Pokémon has any Psychic Energy attached to it, this attack does 50 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
