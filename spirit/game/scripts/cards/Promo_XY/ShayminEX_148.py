from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db7627e5-ae1d-538b-9867-899fae093bdb',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShayminEX.Name',
    display_name='Shaymin-EX',
    searchable_by=['Shaymin-EX', 'Basic', 'EX', 'ShayminEX'],
    subtypes=['Basic', 'EX'],
    collector_number=148,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=492,
    abilities=[
        Ability(
            title='Aroma of Gratitude',
            game_text='Once during your turn (before your attack), you may heal 20 damage from each of your Benched Basic Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Floral Gain',
            game_text='Heal 20 damage and remove all Special Conditions from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
