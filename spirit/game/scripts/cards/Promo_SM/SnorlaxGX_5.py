from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='284585c5-ca7c-5de6-9720-26d4cd90b869',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxGX.Name',
    display_name='Snorlax-GX',
    searchable_by=['Snorlax-GX', 'Basic', 'GX', 'SnorlaxGX'],
    subtypes=['Basic', 'GX'],
    collector_number=5,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Attack(
            title='Collapse',
            game_text='This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Thunderous Snore',
            game_text='This attack can be used if this Pokémon is Asleep. If it is not Asleep, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 5},
            damage=180,
            effect=standard_attack,
        ),
        Attack(
            title='Pulverizing Pancake-GX',
            game_text="This Pokémon is now Asleep. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 5},
            damage=210,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
