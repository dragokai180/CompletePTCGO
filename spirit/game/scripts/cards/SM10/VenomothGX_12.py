from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe11c977-a122-5ea7-8066-cef2193b6ef0',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VenomothGX.Name',
    display_name='Venomoth-GX',
    searchable_by=['Venomoth-GX', 'Stage 1', 'GX', 'VenomothGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=12,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    family_id=48,
    abilities=[
        Attack(
            title='Shinobi Mastery',
            game_text="If you played Koga's Trap from your hand during this turn, this attack does 90 more damage. If you played Janine from your hand during this turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Ten-Card Return-GX',
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
