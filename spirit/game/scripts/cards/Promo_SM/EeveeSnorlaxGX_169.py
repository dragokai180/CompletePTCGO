from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='883606c4-e5bd-5073-8c94-43e96d581c54',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EeveeSnorlaxGX.Name',
    display_name='Eevee & Snorlax-GX',
    searchable_by=['Eevee & Snorlax-GX', 'Basic', 'TAG TEAM', 'GX', 'EeveeSnorlaxGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=169,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Cheer Up',
            game_text='Attach an Energy card from your hand to 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dump Truck Press',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Megaton Friends-GX',
            game_text="If this Pokémon has at least 1 extra Energy attached to it (in addition to this attack's cost), draw cards until you have 10 cards in your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=210,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
