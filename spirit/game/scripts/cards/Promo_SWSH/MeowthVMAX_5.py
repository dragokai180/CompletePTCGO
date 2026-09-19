from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e33d9c2-3c19-5c67-95c2-a74a8852f96f',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MeowthVMAX.Name',
    display_name='Meowth VMAX',
    searchable_by=['Meowth VMAX', 'VMAX', 'MeowthVMAX'],
    subtypes=['VMAX'],
    collector_number=5,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH005'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name',
    family_id=52,
    abilities=[
        Attack(
            title='G-Max Gold Rush',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
