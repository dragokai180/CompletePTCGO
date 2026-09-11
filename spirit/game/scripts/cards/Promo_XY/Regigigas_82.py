from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69c1fa80-da82-5ed7-a73d-2bbe8abfc850',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name',
    display_name='Regigigas',
    searchable_by=['Regigigas', 'Basic', 'Regigigas'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=486,
    abilities=[
        Ability(
            title='Earthen Awakening',
            game_text='Whenever you attach an Energy card from your hand to this Pokémon, heal 20 damage from it.',
            passive=standard_passive('Whenever you attach an Energy card from your hand to this Pokémon, heal 20 damage from it.'),
        ),
        Attack(
            title='Gigas Punch',
            game_text='Flip 2 coins. If both of them are tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
