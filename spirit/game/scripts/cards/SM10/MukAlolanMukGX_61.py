from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e91f6b81-02b7-54e9-859c-9e3d461a08f0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MukAlolanMukGX.Name',
    display_name='Muk & Alolan Muk-GX',
    searchable_by=['Muk & Alolan Muk-GX', 'Basic', 'TAG TEAM', 'GX', 'MukAlolanMukGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=61,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=89,
    abilities=[
        Attack(
            title='Severe Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 8 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Poison Absorption',
            game_text="If your opponent's Active Pokémon is Poisoned, heal 100 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Nasty Goo Mix-GX',
            game_text="Your opponent's Active Pokémon is now Paralyzed and Poisoned. If this Pokémon has at least 4 extra Energy attached to it (in addition to this attack's cost), put 15 damage counters instead of 1 on that Pokémon between turns. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
