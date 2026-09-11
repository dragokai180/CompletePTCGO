from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='adb94b4f-7534-58c4-8c29-6061669acbf5',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name',
    display_name='Scizor',
    searchable_by=['Scizor', 'Stage 1', 'Scizor'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    family_id=123,
    abilities=[
        Attack(
            title='Cut',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
