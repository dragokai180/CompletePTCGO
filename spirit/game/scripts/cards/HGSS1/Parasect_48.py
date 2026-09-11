from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='622177d5-75d0-54f2-8767-573df976dba1',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name',
    display_name='Parasect',
    searchable_by=['Parasect', 'Stage 1', 'Parasect'],
    subtypes=['Stage 1'],
    collector_number=48,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name',
    family_id=46,
    abilities=[
        Attack(
            title='Sleep Drain',
            game_text='The Defending Pokémon is now Asleep. Remove 4 damage counters from Parasect.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
