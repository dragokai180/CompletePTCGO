from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90378e52-2a9b-5862-a6c4-5cf27b69cf35',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    display_name='Spearow',
    searchable_by=['Spearow', 'Basic', 'Spearow'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=21,
    abilities=[
        Attack(
            title='Roost',
            game_text="Remove 4 damage counters from Spearow. Spearow can't retreat during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
