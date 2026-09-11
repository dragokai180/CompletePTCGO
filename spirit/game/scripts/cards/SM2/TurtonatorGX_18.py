from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74d933f3-5b15-5d3c-9ff3-e6fe70059a7a',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TurtonatorGX.Name',
    display_name='Turtonator-GX',
    searchable_by=['Turtonator-GX', 'Basic', 'GX', 'TurtonatorGX'],
    subtypes=['Basic', 'GX'],
    collector_number=18,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=776,
    abilities=[
        Attack(
            title='Shell Trap',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Bright Flame',
            game_text='Discard 2 Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Nitro Tank-GX',
            game_text="Attach 5 Fire Energy cards from your discard pile to your Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
