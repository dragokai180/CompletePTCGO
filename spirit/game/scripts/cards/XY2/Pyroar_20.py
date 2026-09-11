from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c71795f-ec1a-5fc0-b434-43fcf89e13c9',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Ability(
            title='Intimidating Mane',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon."),
        ),
        Attack(
            title='Scorching Fang',
            game_text='You may discard a Fire Energy attached to this Pokémon. If you do, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
