from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9075272f-6470-55b1-8bfe-a30cfb5fba84',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozmaGX.Name',
    display_name='Dusk Mane Necrozma-GX',
    searchable_by=['Dusk Mane Necrozma-GX', 'Basic', 'GX', 'Ultra Beast', 'DuskManeNecrozmaGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=102,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title='Meteor Tempest',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
        ),
        Attack(
            title="Sun's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
