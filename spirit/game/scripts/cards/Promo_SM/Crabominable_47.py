from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0bb43b80-75a2-5586-a79b-b2d69f9ec1ee',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabominable.Name',
    display_name='Crabominable',
    searchable_by=['Crabominable', 'Stage 1', 'Crabominable'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    family_id=740,
    abilities=[
        Attack(
            title='Gutsy Hammer',
            game_text='This Pokémon does 10 damage to itself for each damage counter on it.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Double Stomp',
            game_text='Flip 2 coins. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
