from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9038dd25-1717-5d33-a785-dcbf1fa8edf8',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name',
    display_name='Duosion',
    searchable_by=['Duosion', 'Stage 1', 'Duosion'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name',
    family_id=577,
    abilities=[
        Attack(
            title='Double Link',
            game_text='If Solosis is on your Bench, this attack does 30 more damage. If Duosion is on your Bench, this attack does 60 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
