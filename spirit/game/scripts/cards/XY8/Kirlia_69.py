from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='41b3f92a-5099-5420-8a29-3e1785343aa2',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    display_name='Kirlia',
    searchable_by=['Kirlia', 'Stage 1', 'Kirlia'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    family_id=280,
    abilities=[
        Attack(
            title='Beckon',
            game_text='Put a Supporter card from your discard pile into your hand.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Quick Turn',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
