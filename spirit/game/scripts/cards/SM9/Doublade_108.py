from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9b70f64-7452-579f-bd30-dc6410097577',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    display_name='Doublade',
    searchable_by=['Doublade', 'Stage 1', 'Doublade'],
    subtypes=['Stage 1'],
    collector_number=108,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Tool Drop',
            game_text='This attack does 30 damage for each Pokémon Tool card attached to all Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
