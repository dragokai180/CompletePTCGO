from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6761fc75-2d55-5981-84d2-75bb8f262483',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LightToxtricity.Name',
    display_name='Light Toxtricity',
    searchable_by=['Light Toxtricity', 'Stage 1', 'LightToxtricity'],
    subtypes=['Stage 1'],
    collector_number=137,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH137'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    family_id=848,
    abilities=[
        Attack(
            title='Slow Ballad',
            game_text='Heal 30 damage from both Active Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Beatdown Smash',
            game_text="During your next turn, this Pokémon can't use Beatdown Smash.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
