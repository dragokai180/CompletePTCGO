from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='176a9ad7-f2d2-5efa-a0dd-908db043d265',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name',
    display_name='Keldeo',
    searchable_by=['Keldeo', 'Basic', 'Keldeo'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=647,
    abilities=[
        Attack(
            title='Bail Out',
            game_text='Put a Water Pokémon from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Resolute Blade',
            game_text="This attack does 20 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
