from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fad59901-27ad-535c-8a78-26899cd0a222',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MachampEX.Name',
    display_name='Machamp-EX',
    searchable_by=['Machamp-EX', 'Basic', 'EX', 'MachampEX'],
    subtypes=['Basic', 'EX'],
    collector_number=108,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=68,
    abilities=[
        Attack(
            title='Steaming Mad',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
        ),
        Attack(
            title='Crazy Hammer',
            game_text='If this Pokémon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
