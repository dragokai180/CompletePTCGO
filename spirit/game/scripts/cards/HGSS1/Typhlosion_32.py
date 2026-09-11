from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01c8fe29-570e-5521-85dd-0f0e1e90958f',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name',
    display_name='Typhlosion',
    searchable_by=['Typhlosion', 'Stage 2', 'Typhlosion'],
    subtypes=['Stage 2'],
    collector_number=32,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    family_id=155,
    abilities=[
        Attack(
            title='Magma Punch',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title='Fire Spin',
            game_text='Discard 2 Energy attached to Typhlosion.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
