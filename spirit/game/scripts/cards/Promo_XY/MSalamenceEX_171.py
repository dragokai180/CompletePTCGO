from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c948a6c5-4052-5a6a-8b58-c9968bf2f5bb',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MSalamenceEX.Name',
    display_name='M Salamence-EX',
    searchable_by=['M Salamence-EX', 'MEGA', 'EX', 'MSalamenceEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=171,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.SalamenceEX.Name',
    family_id=373,
    abilities=[
        Attack(
            title='Savage Wing',
            game_text='Discard as many basic Fire Energy attached to this Pokémon as you like. This attack does 40 more damage for each Energy card you discarded in this way.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
