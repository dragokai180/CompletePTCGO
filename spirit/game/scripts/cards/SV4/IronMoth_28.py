from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d5f294d1-f230-5c43-89f4-d3b63bd6b7c8',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name',
    display_name='Iron Moth',
    searchable_by=['Iron Moth', 'Basic', 'Future', 'IronMoth'],
    subtypes=['Basic', 'Future'],
    collector_number=28,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=994,
    abilities=[
        Ability(
            title='Thermal Reactor',
            game_text='Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may move any amount of Fire Energy from your other Pokémon to it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Heat Ray',
            game_text="During your next turn, this Pokémon can't use Heat Ray.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
