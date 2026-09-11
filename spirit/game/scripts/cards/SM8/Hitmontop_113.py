from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1083eb97-b23c-5c2a-8b21-6c695155a742',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name',
    display_name='Hitmontop',
    searchable_by=['Hitmontop', 'Basic', 'Hitmontop'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=237,
    abilities=[
        Attack(
            title='Rapid Spin',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon. If you do, your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Triple Kick',
            game_text='Flip 3 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
