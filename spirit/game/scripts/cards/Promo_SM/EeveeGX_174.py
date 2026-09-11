from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b505fce-184b-5118-83ea-e6be69caccb2',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EeveeGX.Name',
    display_name='Eevee-GX',
    searchable_by=['Eevee-GX', 'Basic', 'GX', 'EeveeGX'],
    subtypes=['Basic', 'GX'],
    collector_number=174,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Ability(
            title='Ascension DNA',
            game_text="Once during your turn (before your attack), if you have a Pokémon in your hand that evolves from Eevee, you may put that card onto this Pokémon to evolve it. Before evolving, heal all damage from this Pokémon. You can't use this Ability during your first turn or on the turn this Pokémon was put into play.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
        ),
        Attack(
            title='Boost Dash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title='Joy Maker-GX',
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
