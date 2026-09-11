from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d359566-67bd-53f9-ad30-0d51121fec68',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name',
    display_name='Ferroseed',
    searchable_by=['Ferroseed', 'Basic', 'Ferroseed'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=597,
    abilities=[
        Attack(
            title='Continuous Tumble',
            game_text='Flip a coin until you get tails. This attack does 20 damage for each heads.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
