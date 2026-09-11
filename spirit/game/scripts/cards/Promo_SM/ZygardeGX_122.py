from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a96fb64-d01d-5301-962a-7f4222ed7189',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name',
    display_name='Zygarde-GX',
    searchable_by=['Zygarde-GX', 'Basic', 'GX', 'ZygardeGX'],
    subtypes=['Basic', 'GX'],
    collector_number=122,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Attack(
            title='Vibration',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Cell Storm',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Liberation-GX',
            game_text="Your opponent reveals their hand. This attack does 120 damage for each Energy card you find there. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
