from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f73eeedd-5823-59a6-84c2-1a0a55e3979e',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name',
    display_name='Arceus',
    searchable_by=['Arceus', 'Basic', 'Arceus'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=493,
    abilities=[
        Attack(
            title='Gather Light',
            game_text='Move as many Energy as you like from your Benched Pokémon to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Judgment Blast',
            game_text='This attack does 30 more damage for each different type of basic Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
