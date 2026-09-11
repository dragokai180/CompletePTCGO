from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='243befce-6950-5585-9304-37ce7e7ea7d7',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    display_name='Quilava',
    searchable_by=['Quilava', 'Stage 1', 'Quilava'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    family_id=155,
    abilities=[
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy attached to Quilava.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
