from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='11dee799-c334-5d11-9fe1-db0f01600cfc',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name',
    display_name='Raikou',
    searchable_by=['Raikou', 'Basic', 'Raikou'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS19'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Attack(
            title='Zap Cannon',
            game_text="During your next turn, Raikou can't use Zap Cannon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
