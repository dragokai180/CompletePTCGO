from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c3e6ca5-5c7c-5799-b090-759c8f562e0b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.XurkitreeGX.Name',
    display_name='Xurkitree-GX',
    searchable_by=['Xurkitree-GX', 'Basic', 'GX', 'Ultra Beast', 'XurkitreeGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=68,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=796,
    abilities=[
        Ability(
            title='Flashing Head',
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon that have any Special Energy attached to them.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon that have any Special Energy attached to them."),
        ),
        Attack(
            title='Rumbling Wires',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
        Attack(
            title='Lighting-GX',
            game_text="Your opponent reveals their hand. Add a card you find there to their Prize cards face down. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
