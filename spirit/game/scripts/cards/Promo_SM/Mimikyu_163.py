from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e0cb3ea-0956-54bb-98d2-4eddf01be725',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name',
    display_name='Mimikyu',
    searchable_by=['Mimikyu', 'Basic', 'Mimikyu'],
    subtypes=['Basic'],
    collector_number=163,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title='Mimic',
            game_text="Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Play Rough',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
