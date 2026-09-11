from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77d3a104-ec40-5b97-a676-3d13914c3b7f',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShuckleGX.Name',
    display_name='Shuckle-GX',
    searchable_by=['Shuckle-GX', 'Basic', 'GX', 'ShuckleGX'],
    subtypes=['Basic', 'GX'],
    collector_number=17,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=213,
    abilities=[
        Ability(
            title='Protective Shell',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon that have 2 or fewer Energy attached to them.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon that have 2 or fewer Energy attached to them."),
        ),
        Attack(
            title='Triple Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 3 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wrap-GX',
            game_text="Your opponent's Active Pokémon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
