from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8598bcd-a292-5335-b47d-8b67cccd22a6',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    display_name='Skiploom',
    searchable_by=['Skiploom', 'Stage 1', 'Skiploom'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    family_id=187,
    abilities=[
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
