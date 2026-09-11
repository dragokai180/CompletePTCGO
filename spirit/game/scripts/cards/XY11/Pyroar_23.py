from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3253d6e-2710-5d1b-859b-0a32edfb3380',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Incinerate',
            game_text="Before doing damage, discard all Pokémon Tool cards attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
